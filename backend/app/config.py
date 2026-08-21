"""
Central configuration.

This is the ONLY file in the project allowed to read from os.environ or
.env directly. Every other module imports settings from here instead of
touching the environment itself — so rotating a key, changing a model
name, or adding a second provider later means editing this one file,
not searching the whole repo for os.environ.get(...) calls.
"""

import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Centralizing the model name here too — when Subpart 5 needs a cheaper/
# faster model for the supervisor vs. a stronger one for tailoring, this
# is where that split gets defined, not scattered across agent files.
CHAT_MODEL = "gemini-3.5-flash"

if not GEMINI_API_KEY:
    raise EnvironmentError(
        "GEMINI_API_KEY not found. Copy .env.example to .env in the "
        "backend/ folder and add your key from https://aistudio.google.com/apikey"
    )
