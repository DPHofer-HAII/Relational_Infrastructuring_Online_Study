import os

import numpy as np
import pandas as pd
from openai import OpenAI
import tensorflow_hub as hub
from scipy.spatial import distance

# Load OpenAI API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

client_openai = OpenAI(api_key=api_key)

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
embed = hub.load(module_url)

# Load the dataset
file_path = "THE_Dataset_JITAI_BFPT.csv"
dataset = pd.read_csv(file_path, delimiter=';')

# Load the Embeddings
all_embeddings_without_BFPT = np.load("embeddings_sentences_without_BFPT.npy")
all_embeddings_with_BFPT = np.load("embeddings_sentences_with_BFPT.npy")

def _creating_the_examples(ei, example_question, example_answer):

    cot_prompt = (
        "You are a health assistant. Your mission is to read the given health query with the label and then return "
        "an answer with short explanation that's supporting the label.\nQuestion: {}\nLabel: {}.").format(
        example_question, example_answer)

    for attempt in range(3):
        try:
            chat_completion_groq_one_shot = client_openai.chat.completions.create(
                messages=[
                    {"role": "system", "content": ""},
                    {"role": "user", "content": cot_prompt, }
                ],
                model="chatgpt-4o-latest",
                store=True,
                seed=1615610578,
            )
            explanation = chat_completion_groq_one_shot.choices[0].message.content
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == 2:
                raise

    return "\n[Example {}]\n{}\nExplanation: {}\nAnswer: {}\n".format(ei + 1, example_question, explanation,
                                                                           example_answer)

