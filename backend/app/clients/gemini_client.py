"""
The one place the Gemini SDK client gets constructed.

Every agent (and Subpart 0's script) imports `client` from here instead
of building its own genai.Client(). If we later add retry logic, request
logging, or swap to a different provider, this is the only file that
changes.
"""

from google import genai

from backend.app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)
