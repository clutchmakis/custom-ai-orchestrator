import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types



def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Send a prompt to Gemini and print the model response and token usage."
    )
    _ = parser.add_argument(
        "user_prompt",
        type=str,
        help="The prompt to send to the Gemini API.",
    )
    _ = parser.add_argument(
        "--verbose", action="store_true", help="Enable verbose output"
    )
    args = parser.parse_args()

    # Load environment variables from .env
    load_dotenv()

    # Read API key
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    # Initialize Gemini client
    client = genai.Client(api_key=api_key)

    # Build request content
    # messages = create_message(args.user_prompt)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Generate content
    response = generate_content(client, messages)
    
    # Craft it into beautiful text 
    content = response.text
    # Printing statistics 
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        # Print response + token stats
        print_stats(response)

    print(content)
    

def generate_content(client, message):
    
    response = client.models.generate_content(
        model="gemma-4-26b-a4b-it",
        contents=message,
    )

    return response
    
def print_stats(response):
    
    # Print the number of tokens used in the response
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    # Print the generated content
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
