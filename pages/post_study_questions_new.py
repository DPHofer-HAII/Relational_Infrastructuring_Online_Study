import streamlit as st
import os
import json
import pandas as pd
from datetime import datetime

SAVE_DIR = "responses"
os.makedirs(SAVE_DIR, exist_ok=True)

st.set_page_config(layout="wide")
st.header("Post-Study Questionnaire")
st.write(r'''$\textsf{\large Please fill out the following questions truthfully and as spontaneous as possible: }$''')

# Configuration for each question: key in session_state, widget type, label, options if applicable, and extra params.
questions = [
    {
        "key": "psq_1",
        "type": "radio",
        "label": r'''$\textsf{\large Which of these statements best describes how the messages felt to you overall? (Select which applies the most) *}$''',
        "options": ["Mostly random or generic", "Sometimes felt tailored to me",
                    "Often felt personal or adapted to me", "I’m not sure"],
        "horizontal": True
    },
    {
        "key": "psq_2",
        "type": "text_input",
        "label": r'''$\textsf{\large Could you identify specific elements of the messages that reflected your personality traits? If yes, please describe. *}$''',
        "placeholder": "Please insert here"
    },
    {
        "key": "psq_3",
        "type": "text_input",
        "label": r'''$\textsf{\large Did any of the messages make you feel understood or emotionally connected? Which ones, and why? *}$''',
        "placeholder": "Please insert here"
    },
    {
        "key": "psq_4",
        "type": "multiselect",
        "label": r'''$\textsf{\large Which of the following personal details or contexts would you find helpful for future messages? Select all that apply: * }$''',
        "options": ["References to your personal goals or progress",
                    "Timing aligned with your daily schedule or calendar",
                    "Mood or energy level", "Information about the weather or location",
                    "Encouragement based on your past activity",
                    "Social or community context", "Preferences for tone or style"],
        "accept_new_options": True
    },
    {
        "key": "psq_5",
        "type": "multiselect",
        "label": r'''$\textsf{\large How important are the following features in helping to motivate you? (Select all that apply): *}$''',
        "options": ["Messages sound like they were written for me", "Messages give me a useful idea or suggestion",
                    "Messages use a friendly or supportive tone", "Messages are brutally honest",
                    "The timing of the messages fit well with my day",
                    "Messages are connected to my goals or activity level",
                    "Messages help me feel encouraged or confident"],
        "accept_new_options": False
    },
    {
        "key": "psq_6",
        "type": "text_input",
        "label": r'''$\textsf{\large Was there anything missing from the messages that would have made them feel more empathic or emotionally intelligent? Please describe. *}$''',
        "placeholder": "Please insert here"
    },
    {
        "key": "psq_7",
        "type": "text_input",
        "label": r'''$\textsf{\large Did any message feel more “human” or natural in tone? What made you feel that way? *}$''',
        "placeholder": "Please insert here"
    },
    {
        "key": "psq_8",
        "type": "text_input",
        "label": r'''$\textsf{\large Do you have any other suggestions or making motivational walking messages more engaging or useful? *}$''',
        "placeholder": "Please insert here"
    },
    {
        "key": "psq_9",
        "type": "text_input",
        "label": r'''$\textsf{\large Which aspects of the message (timing, content, tone) made it feel relevant - or not? *}$''',
        "placeholder": "Please insert here"
    },
    {
        "key": "psq_10",
        "type": "text_input",
        "label": r'''$\textsf{\large What kind of message would increase your likelihood of acting on it? *}$''',
        "placeholder": "Please insert here"
    },
]

# Initialize all psq keys in session_state to None if not present
for q in questions:
    st.session_state.setdefault(q["key"], None)

def collect_full_session_state():
    """
    Returns a dict of all entries in st.session_state.
    If a value is not JSON-serializable, convert it to string.
    """
    full = {}
    for k, v in st.session_state.items():
        try:
            json.dumps(v)
            full[k] = v
        except Exception:
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
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    prof_id = st.session_state.get("prolific_id", "unknown")
    base_name = f"{prof_id}_{ts}"
    json_path = os.path.join(SAVE_DIR, base_name + ".json")
    csv_path = os.path.join(SAVE_DIR, base_name + ".csv")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    rows = []
    for k, v in session_data.items():
        rows.append({"key": k, "value": str(v)})
    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False, encoding="utf-8")

def save_then_show():
    save_full_session_state_to_files()
    st.session_state["can_navigate"] = True

# Render each question inside a container
for q in questions:
    with st.container():
        key = q["key"]
        widget_type = q["type"]
        label = q.get("label", "")
        if widget_type == "radio":
            options = q["options"]
            # Determine index if already answered
            current = st.session_state.get(key)
            if current in options:
                index = options.index(current)
                value = st.radio(label, options, index=index, key=key, horizontal=q.get("horizontal", False))
            else:
                value = st.radio(label, options, key=key, horizontal=q.get("horizontal", False))
            st.session_state[key] = value

        elif widget_type == "multiselect":
            options = q["options"]
            default = st.session_state.get(key) or []
            value = st.multiselect(
                label,
                options=options,
                default=default,
                key=key,
                accept_new_options=q.get("accept_new_options", False)
            )
            st.session_state[key] = value

        elif widget_type == "text_input":
            # If value is None, use empty string so widget doesn't error
            default = st.session_state.get(key) or ""
            value = st.text_input(label, placeholder=q.get("placeholder", ""), key=key, value=default)
            st.session_state[key] = value

# Navigation buttons at bottom
c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/scenario_1_new.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    # Ensure required questions are answered (none are None or empty for text-based)
    required_keys = ["psq_1", "psq_2", "psq_3", "psq_4", "psq_5", "psq_6", "psq_7", "psq_8", "psq_9", "psq_10"]
    all_filled = True
    for rk in required_keys:
        val = st.session_state.get(rk)
        # For multiselect/radio/text: consider empty string or empty list as not filled
        if val is None or (isinstance(val, str) and val.strip() == "") or (isinstance(val, list) and len(val) == 0):
            all_filled = False
            break
    if all_filled:
        if st.button("Next Page", on_click=save_then_show, key="btn_next"):
            pass
        if st.session_state.get("can_navigate"):
            st.success("Data saved. Use the link below to continue:")
            st.page_link("pages/ending_page.py", label="Go to Ending Page", icon=":material/arrow_forward:")

st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')
