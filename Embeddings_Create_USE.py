import numpy as np
import pandas as pd
import tensorflow_hub as hub
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
embed = hub.load(module_url)

# Load the dataset
file_path = "THE_Dataset_JITAI_BFPT.csv"
data = pd.read_csv(file_path, delimiter=';')
data_dropna = data.dropna()

# Clean text columns by removing trailing semicolons
def clean_text(text):
    if isinstance(text, str):
        return text.strip(';').strip()
    return text

# Define job situation

embedding_list = []

for id_row, row in data_dropna.iterrows():
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

    # scenario_dataframe = [clean_text(row['Age']), clean_text(row['Gender']), row['job_situation'], clean_text(row['DOW' + id_col]),
    #                 clean_text(row['TOD' + id_col]), clean_text(row['WF2H' + id_col]), clean_text(row['US' + id_col]),
    #                 clean_text(row['CA' + id_col]), clean_text(row['M' + id_col]), clean_text(row['SL' + id_col]),
    #                 clean_text(row['LIWS' + id_col]), clean_text(row['CET' + id_col]), clean_text(row['CLOC' + id_col]),
    #                 clean_text(row['MPAT' + id_col]), clean_text(row['BPAT' + id_col]), clean_text(row['PASFT' + id_col]),
    #                 clean_text(row['PAPT' + id_col]), clean_text(row['NST' + id_col]), clean_text(row['PASND' + id_col]),
    #                 clean_text(row['LNSQ' + id_col]), clean_text(row['SE' + id_col]), clean_text(row['Reserved']),
    #                 clean_text(row['Trusting']), clean_text(row['Lazy']), clean_text(row['HSW']), clean_text(row['FAI']),
    #                 clean_text(row['OS']), clean_text(row['FFO']), clean_text(row['DTJ']), clean_text(row['GNE']),
    #                 clean_text(row['HAI']), clean_text(row['CKE'])]

    user_data = (
        f"The user is between {clean_text(row['Age'])} years old, {clean_text(row['Gender'])} with a {job_situation} job. "
        f"Their contextual features are the following: "
    )

    scenario_data = [(
            user_data + ", "
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
            # f"My big five personality traits are the following: reserved {clean_text(row['Reserved'])}, trusting {clean_text(row['Trusting'])}, "
            #             f"lazy {clean_text(row['Lazy'])}, handles stress well {clean_text(row['HSW'])}, "
            #             f"few artistic interests {clean_text(row['FAI'])}, outgoing/sociable {clean_text(row['OS'])}, "
            #             f"finds faults with others {clean_text(row['FFO'])}, does a thorough job {clean_text(row['DTJ'])}, "
            #             f"gets nervous easily {clean_text(row['GNE'])}, has an active imagination {clean_text(row['HAI'])}, "
            #             f"is considerate and kind to almost everyone {clean_text(row['CKE'])}."
    )]

    embedding_row = embed(scenario_data)
    embedding_list.append(embedding_row)

embeddings_numpy = np.array(embedding_list)
np.save("embeddings_sentences_without_BFPT.npy", embeddings_numpy)
