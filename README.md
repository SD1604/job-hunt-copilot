# Job-Hunt Copilot

A multi-agent system (LangGraph) that automates job search grunt work —
parsing job descriptions, tailoring resumes, drafting cold outreach, and
tracking applications — built one subpart at a time, from a raw API call
up to a deployed, persistent multi-agent graph.

Built with Gemini (chat + embeddings, free tier) and LangGraph.

## Structure

```
backend/app/       # the real package: config, clients, agents, graph, tools, api
backend/scripts/   # numbered, disposable exploration code, one per subpart
backend/tests/     # pytest, mirrors app/
data/              # sample job descriptions and other fixtures — never real personal data
docs/              # architecture notes, updated as the system grows
frontend/          # UI, added in Subpart 9
```

## Progress

- [x] Subpart 0 — Raw Gemini API call, no framework
- [ ] Subpart 1 — Structured output (JD Parser agent)
- [ ] Subpart 2 — First LangGraph node
- [ ] Subpart 3 — Second node + edge (Resume Tailor)
- [ ] Subpart 4 — Conditional routing
- [ ] Subpart 5 — Supervisor pattern (multi-agent)
- [ ] Subpart 6 — Persistent memory (Application Tracker)
- [ ] Subpart 7 — Real tool calling
- [ ] Subpart 8 — Human-in-the-loop
- [ ] Subpart 9 — Deployment (frontend + API)

## Setup

```bash
python -m venv venv
source venv/bin/activate            # macOS/Linux
pip install -r backend/requirements.txt

cp .env.example .env                # then paste your real GEMINI_API_KEY into .env
```

Free Gemini API key, no card required: https://aistudio.google.com/apikey

## Run Subpart 0

From the project root (imports rely on this):

```bash
python -m backend.scripts.subpart0_basic_call
```
