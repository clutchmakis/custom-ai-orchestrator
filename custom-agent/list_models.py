import os

from dotenv import load_dotenv
from google import genai

# Load the environment
load_dotenv()

# Load the API key from the .env file
api_key = os.environ.get("GEMINI_API_KEY")

# Check if the API key is set
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY environment variable not set")

# Initialize the Gemini API client
client = genai.Client(api_key=api_key)

# List all available models
print("Available Gemini Models:")
print("-" * 60)

models = client.models.list()
for model in models:
    print(f"\nModel: {model.name}")
    if hasattr(model, "display_name"):
        print(f"  Display Name: {model.display_name}")
    if hasattr(model, "description"):
        print(f"  Description: {model.description}")
    if hasattr(model, "supported_generation_methods"):
        print(f"  Supported Methods: {model.supported_generation_methods}")
