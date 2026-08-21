"""
JD Parser agent.

Takes a raw job description string and returns a validated, typed
ParsedJobDescription object instead of free text. This is the first
"tool-shaped" output in the project — every later agent (resume tailor,
router, tracker) depends on having reliable structured data here, not a
paragraph it has to re-interpret.
"""

from typing import List, Optional

from pydantic import BaseModel, Field

from backend.app.clients.gemini_client import client
from backend.app.config import CHAT_MODEL


class ParsedJobDescription(BaseModel):
    """
    The schema IS the contract between this agent and everything
    downstream. If a later agent needs a new field (say, `location`),
    it gets added here once — every caller benefits immediately.
    """

    company: Optional[str] = Field(
        default=None, description="Company name, if mentioned in the JD."
    )
    role: str = Field(description="The job title or role being hired for.")
    seniority: str = Field(
        description="Seniority level, e.g. Internship, Junior, Mid, Senior."
    )
    required_skills: List[str] = Field(
        description="Specific required skills, tools, or technologies mentioned."
    )
    min_experience_years: Optional[int] = Field(
        default=None,
        description="Minimum years of professional experience required, if stated.",
    )


def parse_job_description(raw_text: str) -> ParsedJobDescription:
    """
    Calls Gemini with a response_format schema so the model is
    constrained to return JSON matching ParsedJobDescription — then
    validates that JSON into an actual typed Python object.
    """
    interaction = client.interactions.create(
        model=CHAT_MODEL,
        system_instruction=(
            "You extract structured hiring data from job descriptions. "
            "Only use information present in the text — never invent details."
        ),
        input=f"Extract structured data from this job description:\n\n{raw_text}",
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": ParsedJobDescription.model_json_schema(),
        },
    )

    return ParsedJobDescription.model_validate_json(interaction.output_text)