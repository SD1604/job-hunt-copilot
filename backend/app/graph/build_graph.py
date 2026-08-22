"""
Graph construction.

This is where nodes get wired into an actual StateGraph. Only one node
right now (Subpart 2) — the point of this subpart isn't the wiring
itself (trivial with one node), it's learning what State actually is
before a second node and a real edge get added in Subpart 3.
"""

"""
Graph construction.

Now with a real edge between two nodes: jd_parser -> resume_tailor.
This is the first point where state produced by one node is genuinely
consumed by another, rather than a single node running in isolation.
"""

from langgraph.graph import END, START, StateGraph

from backend.app.agents.jd_parser import parse_job_description
from backend.app.agents.resume_tailor import tailor_resume
from backend.app.graph.state import GraphState


def jd_parser_node(state: GraphState) -> dict:
    parsed = parse_job_description(state["raw_job_description"])
    return {"parsed_job": parsed}


def resume_tailor_node(state: GraphState) -> dict:
    """
    Reads `parsed_job` — written by the PREVIOUS node, not this one.
    This is the actual payoff of shared state: resume_tailor never
    calls the JD parser itself, it just trusts that by the time it
    runs, parsed_job is already populated.
    """
    tailored = tailor_resume(state["parsed_job"], state["base_resume"])
    return {"tailored_resume": tailored}


def build_graph():
    workflow = StateGraph(GraphState)

    workflow.add_node("jd_parser", jd_parser_node)
    workflow.add_node("resume_tailor", resume_tailor_node)

    workflow.add_edge(START, "jd_parser")
    workflow.add_edge("jd_parser", "resume_tailor")
    workflow.add_edge("resume_tailor", END)

    return workflow.compile()