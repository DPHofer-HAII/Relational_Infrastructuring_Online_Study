import os
from groq import Groq
from openai import OpenAI

GROQ_API_KEY = os.environ['GROQ_API_KEY']
OPENAI_API_KEY = os.environ['OTHER_API_KEY']

client_groq = Groq(api_key=GROQ_API_KEY)
client_openai = OpenAI(api_key=OPENAI_API_KEY)

role_system_content_zero_shot = ("You are an intelligent healthcare agent.")
role_system_content_few_shot = ("You are a medical decision maker skilled in making decisions based on summarized reports. Given the following problem, generate mutliple answers using diverse step-by-step reasoning paths and aggregate the final answers to come to a final conclusion.")


few_shot_examples = ()

role_user_content = ("The user is 36-year-old male with a full-time job. Their contextual features are the following:"
"* Big Five Personality Traits (1 = disagree strongly - 5 = agree strongly): Extraversion: 6; Agreeableness: 1; Conscientiousness: 5; Neuroticism: 5; Openness: 2; Agreeableness item: 1."
"* Locus of Causality for Exercise (1 = disagree strongly - 7 = agree strongly): 2."
"* Rapid Assessment of Physical Activity (1 = disagree strongly - 7 agree strongly): 3."
"* Fitness goals: maintain weight; gain muscle; and manage stress."
"* On Sunday at 10 a.m., I was at work, which set the tone for my day."
"* I spent my time at the office with cloudy weather, primarily engaged in working while sitting."
"* My mood was bored, and my stress level hovered around 10 (0 = very low - 100 = very high), which I managed mediocre."
"* During this period, I experienced inefficency in handling tasks, which impacted my confidence and sense of self-efficacy."
"* Reflecting on last night’s sleep, I’d rate its quality as bad, and this left me feeling tired upon waking."
"In this regard, please predict if a just-in-time adaptive intervention should be sent (1 = disagree strongly - 5 = agree strongly) and, if so, which text it should entail? Announce the JITAI with '***' at the beginning and end!")


chat_completion_groq_one_shot = client_groq.chat.completions.create(
    messages=[
        {"role": "system", "content": role_system_content_zero_shot},
        {"role": "user", "content": role_user_content,}
    ],
    model="llama-3.3-70b-versatile",
)

chat_completion_openai_one_shot = client_openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": role_system_content_zero_shot},
        {"role": "user", "content": role_user_content,}
    ]
)

print("LLama 3.3 One-Shot")
print(chat_completion_groq_one_shot.choices[0].message.content)
print("------------------------------------------------------------------------------------------")
print("ChatGPT One-Shot")
print(chat_completion_openai_one_shot.choices[0].message.content)

#FILL IN TEXT FOR THE LLM: BASE TEXT FOR REUSE
# The user is xx-year-old GENDER with JOB_SITUATION. Their contextual features are the following:
# Big Five Personality Traits (1 = disagree strongly - 5 = agree strongly): Extraversion: XX; Agreeableness: XX; Conscientiousness: XX; Neuroticism: XX; Openness: XX; Agreeableness item: XX
# Locus of Causality for Exercise (1 = disagree strongly - 7 = agree strongly): XX
# Rapid Assessment of Physical Activity (1 = disagree strongly - 7 agree strongly): XX
# Fitness goals: XX; XX; and XX
# On DAY_TEXT at TIME_TEXT, I was USER_STATUS, which set the tone for my day.
# I spent my time at LOCATION with WEATHER, primarily engaged in ACTIVITY while POSITON_OF_BODY.
# My mood was MOOD, and my stress level hovered around STRESS (0 = very low - 100 = very high), which I managed by HANDLING.
# During this period, I experienced LOCUS_OF_CONTROL in handling tasks, which impacted my confidence and sense of self-efficacy.
# Reflecting on last night’s sleep, I’d rate its quality as SLEEP_QUALITY, and this left me feeling SLEEP_MOOD upon waking.