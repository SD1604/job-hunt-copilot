"""
The shared state every node reads from and writes to as it moves
through the graph.

Kept in its own file, separate from build_graph.py, on purpose — the
SHAPE of the data (this file) and the WIRING between nodes
(build_graph.py) are different concerns that change for different
reasons. Starts minimal: one field added per subpart, not everything
up front, so it's always obvious which subpart introduced which piece
of data.
"""

from typing import Optional, TypedDict

from backend.app.agents.jd_parser import ParsedJobDescription
from backend.app.agents.resume_tailor import TailoredResume


class GraphState(TypedDict):
    raw_job_description: str
    parsed_job: Optional[ParsedJobDescription]
    base_resume: str
    tailored_resume: Optional[TailoredResume]