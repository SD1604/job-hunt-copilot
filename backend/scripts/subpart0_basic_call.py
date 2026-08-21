"""
Subpart 0: Raw LLM API call — no LangChain, no LangGraph, no framework.

Goal: understand what actually happens on an API call before a framework
starts hiding it from you. Every abstraction added later (chains, agents,
graphs) is ultimately just wrapping this.

Run from the project root as a module, so the `backend.app...` imports
resolve correctly:

    python -m backend.scripts.subpart0_basic_call
"""

from pathlib import Path

from backend.app.clients.gemini_client import client
from backend.app.config import CHAT_MODEL

# 1. Read the sample JD from data/, not from a hardcoded string in this
#    file. Path(__file__).resolve() makes this work no matter what
#    directory you run the script from.
JD_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "sample_job_descriptions"
    / "sample_ba_role.txt"
)
job_description = JD_PATH.read_text()

# 2. The system instruction sets the model's role/behavior for this call.
#    Kept separate from the user input on purpose — it's the model's
#    "job description," not part of the conversation content.
system_instruction = "You are a career assistant that summarizes job descriptions concisely."

# 3. The actual API call. Everything here is explicit: which model, the
#    system instruction, and the input text.
interaction = client.interactions.create(
    model=CHAT_MODEL,
    system_instruction=system_instruction,
    input=(
        "Summarize this job description in exactly 3 bullet points, "
        f"focused on required skills and seniority level:\n\n{job_description}"
    ),
)

# 4. output_text is a convenience property that joins the response's
#    text content for you. The real response object has more structure
#    (usage metadata, multiple content blocks) — worth a look with
#    print(interaction) once, just to see what's underneath.
print(interaction.output_text)
