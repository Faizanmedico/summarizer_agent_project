# connection.py
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load environment variables from .env
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("Missing GEMINI_API_KEY in .env")

# Create external Gemini-compatible OpenAI client
# This base_url points to the Gemini API's OpenAI-compatible endpoint
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Create model
# We'll use 'gemini-1.5-flash' for efficiency
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)

# Define run config
run_config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True # Disable tracing for now to avoid extra setup/warnings
)

# Export for main.py
def get_config():
    return run_config