# Universally used
def _send_to_chatgpt_with_BFPT(examples, question):
    instruction = (
        "You are an intelligent healthcare agent for motivational messages. Your task is to process each incoming user message and decide whether to send a motivational response to foster physical activity, or not. In addition, the user input will include messages from other users that were perceived as closely related to the user’s context and potentially personality traits – given a database. Follow these steps precisely:"
        "1. Input Schema:"
        "- user_message: The raw text the user sends."
        "- optional personality_features: If the user or retrieved context suggests any of the Big Five traits (extraversion, agreeableness, conscientiousness, neuroticism, openness), these will be provided here (e.g., {'Extraversion: 1', ‘Agreeableness: 4‘, ‘Conscientiousness: 4 ', ‘Neuroticism: 3', ‘Openness: 3’}) – they are optional and will not always be given!"
        "- retrieved_examples: A list of example objects. Each example object has:"
        "• example_message: a prior user message (may be similar in theme)."
        "• example_explanation: an LLM-generated rationale or commentary about that example."
        "• example_user_evaluation: an integer 1–5 indicating how strongly sending a motivational message was recommended for that example."
        "2. Analysis & RAG Integration:"
        "a. Content Analysis:"
        "- Examine user_message: detect contextual cues, emotion features like stress and affect, possible need for encouragement or caution."
        "- Compare semantic and emotional parallels between user_message and each retrieved example (using the example_explanation to understand context)."
        "b. Analysis of Examples:"
        "- Use the retrieved_examples to inform both rating and message phrasing:"
        "• If an example_user_evaluation was high and example_explanation indicates why, compare user_message to that example."
        "• Avoid copying content; instead, adapt patterns (tone, structure) that succeeded in examples."
        "- If retrieved_examples list is empty, proceed based solely on user_message analysis."
        "3. JITAIs:"
        "a. Definition:"
        "- JITAIs are automated, data driven prompts tailored in real time to the user’s context, vulnerability, and receptivity."
        "b. When to send:"
        "- Moments of vulnerability – when the user is likely to lapse (e.g., craving, prolonged sedentary time)"
        "- Moments of opportunity – when the user is receptive and able to act (e.g., idle time between meetings)"
        "- When context data suggest it is safe and the user is likely receptive"
        "c. When to withhold:"
        "-During contexts with high demand/workload, sleep or other busy contexts."
        "- If a user’s schedule or location suggests they are unable to respond effectively (busy meetings, sleeping)"
        "- If the user is already engaged in physical activity."
        "- If user already did some physical activity."
        "4. Evaluation:"
        "a. Recommendation Scoring:"
        "- On a scale 1–5, rate “How strongly do you recommend sending a motivational message?”"
        "• 1 = strongly disagree (do not send)"
        "• 2 = disagree"
        "• 3 = neutral / borderline"
        "• 4 = agree"
        "• 5 = strongly agree"
        "- Justify the rating by referencing specific aspects: e.g., contextual cues, emotional tone, risk, readiness to change, similarity to retrieved examples, overall benefit vs. potential harm or irrelevance."
        "- If there is relevant clinical or safety concern (e.g., signs of crisis or need for professional care), a lower recommendation may be warranted; mention this explicitly in your reasoning."
        "c. Decision Rule:"
        "- If your rating is ≥ 3 (neutral, agree, or strongly agree), proceed to generate a motivational message."
        "- If your rating is ≤ 2, explicitly state: “No motivational message generated,” and explain what factors led to that decision."
        "d. Reasoning Explanation:"
        "- Provide a structured rationale: list key factors in bullet or numbered form (e.g., “1. Contextual Cues: geolocation stated close to a forest therefore forest bathing was recommended; 2. Emotional tone: hopeful but anxious; 3. Similar example had evaluation 4 and succeeded in encouraging self-care; 4. Personality features: high neuroticism → choose calming language,” etc.)."
        "- Reference any retrieved example(s) when they influenced your decision (“Example #2 showed a user in a similar situation who responded positively to reassurance about small steps.”)."
        "- If you decide not to send a message, clearly state “No motivational message generated” and summarize factors."
        "5. Message Generation (if recommendation ≥ threshold):"
        "a. Personalization via Personality Features:"
        "- personalize based on the Big Five Personality Trait (50 = highest till 5 = lowest). Make sure to understand the combination of traits/the spectrum the user has and generate a message accordingly"
        "- For every personality trait there is a definition, list of words describing the core quality, as well as a list of words describing people ranking high and low in the personality trait"
        "• Extraversion"
        "o Definition: a tendency to seek stimulation in the company of others"
        "o Core Quality: sociability, energy from social interaction, assertiveness, emotional expression"
        "o People ranking high are Extroverts: extroverted, excitement seeking, attention seeking, outgoing, warm, seeking adventure, outgoing, enthusiastic in groups, often energized by social situations, happy to be the center of attention"
        "o People ranking low are Introverts: Socially withdrawn, detached coldness, quiet, reserved, prefers solitary or small-group settings, fatigued by too much social interaction, reflective"
        "• Agreeableness"
        "o Definition: a tendency to be compassionate and cooperative towards others"
        "o Core Quality: cooperative, empathy, trustworthy, good-natured, maintaining harmony in relationships"
        "o People ranking high are Agreeable: submissiveness, selflessness, gullibility, helpful, trusting/forgiving, empathetic, supportive, team-oriented, straightforward, altruistic, compliant, modest, sympathetic"
        "o People ranking low are Antagonistic: deceitfulness, manipulativeness, callousness, critical, uncooperative, suspicious, competitive, skeptical, demanding, insulting, stubborn, show-offs, unsympathetic, less caring"
        "• Conscientiousness:"
        "o Definition: a tendency that a person acts in an organized or spontaneous way"
        "o Core Quality: self-discipline, organization, and goal-directed behaviour, competence, thoughtfulness, goal driven"
        "o People ranking high are conscientious: perfectionism, workaholism, hardworking, dependable, organized, reliable, persistent, good at planning, competent, dutiful, achievement-striving, self-disciplined, considerate"
        "o People ranking low are unconscientious: distractibility, irresponsibility, rashness, impulsive, careless, disorganized, easily distracted, less structured, incompetent, procrastinator, undisciplined"
        "• Neuroticism:"
        "o Definition: the extent to which a person’s emotion is sensitive to the environment"
        "o Core Quality: tendency towards unstable emotions, tendency toward emotional volatility versus calmness and resilience"
        "o People ranking high are neurotic: depressivity, emotional lability, shamefulness, anxious, unhappy, prone to negative emotions, prone to worry, mood swings, very stressed, may experience anxiety more frequently, hostile (irritable), self-conscious (shy), vulnerable, experiencing dramatic shifts in mood"
        "o People ranking low are emotionally stable: fearlessness, shamelessness, calm, even-tempered, secure, generally calm, secure, and resilient when facing challenges, laid back, emotionally stable, confident, rarely sad or depressed"
        "• Openness:"
        "o Definition: the extent to which a person is open to experience a variety of activities"
        "o Core Quality: imagination, feelings, actions, ideas, curiosity, creativity, willingness to explore new ideas or activities"
        "o People ranking are open to experience: magical thinking, eccentricity, curious, wide range of interests, independent, enjoys variety, embraces change, likely to engage in creative or unconventional pursuits, imaginative, open to trying new things"
        "o People ranking low are closed to experience: inflexible, close-minded, practical, conventional, prefers routine, prefers routine and tradition, values practicality over novelty, predictable, not very imaginative, uncomfortable with change, strict with routine, traditional"
        "- If no personality info, choose balanced empathetic-professional tone."
            "b. Content & Style:"
                "- Mention contextual factors stated by the user so that they feel understood"
                "- Keep concise (1–4 short paragraphs or bullet points)"
                "- Avoid jargon; ensure clarity."
                "- Encourage specific, achievable actions or mindset shifts without making promises."
                "- Keep in mind that the user reflects on a point in time of last week but the message must be written as if the user is currently in this situation and you make the decision if a message should be sent and if so what the content needs to be to motivate them for physical activity."
                "- Never use ‘//n’ or ‘\\n’"
            "c. Safety & Boundaries:"
                "- If user_message hints at crisis or medical risk, lower recommendation as needed; if still ≥ threshold, message may include encouragement to seek professional help—but only if clearly relevant."
                "- Never claim to replace professional care."
            "d. Transparency:"
                "- Omit apologies or disclaimers like “I’m not a professional.” You may express uncertainty concisely: “This approach may help based on what you shared…”"
                "- Do not mention “I am an AI.”"
            "e. Output Fields:"
                "- recommendation_score: <integer 1–5>"
                "- reasoning: Consolidated rationale as described."
                "- motivational_message: Generated text or the literal “No motivational message generated.”"
                "- applied_personality_tone: Brief note on how traits shaped tone."
        "6. Response Format:"
            "- Return exactly a JSON object with keys: recommendation_score, reasoning, motivational_message, applied_personality_tone."
            "- Do not include extra keys or metadata."
            "- Ensure “reasoning” is formatted in bullet or numbered form, human-readable."
            "- Ensure “motivational_message” is plain text, may include line breaks."
        "Overall, ensure your internal reasoning is explicit, tie decisions to retrieved examples when available, and personalize the tone according to any Big Five features. Output must follow the JSON structure exactly and not contain apologies or self-referential disclaimers."
    )

    final_user_prompt = examples + "\nFinally, please answer to the below question:\n" + question
    try:
        chat_completion_groq_one_shot = client_openai.chat.completions.create(
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": final_user_prompt, }
            ],
            model="chatgpt-4o-latest",
            store=True,
            seed=1615610578,
        )
        return chat_completion_groq_one_shot.choices[0].message.content
    except Exception as e:
        print(e)

