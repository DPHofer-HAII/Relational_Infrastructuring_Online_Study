import pandas as pd
import json


def clean_text(text):
    if isinstance(text, str):
        return text.strip(';').strip()
    return text


def csv_to_jsonl(csv_file, jsonl_file):
    # Load CSV into a pandas DataFrame
    df = pd.read_csv(csv_file, sep=';')

    # Ensure there is data to process
    if df.empty:
        raise ValueError("CSV file is empty")

    # Define the static role
    static_role = "You are a health-care assistant focused on facilitating physical activity recommendations and motivation. Your task is to analyze the user's message and provide a recommendation score and, if appropriate, a motivational message based on the contextual features explicitly stated in the user's input.\n\nGuidelines for analysis:\n1. Only consider information that is explicitly stated in the user's message.\n2. Pay special attention to the Big Five personality traits if they are mentioned.\n3. If information is missing or stated as 'na' or 'nan', you may infer based on the available information.\n\nGenerating recommendations and messages:\n1. Provide a recommendation score from 1 = disagree strongly (don't send message) to 5 = agree strongly (absolutely send message) based on the contextual features.\n2. If the recommendation score is 2 or higher, generate a motivational message.\n3. The message should be tailored to the explicitly stated information, with a special focus on personality traits if mentioned.\n4. Do not mention personality traits in the message if they are not explicitly stated in the user's input.\n\nOutput your recommendation and message (if applicable) in the following format:\n<recommendation>\nScore: [Your score here]\nReasoning: [Your reasoning for the score]\nMessage: [Your message here, if score is 2 or higher]\n</recommendation>\n\nBased on the information provided in the user's message, provide your recommendation score, reasoning, and a motivational message (if applicable) within the <recommendation> tags."

    # Convert each row into the required dictionary format
    entries = []
    for id_row, row in df.iterrows():
        id_col = ""  # Modify this if necessary based on data structure

        # Determine job situation
        if row["EFT"] == "Yes;":
            job_situation = "full-time"
        elif row["EPT"] == "Yes;":
            job_situation = "part-time"
        elif row["SEP"] == "Yes;":
            job_situation = "self-employed"
        else:
            job_situation = "NaN"

        user_data = (
            f"The user is between {clean_text(row['Age'])} years old, {clean_text(row['Gender'])} with a {job_situation} job. "
            f"Their contextual features are the following: "
        )

        scenario_data = (
                user_data +
                f"It's {clean_text(row['DOW' + id_col])} and the time is {clean_text(row['TOD' + id_col])}. "
                f"Looking outside, I notice the weather is {clean_text(row['WF2H' + id_col])}. "
                f"Currently, I am {clean_text(row['US' + id_col])} (status: at work/on vacation/etc.) "
                f"and {clean_text(row['CA' + id_col])} (current activity). "
                f"On a scale from 0-100, my mood today is {clean_text(row['M' + id_col])}, "
                f"and my stress level is {clean_text(row['SL' + id_col])}. "
                f"The last time I checked my smartphone was {clean_text(row['LIWS' + id_col])} (hours/minutes ago). "
                f"When I look at my calendar for today, I see these entries: {clean_text(row['CET' + id_col])}. "
                f"From where I am, I can easily reach these places within a kilometer: {clean_text(row['CLOC' + id_col])} (list nearby locations). "
                f"Regarding physical activity today, my motivation level is {clean_text(row['MPAT' + id_col])} (0-100), "
                f"while my perceived barriers are {clean_text(row['BPAT' + id_col])} (0-100). "
                f"I {clean_text(row['PASFT' + id_col])} (had/didn't have) physical activity scheduled for today, "
                f"and I {clean_text(row['PAPT' + id_col])} (did/didn't complete) the planned activity. "
                f"During the day, I {clean_text(row['NST' + id_col])} (did/didn't) receive any PA intervention or support. "
                f"Looking ahead to tomorrow, I {clean_text(row['PASND' + id_col])} (have/don't have) physical activity planned. "
                f"Thinking about my wellness, my sleep quality last night was {clean_text(row['LNSQ' + id_col])} (0-100). "
                f"Considering my scheduled activities for today, my confidence in completing them under the current circumstances is {clean_text(row['SE' + id_col])} (0-100). "
                f"My big five personality traits are the following: reserved {clean_text(row['Reserved'])}, trusting {clean_text(row['Trusting'])}, lazy {clean_text(row['Lazy'])}, handles stress well {clean_text(row['HSW'])}, few artistic interests {clean_text(row['FAI'])}, outgoing/sociable {clean_text(row['OS'])}, finds faults with others {clean_text(row['FFO'])}, does a thorough job {clean_text(row['DTJ'])}, gets nervous easily {clean_text(row['GNE'])}, has an active imagination {clean_text(row['HAI'])}, is considerate and kind to almost everyone {clean_text(row['CKE'])}."
        )
        outcome = f"{clean_text(row.get('AS', ''))} {clean_text(row.get('EnhancedMessage', ''))}".strip()
        entries.append({
            "messages": [
                {"role": "system", "content": static_role},
                {"role": "user", "content": scenario_data},
                {"role": "assistant", "content": outcome}
            ]
        })

    # Write to JSONL file
    with open(jsonl_file, 'w', encoding='utf-8') as f:
        for entry in entries:
            json.dump(entry, f, ensure_ascii=False)
            f.write("\n")

    print(f"Successfully saved {len(entries)} entries to {jsonl_file}")


# Example usage
csv_to_jsonl('THE_Dataset_JITAI_BFPT.csv', 'THE_Dataset_JITAI_BFPT_with_BFPT.jsonl')
