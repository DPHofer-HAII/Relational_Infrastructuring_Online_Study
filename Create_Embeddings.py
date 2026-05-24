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
        row["job_situation"] = "full-time"
    elif row["EPT"] == "Yes;":
        row["job_situation"] = "part-time"
    elif row["SEP"] == "Yes;":
        row["job_situation"] = "self-employed"
    else:
        row["job_situation"] = "NaN"

    scenario_dataframe = [clean_text(row['Age']), clean_text(row['Gender']), row['job_situation'], clean_text(row['DOW' + id_col]),
                    clean_text(row['TOD' + id_col]), clean_text(row['WF2H' + id_col]), clean_text(row['US' + id_col]),
                    clean_text(row['CA' + id_col]), clean_text(row['M' + id_col]), clean_text(row['SL' + id_col]),
                    clean_text(row['LIWS' + id_col]), clean_text(row['CET' + id_col]), clean_text(row['CLOC' + id_col]),
                    clean_text(row['MPAT' + id_col]), clean_text(row['BPAT' + id_col]), clean_text(row['PASFT' + id_col]),
                    clean_text(row['PAPT' + id_col]), clean_text(row['NST' + id_col]), clean_text(row['PASND' + id_col]),
                    clean_text(row['LNSQ' + id_col]), clean_text(row['SE' + id_col]), clean_text(row['Reserved']),
                    clean_text(row['Trusting']), clean_text(row['Lazy']), clean_text(row['HSW']), clean_text(row['FAI']),
                    clean_text(row['OS']), clean_text(row['FFO']), clean_text(row['DTJ']), clean_text(row['GNE']),
                    clean_text(row['HAI']), clean_text(row['CKE'])]

    embedding_row = embed(scenario_dataframe)
    embedding_list.append(embedding_row)

se = pd.Series(embedding_list)
data["embeddings"] = se.values

# Save to CSV
output_file = "THE_Dataset_JITAI_BFPT_with_embeddings.csv"
# data.drop(columns=["EFT", "EPT", "SEP"], inplace=True)
data.to_csv(output_file, index=False)
print(f"Embeddings saved to {output_file}")