def _process_cosine_data(cosine_distance_list):
    # Pick the three closest examples
    indexed_numbers = list(enumerate(cosine_distance_list))  # Pair numbers with their indices
    indexed_numbers.sort(key=lambda x: x[1])  # Sort based on values

    lowest_three = indexed_numbers[:3]  # Get three lowest
    # print(lowest_three[0][0])
    # print(lowest_three)
    # print(data.iloc[lowest_three[0][0]])

    return lowest_three

def _compute_cosine_distances(scenario_data: str, embeddings) -> list:
    embedding_row = embed([scenario_data])
    return [distance.cosine(embedding_row[0], emb[0]) for emb in embeddings]

def _get_data_answer(context_data):
    return context_data["AS"] + " " + context_data["EnhancedMessage"]

def _create_information(context_data):
    
    if context_data.get("EFT") == "Yes;":
        job_situation = "full-time"
    elif context_data.get("EPT") == "Yes;":
        job_situation = "part-time"
    elif context_data.get("SEP") == "Yes;":
        job_situation = "self-employed"
    else:
        job_situation = "NaN"

    user_data = ("The user is between " + context_data.get("Age") + " years old, " + context_data.get("Gender") + " with a " + job_situation + " job. "
                "Their contextual features are the following:")

    storyline = ("It's " + str(context_data.get("DOW")) + "and the time is " + str(context_data.get("TOD")) + ". Looking outside, I notice the weather is " + str(context_data.get("WF2H")) + ". Currently, I am " + str(context_data.get("US")) + " (status: at work/on vacation/etc.) and " + str(context_data.get("CA")) + "  (current activity)."
    "On a scale from 0-100, my mood today is " + str(context_data.get("M")) + " , and my stress level is " + str(context_data.get("SL")) + ". The last time I checked my smartphone was " + str(context_data.get("LIWS")) + " (hours/minutes ago). When I look at my calendar for today, I see these entries: " + str(context_data.get("CET")) + "."
    "From where I am, I can easily reach these places within a kilometer: " + str(context_data.get("CLOC")) + " (list nearby locations)."
    "Regarding physical activity today, my motivation level is " + str(context_data.get("MPAT")) + " (0-100), while my perceived barriers are " + str(context_data.get("BPAT")) + " (0-100). I " + str(context_data.get("PASFT")) + " (had/didn't have) physical activity scheduled for today, and I " + str(context_data.get("PAPT")) + " (did/didn't complete) the planned activity. During the day, I " + str(context_data.get("NST")) + " (did/didn't) receive any PA intervention or support. Looking ahead to tomorrow, I " + str(context_data.get("PASND")) + " (have/don't have) physical activity planned."
    "Thinking about my wellness, my sleep quality last night was " + str(context_data.get("LNSQ")) + " (0-100). Considering my scheduled activities for today, my confidence in completing them under the current circumstances is " + str(context_data.get("SE")) + " (0-100).")

    bfpt_information = (
        f"My big five personality traits are the following: reserved {context_data.get('Reserved')}, trusting {context_data.get('Trusting')}, "
        f"lazy {context_data.get('Lazy')}, handles stress well {context_data.get('HSW')}, "
        f"few artistic interests {context_data.get('FAI')}, outgoing/sociable {context_data.get('OS')}, "
        f"finds faults with others {context_data.get('FFO')}, does a thorough job {context_data.get('DTJ')}, "
        f"gets nervous easily {context_data.get('GNE')}, has an active imagination {context_data.get('HAI')}, "
        f"is considerate and kind to almost everyone {context_data.get('CKE')}."
    )


    scenario_data_without_bfpt = user_data + " " + storyline
    scenario_data_with_bfpt = user_data + " " + storyline + " " + bfpt_information

    return scenario_data_without_bfpt, scenario_data_with_bfpt

