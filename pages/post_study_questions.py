import streamlit as st
import os
import json
import pandas as pd
from datetime import datetime

SAVE_DIR = "responses"
os.makedirs(SAVE_DIR, exist_ok=True)

if 'psq_1' not in st.session_state:
    st.session_state['psq_1'] = None
if 'psq_2' not in st.session_state:
    st.session_state['psq_2'] = None
if 'psq_3' not in st.session_state:
    st.session_state['psq_3'] = None
if 'psq_4' not in st.session_state:
    st.session_state['psq_4'] = None
if 'psq_5' not in st.session_state:
    st.session_state['psq_5'] = None
if 'psq_6' not in st.session_state:
    st.session_state['psq_6'] = None
if 'psq_7' not in st.session_state:
    st.session_state['psq_7'] = None
if 'psq_8' not in st.session_state:
    st.session_state['psq_8'] = None
if 'psq_9' not in st.session_state:
    st.session_state['psq_9'] = None
if 'psq_10' not in st.session_state:
    st.session_state['psq_10'] = None
if 'psq_11' not in st.session_state:
    st.session_state['psq_11'] = None
    
def set_new_index_psq_1_value():
    st.session_state.psq_1 = st.session_state.key_psq_1
def set_new_index_psq_2_value():
    st.session_state.psq_2 = st.session_state.key_psq_2
def set_new_index_psq_3_value():
    st.session_state.psq_3 = st.session_state.key_psq_3
def set_new_index_psq_4_value():
    st.session_state.psq_4 = st.session_state.key_psq_4
def set_new_index_psq_5_value():
    st.session_state.psq_5 = st.session_state.key_psq_5
def set_new_index_psq_6_value():
    st.session_state.psq_6 = st.session_state.key_psq_6
def set_new_index_psq_7_value():
    st.session_state.psq_7 = st.session_state.key_psq_7
def set_new_index_psq_8_value():
    st.session_state.psq_8 = st.session_state.key_psq_8
def set_new_index_psq_9_value():
    st.session_state.psq_9 = st.session_state.key_psq_9
def set_new_index_psq_10_value():
    st.session_state.psq_10 = st.session_state.key_psq_10
def set_new_index_psq_11_value():
    st.session_state.psq_11 = st.session_state.key_psq_11

def collect_full_session_state():
    """
    Returns a dict of all entries in st.session_state.
    If a value is not JSON-serializable, convert it to string.
    """
    full = {}
    for k, v in st.session_state.items():
        try:
            # Test JSON serialization
            json.dumps(v)
            full[k] = v
        except Exception:
            # Fallback: stringify
            full[k] = str(v)
    return full

def save_full_session_state_to_files():
    """
    Saves the entire st.session_state to JSON and CSV in SAVE_DIR.
    - JSON keeps nested structures when possible.
    - CSV lists key,value (stringified) per row.
    """
    session_data = collect_full_session_state()

    metadata = {
        "prolific_id": st.session_state.get("prolific_id"),
        "timestamp": datetime.now().isoformat(),
        "start_time": st.session_state.get("start_time"),
    }

    output = {
        "metadata": metadata,
        "session_state": session_data
    }

    # Filename base: uuid + timestamp
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = f"{st.session_state['prolific_id']}_{ts}"

    json_path = os.path.join(SAVE_DIR, base_name + ".json")
    csv_path = os.path.join(SAVE_DIR, base_name + ".csv")

    # Save JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Prepare a DataFrame for CSV: two columns key and value (stringified)
    rows = []
    for k, v in session_data.items():
        # Convert value to string for CSV
        rows.append({"key": k, "value": str(v)})
    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False, encoding="utf-8")

    #st.success(f"All session_state saved to:\n• {json_path}\n• {csv_path}")

def save_then_show():
    save_full_session_state_to_files()
    # Use session_state flag to indicate saved; next rerun shows link
    st.session_state["can_navigate"] = True

st.set_page_config(layout="wide")

st.header("Post-Study Questionnaire")

st.write(r'''$\textsf{\large Please fill out the following questions truthfully and as spontaneous as possible: }$''')

with st.container(border=True):
    psq_1_option_list = ["Mostly random or generic", "Sometimes felt tailored to me", "Often felt personal or adapted to me", "I’m not sure"]
    if st.session_state.psq_1 is None:
        index_variable_psq_1 = None
    else:
        index_variable_psq_1 = psq_1_option_list.index(st.session_state.psq_1)
    st.session_state.psq_1 = st.radio(r'''$\textsf{\large Which of these statements best describes how the messages felt to you overall? (Select which applies the most) *}$''', psq_1_option_list,
                                       index=index_variable_psq_1, key="key_psq_1", horizontal=True, on_change=set_new_index_psq_1_value)

with st.container(border=True):
    if st.session_state.psq_2 is None:
        index_variable_psq_2 = None
    else:
        index_variable_psq_2 = st.session_state.psq_2
    st.session_state.psq_2 = st.text_input(label=r'''$\textsf{\large Could you identify specific elements of the messages that reflected your personality traits? If yes, please describe. *}$''',
                                           placeholder="Please insert here", key="key_psq_2", on_change=set_new_index_psq_2_value,
                                           value=index_variable_psq_2)

with st.container(border=True):
    if st.session_state.psq_3 is None:
        index_variable_psq_3 = None
    else:
        index_variable_psq_3 = st.session_state.psq_3
    st.session_state.psq_3 = st.text_input(label=r'''$\textsf{\large Did any of the messages make you feel understood or emotionally connected? Which ones, and why? *}$''',
                                           placeholder="Please insert here", key="key_psq_3", on_change=set_new_index_psq_3_value,
                                           value=index_variable_psq_3)

