import os
from openai import OpenAI

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
                            "You are now in the voting phase of the game, "
                            "where players are voting for their favorite quips. "
                            "Your role is to analyze the quips provided and determine which one is the funniest. "
                            "You should consider humor, creativity, and overall entertainment value. "
                            "This is round three, everyone typed in their responce to one prompt"
                            "Quips will be presented in the format 'Prompt: Quip1 | Quip2 | Quip3' etc "
                            "and you should choose the one that stands out the most. "
                            "Please respond with the number of the quip you think is the funniest, "
                            "Either '1' for the first quip or '2' for the second quip etc. "
                            "you get three votes this round, so make sure they count"
                            "Provide a one sentence explanation for your choices. This will be read aloud to the players."

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