def get_ragging(scenario_data_without_bfpt_old, scenario_data_with_bfpt_old, scenario_data_without_bfpt_new, scenario_data_with_bfpt_new):
    examples_with_BFPT = ""
    examples_without_BFPT = ""

    # scenario_data_without_bfpt, scenario_data_with_bfpt = _create_information(context_data)
    most_similar_with_BFPT = _process_cosine_data(
        _compute_cosine_distances(scenario_data_with_bfpt_old, all_embeddings_with_BFPT)
    )
    for ei, (idx, _) in enumerate(most_similar_with_BFPT):
        _, ctx = _create_information(dataset.iloc[idx])
        examples_with_BFPT += _creating_the_examples(ei, ctx, _get_data_answer(dataset.iloc[idx]))
    answer_with_BFPT = _send_to_chatgpt_with_BFPT(examples_with_BFPT, scenario_data_with_bfpt_new)

    most_similar_without_BFPT = _process_cosine_data(
        _compute_cosine_distances(scenario_data_without_bfpt_old, all_embeddings_without_BFPT)
    )
    for ei, (idx, _) in enumerate(most_similar_without_BFPT):
        ctx, _ = _create_information(dataset.iloc[idx])
        examples_without_BFPT += _creating_the_examples(ei, ctx, _get_data_answer(dataset.iloc[idx]))
    answer_without_BFPT = _send_to_chatgpt_with_BFPT(examples_without_BFPT, scenario_data_without_bfpt_new)


    return answer_without_BFPT, answer_with_BFPT, examples_without_BFPT, examples_with_BFPT





