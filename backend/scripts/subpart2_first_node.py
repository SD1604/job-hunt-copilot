"""
Subpart 2: first LangGraph node.

Run from the project root:

    python -m backend.scripts.subpart2_first_node
"""

from pathlib import Path

from backend.app.graph.build_graph import build_graph

JD_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "sample_job_descriptions"
    / "sample_ba_role.txt"
)
job_description = JD_PATH.read_text()

graph = build_graph()

result = graph.invoke({"raw_job_description": job_description, "parsed_job": None})

print(result["parsed_job"].model_dump_json(indent=2))