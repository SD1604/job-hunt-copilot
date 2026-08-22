"""
Subpart 3: second node + real edge (Resume Tailor).

Run from the project root:

    python -m backend.scripts.subpart3_resume_tailor
"""

from pathlib import Path

from backend.app.graph.build_graph import build_graph

ROOT = Path(__file__).resolve().parents[2]
job_description = (ROOT / "data" / "sample_job_descriptions" / "sample_ba_role.txt").read_text()
base_resume = (ROOT / "data" / "resumes" / "sample_base_resume.txt").read_text()

graph = build_graph()

result = graph.invoke(
    {
        "raw_job_description": job_description,
        "parsed_job": None,
        "base_resume": base_resume,
        "tailored_resume": None,
    }
)

print(result["tailored_resume"].model_dump_json(indent=2))