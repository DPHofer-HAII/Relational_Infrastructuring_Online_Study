import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

client = OpenAI(api_key=api_key)

response = client.files.create(
  file=open("THE_Dataset_JITAI_BFPT_with_BFPT.jsonl", "rb"),
  purpose="fine-tune"
)

print(response)