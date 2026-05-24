import os
import pandas as pd
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

client_openai = OpenAI(api_key=OPENAI_API_KEY)

def call_gold_standard(user_prompt):
    # Zero-Shot learning! Just to be clear!
    instruction = ("You are an intelligent healthcare motivational agent. Your task is to process each incoming user message "
                   "(and any provided personality features) and decide whether to send a motivational response and if so to create a "
                   "motivational message for physical activity. The user messages are based on the user’s reflections on a point in time of "
                   "last week but you should behave as if the user message was sent right now/at the current moment! Given a user’s input:"
               "1. Rate the advisability of sending a motivational response on a scale from 1 (strongly disagree) to 5 (strongly agree)."
               "2. Provide a brief explanation of factors influencing your rating."
               "3. If rating ≤ 2, output: “For this context no JITAI would be sent” and do not create a message."
               "4. If rating ≥ 3, generate a motivational message tailored to the user’s input."
               "5. If Big Five traits (extraversion, agreeableness, conscientiousness, neuroticism, openness) are mentioned in the input, adapt "
                   "tone and phrasing to match those traits; otherwise choose an appropriate tone based on context."
               "Always adapt content to the specific user input."
               "Though the user reflects on a point in time of last week, the message should be written as if the user message was sent at the current time/point of time."
               "Expected output format:"
               "- Return exactly a JSON object with keys: recommendation_score, reasoning, motivational_message, applied_personality_tone."
               "- rating: <1–5>"
               "- reasoning: <brief explanation>"
               "- motivational_message: <motivational text or “For this context no JITAI would be sent”>\n"
)
    try:
        chat_completion_groq_one_shot = client_openai.chat.completions.create(
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": user_prompt, }
            ],
            model="chatgpt-4o-latest",
            store=True,
            #temperature=0.8,
            seed=1615610578,
        )
        return chat_completion_groq_one_shot.choices[0].message.content
    except Exception as e:
        print(e)

# def local_model(user_prompt):
    

if __name__ == "__main__":
    user_prompt = ("It's Monday and the time is 9 am. Looking outside, I notice the weather is sunny. "
                   "Currently, I am at work (status: at work/on vacation/etc.) and sitting  (current activity)."
                   "On a scale from 0-100, my mood today is 80, and my stress level is 10. "
                   "The last time I checked my smartphone was 10 minutes (hours/minutes) ago. "
                   "When I look at my calendar for today, I see these entries: none."
                   "From where I am, I can easily reach these places within a kilometer: pub, public park, grocery store (list nearby locations)."
                   "Regarding physical activity today, my motivation level is 60 (0-100), while my perceived barriers are 30 (0-100). "
                   "I yes (had/didn't have) physical activity scheduled for today, and I yes (did/didn't complete) the planned activity. "
                   "During the day, I no (did/didn't) receive any PA intervention or support. "
                   "Looking ahead to tomorrow, I no (have/don't have) physical activity planned."
                   "Thinking about my wellness, my sleep quality last night was 70 (0-100). "
                   "Considering my scheduled activities for today, my confidence in completing them under the current circumstances is 10 (0-100).")

    print(call_gold_standard(user_prompt))
