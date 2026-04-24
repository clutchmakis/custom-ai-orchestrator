def generate_content(client, message):
    
    response = client.models.generate_content(
        model="gemma-4-26b-a4b-it",
        contents=message,
    )

    return response