if __name__ == "__main__":
    # Example data
    age = "36-year-old"
    gender = "male"
    job_situation = "full-time"
    day_of_week = "moodonday"
    time_of_day = "10:00"
    weather = "rainy"
    user_status = "sassy"
    current_activity = "work"
    mood = "50"
    stress_level = "50"
    last_interaction = "20 minutes"
    calender_entries = "none"
    close_locations = "park, bus station"
    motivation_pa = "30"  # Look at it again!
    barrier_pa = "70"
    pa_scheduled_today = "running in a circle"
    pa_performed_today = "none"
    jitai_sent_today = "yes"
    pa_scheduled_tomorrow = "no"
    last_nights_sleep_quality = "30"
    self_efficacy = "10"
    reserved = "agree strongly"
    trusting = "agree a little"
    lazy = "disagree strongly"
    handles_stress_well = "agree a little"
    few_artistic_interests = "agree a little"
    outgoing_sociable = "disagree a little"
    find_faults_with_others = "agree strongly"
    does_a_thorough_job = "agree strongly"
    gets_nervous_easily = "disagree a little"
    active_imagination = "agree strongly"
    kind_to_almost_everyone = "agree strongly"

    context_data = {"age": age, "gender": gender, "job_situation": job_situation, "reserved": reserved,
                    "trusting": trusting,
                    "lazy": lazy, "handles_stress_well": handles_stress_well, "calendar_entries": calender_entries,
                    "few_artistic_interests": few_artistic_interests, "outgoing_sociable": outgoing_sociable,
                    "find_faults_with_others": find_faults_with_others,
                    "does_a_thorough_job": does_a_thorough_job, "gets_nervous_easily": gets_nervous_easily,
                    "active_imagination": active_imagination,
                    "kind_to_almost_everyone": kind_to_almost_everyone, "day_of_week": day_of_week,
                    "time_of_day": time_of_day,
                    "user_status": user_status, "close_locations": close_locations, "weather": weather,
                    "current_activity": current_activity,
                    "mood": mood, "stress_level": stress_level, "self_efficacy": self_efficacy,
                    "last_interaction": last_interaction,
                    "last_nights_sleep_quality": last_nights_sleep_quality, "motivation_pa": motivation_pa,
                    "barrier_pa": barrier_pa,
                    "pa_scheduled_today": pa_scheduled_today, "pa_performed_today": pa_performed_today,
                    "jitai_sent_today": jitai_sent_today,
                    "pa_scheduled_tomorrow": pa_scheduled_tomorrow}


    user_data = (
        f"The user is between {context_data.get('age')} years old, {context_data.get('gender')} with a "
        f"{context_data.get('job_situation')} job. "
        f"Their contextual features are the following: "
    )

    storyline = (
        f"It's {context_data.get('day_of_week')} and the time is {context_data.get('time_of_day')}. "
        f"Looking outside, I notice the weather is {context_data.get('weather')}. "
        f"Currently, I am {context_data.get('user_status')} (status: at work/on vacation/etc.) "
        f"and {context_data.get('current_activity')} (current activity). "
        f"On a scale from 0-100, my mood today is {context_data.get('mood')}, "
        f"and my stress level is {context_data.get('stress_level')}. "
        f"The last time I checked my smartphone was {context_data.get('last_interaction')} (hours/minutes ago). "
        f"When I look at my calendar for today, I see these entries: {context_data.get('calender_entries')}. "
        f"From where I am, I can easily reach these places within a kilometer: {context_data.get('close_locations')} (list nearby locations). "
        f"Regarding physical activity today, my motivation level is {context_data.get('motivation_pa')} (0-100), "
        f"while my perceived barriers are {context_data.get('barrier_pa')} (0-100). "
        f"I {context_data.get('pa_scheduled_today')} (had/didn't have) physical activity scheduled for today, "
        f"and I {context_data.get('pa_performed_today')} (did/didn't complete) the planned activity. "
        f"During the day, I {context_data.get('jitai_sent_today')} (did/didn't) receive any pa intervention or support. "
        f"Looking ahead to tomorrow, I {context_data.get('pa_scheduled_tomorrow')} (have/don't have) physical activity planned. "
        f"Thinking about my wellness, my sleep quality last night was {context_data.get('last_nights_sleep_quality')} (0-100). "
        f"Considering my scheduled activities for today, my confidence in completing them under the current circumstances is {context_data.get('self_efficacy')} (0-100). "
    )

    bfpt_information = (
        f"My big five personality traits are the following: reserved {context_data.get('reserved')}, trusting {context_data.get('trusting')}, "
        f"lazy {context_data.get('lazy')}, handles stress well {context_data.get('handles_stress_well')}, "
        f"few artistic interests {context_data.get('few_artistic_interests')}, outgoing/sociable {context_data.get('outgoing_sociable')}, "
        f"finds faults with others {context_data.get('find_faults_with_others')}, does a thorough job {context_data.get('does_a_thorough_job')}, "
        f"gets nervous easily {context_data.get('gets_nervous_easily')}, has an active imagination {context_data.get('active_imagination')}, "
        f"is considerate and kind to almost everyone {context_data.get('kind_to_almost_everyone')}."
    )

    scenario_data_without_bfpt = user_data + " " + storyline
    scenario_data_with_bfpt = user_data + " " + storyline + " " + bfpt_information

    response_without, response_with, _, _ = get_ragging(scenario_data_without_bfpt, scenario_data_with_bfpt)
    #print(response_without)
    #print(response_with)
