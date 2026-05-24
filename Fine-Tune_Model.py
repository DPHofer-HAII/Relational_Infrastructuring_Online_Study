# LAST USAGE. WITHOUT BFPT!!!

import os
from openai import OpenAI

# Load OpenAI API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

client = OpenAI(api_key=api_key)

# Create fine-tuning job
fine_tune_response = client.fine_tuning.jobs.create(
    model="gpt-4o-2024-08-06",
    training_file=os.environ.get("OPENAI_TRAINING_FILE_ID"),  # see platform.openai.com - dashboard - storage
    seed=1615610578
)

print(fine_tune_response)
