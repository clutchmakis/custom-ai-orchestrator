def print_stats_and_response(response):
    # Print the prompt
    print(
        "User prompt: Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )

    # Print the number of tokens used in the response
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    # Print the generated content
    print("Response:")
    print(response.text)