with st.container(border=True):
    psq_4_option_list = ["References to your personal goals or progress", "Timing aligned with your daily schedule or calendar",
                         "Mood or energy level", "Information about the weather or location", "Encouragement based on your past activity",
                         "Social or community context", "Preferences for tone or style"]
    if st.session_state.psq_4 is None:
        index_variable_psq_4 = None
    else:
        index_variable_psq_4 = st.session_state.psq_4
    st.session_state.psq_4 = st.multiselect(
        label=r'''$\textsf{\large Which of the following personal details or context information would you find helpful for future messages? Select all that apply: * }$''',
        options=psq_4_option_list, key="key_psq_4", on_change=set_new_index_psq_4_value, accept_new_options=False, default=index_variable_psq_4,
    )

with st.container(border=True):
    psq_5_option_list = ["Messages sound like they were written for me", "Messages give me a useful idea or suggestion",
                         "Messages use a friendly or supportive tone", "Messages are brutally honest",
                         "The timing of the messages fit well with my day", "Messages are connected to my goals or activity level",
                         "Messages help me feel encouraged or confident"]
    if st.session_state.psq_5 is None:
        index_variable_psq_5 = None
    else:
        index_variable_psq_5 = st.session_state.psq_5
    st.session_state.psq_5 = st.multiselect(
        label=r'''$\textsf{\large How important are the following features in helping to motivate you? (Select all that apply): *}$''',
        options=psq_5_option_list, key="key_psq_5", on_change=set_new_index_psq_5_value, accept_new_options=False, default=index_variable_psq_5
    )

with st.container(border=True):
    if st.session_state.psq_6 is None:
        index_variable_psq_6 = None
    else:
        index_variable_psq_6 = st.session_state.psq_6
    st.session_state.psq_6 = st.text_input(label=r'''$\textsf{\large Was there anything missing from the messages that would have made them feel more empathic or emotionally intelligent? Please describe. *}$''',
                                           placeholder="Please insert here", key="key_psq_6", on_change=set_new_index_psq_6_value,
                                           value=index_variable_psq_6)

with st.container(border=True):
    if st.session_state.psq_7 is None:
        index_variable_psq_7 = None
    else:
        index_variable_psq_7 = st.session_state.psq_7
    st.session_state.psq_7 = st.text_input(label=r'''$\textsf{\large Did any message feel more “human” or natural in tone? What made you feel that way? *}$''',
                                           placeholder="Please insert here", key="key_psq_7", on_change=set_new_index_psq_7_value,
                                           value=index_variable_psq_7)

with st.container(border=True):
    if st.session_state.psq_8 is None:
        index_variable_psq_8 = None
    else:
        index_variable_psq_8 = st.session_state.psq_8
    st.session_state.psq_8 = st.text_input(label=r'''$\textsf{\large Do you have any other suggestions or making motivational messages more engaging or useful? *}$''',
                                           placeholder="Please insert here", key="key_psq_8", on_change=set_new_index_psq_8_value,
                                           value=index_variable_psq_8)

with st.container(border=True):
    if st.session_state.psq_9 is None:
        index_variable_psq_9 = None
    else:
        index_variable_psq_9 = st.session_state.psq_9
    st.session_state.psq_9 = st.text_input(label=r'''$\textsf{\large Which aspects of the message (timing, content, tone, etc.) made it feel relevant - or not? *}$''',
                                           placeholder="Please insert here", key="key_psq_9", on_change=set_new_index_psq_9_value,
                                           value=index_variable_psq_9)

with st.container(border=True):
    if st.session_state.psq_10 is None:
        index_variable_psq_10 = None
    else:
        index_variable_psq_10 = st.session_state.psq_10
    st.session_state.psq_10 = st.text_input(label=r'''$\textsf{\large What kind of message would increase your likelihood of acting on it? *}$''',
                                           placeholder="Please insert here", key="key_psq_10", on_change=set_new_index_psq_10_value,
                                           value=index_variable_psq_10)

with st.container(border=True):
    if st.session_state.psq_11 is None:
        index_variable_psq_11 = None
    else:
        index_variable_psq_11 = st.session_state.psq_11
    st.session_state.psq_11 = st.text_input(label=r'''$\textsf{\large Any other ideas of how to personalize your message? Any ideas are welcome: *}$''',
                                           placeholder="Please insert here", key="key_psq_11", on_change=set_new_index_psq_11_value,
                                           value=index_variable_psq_11)

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/scenario_1_new.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    if (st.session_state.psq_1 is not None and st.session_state.psq_2 is not None and st.session_state.psq_3 is not None
            and st.session_state.psq_4 is not None and st.session_state.psq_5 != None and st.session_state.psq_6 != None
            and st.session_state.psq_7 != None and st.session_state.psq_8 != None and st.session_state.psq_9 != None
            and st.session_state.psq_10 != None and st.session_state.psq_11 != None):
        if st.button("Submit Data", on_click=save_then_show, key="btn_next"):
            # This block runs on the same run as on_click, but typically link appears on next rerun
            pass

        # After rerun, if saved:
        if st.session_state.get("can_navigate"):
            st.success("Data saved. Please use the following to finish the study:")
            st.page_link("pages/ending_page.py", label="Go to Ending Page", icon=":material/arrow_forward:")
        #st.page_link("pages/ending_page.py", label="Next Page", icon=":material/arrow_forward:")

st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')