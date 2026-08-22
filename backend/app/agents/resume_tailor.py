"""
Resume Tailor agent.

Takes the parsed job description (from jd_parser) plus a candidate's
base resume, and returns which required skills are already evidenced
in the resume, which are missing, and a set of tailored bullet points.

The "matched vs missing" split matters as much as the rewritten
bullets: it forces the model to reason about EVIDENCE in the resume
before writing anything, rather than freely inventing experience that
sounds good. That instruction is explicit below, on purpose.
"""

from typing import List

from pydantic import BaseModel, Field

from backend.app.agents.jd_parser import ParsedJobDescription
from backend.app.clients.gemini_client import client
from backend.app.config import CHAT_MODEL


class TailoredResume(BaseModel):
    matched_skills: List[str] = Field(
        description="Required skills from the JD that the resume already demonstrates."
    )
    missing_skills: List[str] = Field(
        description="Required skills from the JD with no clear evidence in the resume."
    )
    tailored_bullets: List[str] = Field(
        description=(
            "3-5 rewritten resume bullet points, based only on experience "
            "already present in the resume, emphasizing relevance to this role."
        )
    )


def tailor_resume(parsed_job: ParsedJobDescription, base_resume: str) -> TailoredResume:
    interaction = client.interactions.create(
        model=CHAT_MODEL,
        system_instruction=(
            "You are a resume tailoring assistant. You rewrite resume bullet "
            "points to align with a specific job description. You NEVER invent "
            "experience, tools, or skills that aren't already present in the "
            "candidate's resume — you only reframe and emphasize what's real."
            "You NEVER invent experience, tools, skills, or specific contexts/domains "
            "that aren't already present in the candidate's resume — you only "
            "reframe and emphasize what's explicitly stated."
        ),
        input=(
            f"Job role: {parsed_job.role}\n"
            f"Seniority: {parsed_job.seniority}\n"
            f"Required skills: {', '.join(parsed_job.required_skills)}\n\n"
            f"Candidate's base resume:\n{base_resume}\n\n"
            "First identify which required skills are matched vs missing in "
            "the resume, then rewrite 3-5 bullet points tailored to this role."
        ),
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": TailoredResume.model_json_schema(),
        },
    )
    return TailoredResume.model_validate_json(interaction.output_text)