import os
import pandas as pd
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

client_openai = OpenAI(api_key=OPENAI_API_KEY)


def extract_user_message(user_prompt):
    try:
        chat_completion_groq_one_shot = client_openai.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an intelligent assistant here to extract personalized messages from the text given. Only extract the part of the message received that clearly indicates that it is a message intended for a user. Never paraphrase or rewrite anything! If you do not find a message please show the following: 'For this context no JITAI would be sent!' "
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            model="gpt-4o-2024-08-06",
            store=True,
            temperature=0.2,
            seed=1615610578,
        )
        return chat_completion_groq_one_shot.choices[0].message.content
    except Exception as e:
        print(e)


# def local_model(user_prompt):
