from google.genai import types


# Create a message
def create_message(user_prompt: str) -> list[types.Content]:
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    
    return messages
