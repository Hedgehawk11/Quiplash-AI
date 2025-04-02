import os
from openai import OpenAI

print("\n the format for this is: Instructions: word")

def send_message(question):
    token = "YOUR_TOKEN_HERE"
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "gpt-4o"

    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a player in a game called quiplash."
                           "Your role is to provide humorous and witty responses to the prompts given. "
                           "You should aim to be funny, clever, and engaging."
                           "Remember, the goal is to entertain and amuse the other players. "
                           "Please keep your responses under 45 characters to ensure they fit within the game constraints. "
                           "Do not provide explanations or context for your answers. Just give the quip directly."
                           "This is round three, everyone in the game is getting one prompt"
                           "This is word lash, you will be provided with a word and instructions in the format of 'Instructions: word'"
                        

            },
            {
                "role": "user",
                "content": question,
            }
        ],
        model=model_name,
        temperature=1.,
        max_tokens=1000,
        top_p=1.
    )

    return response.choices[0].message.content

while True:
    question = input('\nWhat is your question?\n')
    if question.lower() in ['exit', 'quit']:
        break
    response = send_message(question)
    print("\n" + response)