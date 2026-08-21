"""
Subpart 1: Structured output — the JD Parser agent.

Run from the project root:

    python -m backend.scripts.subpart1_jd_parser
"""

from pathlib import Path

from backend.app.agents.jd_parser import parse_job_description

JD_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "sample_job_descriptions"
    / "sample_ba_role.txt"
)
job_description = JD_PATH.read_text()

parsed = parse_job_description(job_description)

print(parsed.model_dump_json(indent=2))