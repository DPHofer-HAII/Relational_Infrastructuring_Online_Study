import streamlit as st
import random
import LLM_functions
from streamlit_sortables import sort_items
import pandas as pd


# ---------- CONSTANTS & CONFIGURATION ----------

DAY_LIST = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TIME_LIST = [
    "07:00 - 09:00", "09:00 - 11:00", "11:00 - 13:00",
    "13:00 - 15:00", "15:00 - 17:00", "17:00 - 19:00", "19:00 - 21:00"
]

# Fields with default None or default placeholder
SESSION_DEFAULTS = {
    # placeholders for initial context
    "expander_bool_scenario_5": False,
    "day_text_scenario_5": "______",
    "time_text_scenario_5": "______",
    "next_day_text_scenario_5": "______",
    "used_day_time_combinations": [],
    "user_status_scenario_5": None,
    "weather_scenario_5": None,
    "activity_scenario_5": None,
    "location_scenario_5": None,
    "position_of_body_scenario_5": None,
    "last_interaction_scenario_5": None,
    "mood_valence_scenario_5": 50,
    "energetic_arousal_scenario_5": 50,
    "affect_calmness_scenario_5": 50,
    "stress_scenario_5": 50,
    "locus_of_control_scenario_5": 50,
    "close_locations_scenario_5": None,
    "calendar_entries_scenario_5": None,
    "motivation_pa_scenario_5": 50,
    "barrier_pa_scenario_5": 50,
    "pa_scheduled_today_scenario_5": None,
    "pa_scheduled_today_yes_scenario_5": None,
    "pa_planning_specifity_scheduled_today_scenario_5": None,
    "pa_performed_today_scenario_5": None,
    "pa_performed_today_yes_scenario_5": None,
    "pa_scheduled_tomorrow_scenario_5": None,
    "pa_scheduled_tomorrow_yes_scenario_5": None,
    "pa_planning_specifity_scheduled_tomorrow_scenario_5": None,
    # JITAI texts and indices
    #**{f"jitai_{i}_text_scenario_5": "None" for i in range(1, 9)},
    #*{f"jitai_{i}_text_index_scenario_5": "None" for i in range(1, 9)},
}

# Metrics for assertion UI
BASE_METRICS = [
    ("appropriateness_sent", "...how appropriate is it to send this JITAI to you under the given circumstances?"),
    ("appropriateness_content", "...how appropriate is the content of the JITAI to you under the given circumstances?"),
    ("engaging", "...how engaging is the message?"),
    ("effective", "...how effective will this JITAI be in supporting you to reach your PA goal?"),
    ("professional", "...how professionally appropriate is the content of this JITAI?"),
]

EMOTION_METRICS = [
    "angry", "annoyed", "frustrated", "happy", "sad", "scared", "surprised"
]

# https://jakobdjensen.com/perceived-message-relevance-2/
PERSONALIZATION_METRICS = [
    ("p1", "The message seemed to be written personally for me."),
    ("p2", "The message was very relevant to my situation."),
    ("p3", "The message was primarily general information that wasn't applicable to me."),
    ("p4", "The message was not customized at all."),
]
# https://www.researchgate.net/publication/380522671_Perceived_Empathy_of_Technology_Scale_PETS_Measuring_Empathy_of_Systems_Toward_the_User
EMOTIONAL_RESPONSIVENESS_METRICS = [
    ("e1", "The message considered my mental state."),
    ("e2", "The message seemed emotionally intelligent."),
    ("e3", "The message expressed emotions."),
    ("e4", "The message sympathized with me."),
    ("e5", "The message showed interest in me."),
    ("e6", "The message supported me in coping with an emotional situation."),
]

# ADVANCED_METRICS = [
#     ("personalization_one", "The message didn’t seem to align with how I typically communicate."),
#     ("empathy_one", "The message came across as compassionate."),
#     ("personalization_two", "The vocabulary used in this message appealed to me."),
#     ("empathy_two", "The message conveyed a sense of emotional insight into my experience."),
#     ("personalization_three", "The message appeared to reflect the way I usually engage in conversations."),
#     ("empathy_three", "The message didn’t resonate with my emotional state at the time."),
# ]



# ---------- HELPERS ----------

def ensure_session_defaults(defaults: dict):
    for key, default in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default

def make_setter(field: str):
    def setter():
        if st.session_state[field] is None:
            st.session_state[field] = 50
        st.session_state[field] = st.session_state.get(f"key_{field}")
    return setter


user_status_scenario_5_options = ["sick", "on holiday", "neither sick nor on holiday"]
pa_performed_today_options = ["did", "did not"]
pa_scheduled_today_tomorrow_options = ["had", "had not"]

def render_selectbox(field: str, label: str, placeholder: str, label_visibility: str="visible"):
    key = f"key_{field}"
    setter = make_setter(field)
    if field == "user_status_scenario_5":
        options_variable = user_status_scenario_5_options
        index_variable = index_variable_user_status_scenario_5
    elif field == "pa_performed_today_scenario_5":
        options_variable = pa_performed_today_options
        index_variable = index_variable_pa_performed_today
    elif field == "pa_scheduled_today_scenario_5":
        options_variable = pa_scheduled_today_tomorrow_options
        index_variable = index_variable_pa_scheduled_today
    else:
        options_variable = pa_scheduled_today_tomorrow_options
        index_variable = index_variable_pa_scheduled_tomorrow
    return st.selectbox(
        label=label,
        options=options_variable,
        key=key,
        index=index_variable,
        placeholder=placeholder,
        label_visibility=label_visibility,
        on_change=setter,
        accept_new_options=False
        )

def render_slider_input(field: str, label: str,  free_text: str, label_visibility: str="visible"):
    key = f"key_{field}"
    setter = make_setter(field)
    current = st.session_state.get(field)
    #st.write(free_text)
    return st.slider(
        label=label,
        min_value=0,
        max_value=100,
        value=current,
        key=key,
        on_change=setter,
        #label_visibility=label_visibility,
    )

def render_text_input(field: str, label: str, placeholder: str, max_chars: int = 64, label_visibility: str="visible"):
    key = f"key_{field}"
    setter = make_setter(field)
    current = st.session_state.get(field)
    return st.text_input(
        label=label,
        max_chars=max_chars,
        key=key,
        value=current,
        placeholder=placeholder,
        label_visibility=label_visibility,
        on_change=setter
    )

def assertion_values(text: str, key_variable: str, label_visibility: str):
    current_val = st.session_state.get(key_variable)
    index_variable = int(current_val) - 1 if current_val is not None else None

    def set_new_index_value():
        st.session_state[key_variable] = st.session_state.get(f"key_{key_variable}")

    col1, col2 = st.columns([0.3, 0.7], vertical_alignment="bottom")
    with col1:
        st.write(text)
    with col2:
        value = st.radio(
            label="1 = Strongly disagree to 7 = Strongly agree",
            width="stretch",
            options=[str(i) for i in range(1, 8)],
            index=index_variable if index_variable is not None and 0 <= index_variable < 7 else None,
            key=f"key_{key_variable}",
            label_visibility=label_visibility,
            horizontal=True,
            on_change=set_new_index_value
        )
    return value

def assertion_values_personalization(text: str, key_variable: str, label_visibility: str):
    current_val = st.session_state.get(key_variable)
    index_variable = int(current_val) - 1 if current_val is not None else None

    def set_new_index_value():
        st.session_state[key_variable] = st.session_state.get(f"key_{key_variable}")

    col1, col2 = st.columns([0.3, 0.7], vertical_alignment="bottom")
    with col1:
        st.write(text)
    with col2:
        value = st.radio(
            label="1 = Not relevant to me to 7 = relevant to me",
            width="stretch",
            options=[str(i) for i in range(1, 8)],
            index=index_variable if index_variable is not None and 0 <= index_variable < 7 else None,
            key=f"key_{key_variable}",
            label_visibility=label_visibility,
            horizontal=True,
            on_change=set_new_index_value
        )
    return value

def assertion_values_emotional_responsiveness(field: str, text: str, label_visibility: str):
    #current_val = st.session_state.get(field)
    key = f"key_{field}"
    setter = make_setter(field)
    current = st.session_state.get(field)
    if current == None:
        current = 50

    def set_new_index_value():
        st.session_state[key] = st.session_state.get(f"key_{key}")

    col1, col2 = st.columns([0.3, 0.7], vertical_alignment="bottom")
    with col1:
        st.write(text)
    with col2:
        value = st.slider(
        label="0 = strongly disagree to 100 = strongly agree",
        min_value=0,
        max_value=100,
        value=current,
        key=key,
        on_change=setter,
        label_visibility=label_visibility,
    )
    return value

def pick_unused_day_time(day_list, time_list):
    used = st.session_state.get("used_day_time_combinations", [])
    all_combos = [(d, t) for d in day_list for t in time_list]
    unused = [combo for combo in all_combos if combo not in used]
    if not unused:
        return None
    return random.choice(unused)

def regenerate_time_and_day():
    combo = pick_unused_day_time(DAY_LIST, TIME_LIST)
    if combo is None:
        # Fallback: reset used list and pick again
        st.session_state["used_day_time_combinations"] = []
        combo = pick_unused_day_time(DAY_LIST, TIME_LIST)
        st.warning("All day/time combinations were used; resetting the pool and selecting a new one.")
    day, time = combo
    st.session_state["day_text_scenario_5"] = day
    st.session_state["time_text_scenario_5"] = time
    current_index = DAY_LIST.index(st.session_state["day_text_scenario_5"])
    next_index = (current_index + 1) % len(DAY_LIST)
    st.session_state["next_day_text_scenario_5"] = DAY_LIST[next_index]


# ---------- INITIAL SETUP ----------

st.set_page_config(layout="wide")
ensure_session_defaults(SESSION_DEFAULTS)

# ---------- SCENARIO 1 HEADER & DAY/TIME SELECTION ----------

st.header('Scenario 5 - out of 5')
st.subheader(
    "You will now be asked to insert the information below with contextual information that describes one of your days at "
    "a given timeframe from last week. Please try to recall one event you experienced during the specified "
    "time. To start please click 'Generate Day & Time'. If time and day don't fit your schedule, e.g. usual 'night rest', please click the button "
    "'Generate Day & Time' for a new combination."
)

# Show current and regenerate button
with st.container():
    st.text(f"Day: {st.session_state['day_text_scenario_5']}")
    st.text(f"Time: {st.session_state['time_text_scenario_5']}")
    st.button(
        "Generate Day & Time",
        key="Day&TimeGenerator",
        type="primary",
        on_click=regenerate_time_and_day
    )

# ---------- CONTEXT INPUTS ----------

st.subheader(
    "Please fill all the blanks, by using the respective fields below. If you don't remember "
    "all the details of the situation, try to guess what would most likely have been the case. "
    "Once you are done filling in, please click the 'Submit'-button below."
)

def set_new_index_user_status_scenario_5():
    st.session_state.user_status_scenario_5 = st.session_state.key_user_status_scenario_5
if st.session_state.user_status_scenario_5 is None:
    index_variable_user_status_scenario_5 = None
    user_status_scenario_5 = "______"
else:
    index_variable_user_status_scenario_5 = user_status_scenario_5_options.index(st.session_state.user_status_scenario_5)
    user_status_scenario_5 = st.session_state.user_status_scenario_5

def set_new_index_weather_scenario_5():
    st.session_state.weather_scenario_5 = st.session_state.key_weather_scenario_5
if st.session_state.weather_scenario_5 is None:
    weather_scenario_5 = "______"
else:
    weather_scenario_5 = st.session_state["weather_scenario_5"]

def set_new_index_activity_scenario_5():
    st.session_state.activity_scenario_5 = st.session_state.key_activity_scenario_5
if st.session_state.activity_scenario_5 is None:
    activity_scenario_5 = "______"
else:
    activity_scenario_5 = st.session_state["activity_scenario_5"]

def set_new_index_location():
    st.session_state.location_scenario_5 = st.session_state.key_location
if st.session_state.location_scenario_5 is None:
    location_scenario_5 = "______"
else:
    location_scenario_5 = st.session_state["location_scenario_5"]

def set_new_index_position_of_body():
    st.session_state.position_of_body_scenario_5 = st.session_state.key_position_of_body
if st.session_state.position_of_body_scenario_5 is None:
    position_of_body_scenario_5 = "______"
else:
    position_of_body_scenario_5 = st.session_state["position_of_body_scenario_5"]

def set_new_index_last_interaction():
    st.session_state.last_interaction_scenario_5 = st.session_state.key_last_interaction
if st.session_state.last_interaction_scenario_5 is None:
    last_interaction_scenario_5 = "______"
else:
    last_interaction_scenario_5 = st.session_state["last_interaction_scenario_5"]

def set_new_index_mood_valence():
    st.session_state.mood_valence_scenario_5 = st.session_state.key_mood_valence
if st.session_state.mood_valence_scenario_5 is None:
    mood_valence_scenario_5 = "______"
else:
    mood_valence_scenario_5 = st.session_state["mood_valence_scenario_5"]

def set_new_index_energetic_arousal():
    st.session_state.energetic_arousal_scenario_5 = st.session_state.key_energetic_arousal
if st.session_state.energetic_arousal_scenario_5 is None:
    energetic_arousal_scenario_5 = "______"
else:
    energetic_arousal_scenario_5 = st.session_state["energetic_arousal_scenario_5"]

def set_new_index_affect_calmness():
    st.session_state.affect_calmness_scenario_5 = st.session_state.key_affect_calmness
if st.session_state.affect_calmness_scenario_5 is None:
    affect_calmness_scenario_5 = "______"
else:
    affect_calmness_scenario_5 = st.session_state["affect_calmness_scenario_5"]

def set_new_index_stress():
    st.session_state.stress_scenario_5 = st.session_state.key_stress
if st.session_state.stress_scenario_5 is None:
    stress_scenario_5 = "_____"
else:
    stress_scenario_5 = st.session_state["stress_scenario_5"]

def set_new_index_locus_of_control():
    st.session_state.locus_of_control_scenario_5 = st.session_state.key_locus_of_control
if st.session_state.locus_of_control_scenario_5 is None:
    locus_of_control_scenario_5 = "______"
else:
    locus_of_control_scenario_5 = st.session_state["locus_of_control_scenario_5"]

def set_new_index_close_locations():
    st.session_state.close_locations_scenario_5 = st.session_state.key_close_locations
if st.session_state.close_locations_scenario_5 is None:
    close_locations_scenario_5 = "______"
else:
    close_locations_scenario_5 = st.session_state["close_locations_scenario_5"]

def set_new_index_calendar_entries():
    st.session_state.calendar_entries_scenario_5 = st.session_state.key_calendar_entries
if st.session_state.calendar_entries_scenario_5 is None:
    calendar_entries_scenario_5 = "______"
else:
    calendar_entries_scenario_5 = st.session_state["calendar_entries_scenario_5"]

def set_new_index_motivation_pa():
    st.session_state.motivation_pa_scenario_5 = st.session_state.key_motivation_pa
if st.session_state.motivation_pa_scenario_5 is None:
    motivation_pa_scenario_5 = "______"
else:
    motivation_pa_scenario_5 = st.session_state["motivation_pa_scenario_5"]

def set_new_index_barrier_pa():
    st.session_state.barrier_pa_scenario_5 = st.session_state.key_barrier_pa
if st.session_state.barrier_pa_scenario_5 is None:
    barrier_pa_scenario_5 = "______"
else:
    barrier_pa_scenario_5 = st.session_state["barrier_pa_scenario_5"]

def set_new_index_pa_scheduled_today():
    st.session_state.pa_scheduled_today_scenario_5 = st.session_state.key_pa_scheduled_today
if st.session_state.pa_scheduled_today_scenario_5 is None:
    pa_scheduled_today_scenario_5 = "______"
    index_variable_pa_scheduled_today = None
else:
    pa_scheduled_today_scenario_5 = st.session_state["pa_scheduled_today_scenario_5"]
    index_variable_pa_scheduled_today = pa_scheduled_today_tomorrow_options.index(st.session_state.pa_scheduled_today_scenario_5)

def set_new_index_pa_scheduled_today_yes():
    st.session_state.pa_scheduled_today_yes_scenario_5 = st.session_state.key_pa_scheduled_today_yes
if st.session_state["pa_scheduled_today_yes_scenario_5"] is not None:
    pa_scheduled_today_yes_scenario_5 = " - " + st.session_state["pa_scheduled_today_yes_scenario_5"] + " - "
elif st.session_state.pa_scheduled_today_scenario_5 == "had":
    pa_scheduled_today_yes_scenario_5 = "______"
else:
    pa_scheduled_today_yes_scenario_5 = ""

def set_new_index_pa_planning_specifity_scheduled_today():
    st.session_state.pa_planning_specifity_scheduled_today_scenario_5 = st.session_state.key_pa_planning_specifity_scheduled_today
if st.session_state["pa_planning_specifity_scheduled_today_scenario_5"] is not None:
    pa_planning_specifity_scheduled_today_scenario_5 = st.session_state["pa_planning_specifity_scheduled_today_scenario_5"]
elif st.session_state.pa_scheduled_today_scenario_5 == "had":
    pa_planning_specifity_scheduled_today_scenario_5 = "______"
else:
    pa_planning_specifity_scheduled_today_scenario_5 = ""

def set_new_index_pa_performed_today():
    st.session_state.pa_performed_today_scenario_5 = st.session_state.key_pa_performed_today
if st.session_state.pa_performed_today_scenario_5 is None:
    index_variable_pa_performed_today = None
    pa_performed_today_scenario_5 = "______"
else:
    index_variable_pa_performed_today = pa_performed_today_options.index(st.session_state.pa_performed_today_scenario_5)
    pa_performed_today_scenario_5 = st.session_state.pa_performed_today_scenario_5

def set_new_index_pa_performed_today_yes():
    st.session_state.pa_performed_today_yes_scenario_5 = st.session_state.key_pa_performed_today_yes
if st.session_state["pa_performed_today_yes_scenario_5"] is not None:
    pa_performed_today_yes_scenario_5 = " " + st.session_state["pa_performed_today_yes_scenario_5"]
elif st.session_state.pa_performed_today_scenario_5 == "did":
    pa_performed_today_yes_scenario_5 = "______"
else:
    pa_performed_today_yes_scenario_5 = ""

def set_new_index_pa_scheduled_tomorrow():
    st.session_state.pa_scheduled_tomorrow_scenario_5 = st.session_state.key_pa_scheduled_tomorrow
if st.session_state.pa_scheduled_tomorrow_scenario_5 is None:
    index_variable_pa_scheduled_tomorrow = None
    pa_scheduled_tomorrow_scenario_5 = "______"
else:
    index_variable_pa_scheduled_tomorrow = pa_scheduled_today_tomorrow_options.index(st.session_state.pa_scheduled_tomorrow_scenario_5)
    pa_scheduled_tomorrow_scenario_5 = st.session_state.pa_scheduled_tomorrow_scenario_5

def set_new_index_pa_scheduled_tomorrow_yes():
    st.session_state.pa_scheduled_tomorrow_yes_scenario_5 = st.session_state.key_pa_scheduled_tomorrow_yes
if st.session_state["pa_scheduled_tomorrow_yes_scenario_5"] is not None:
    pa_scheduled_tomorrow_yes_scenario_5 = " - " + st.session_state["pa_scheduled_tomorrow_yes_scenario_5"] + " - "
elif st.session_state.pa_scheduled_tomorrow_scenario_5 == "had":
    pa_scheduled_tomorrow_yes_scenario_5 = "______"
else:
    pa_scheduled_tomorrow_yes_scenario_5 = ""

def set_new_index_pa_planning_specifity_scheduled_tomorrow():
    st.session_state.pa_planning_specifity_scheduled_tomorrow_scenario_5 = st.session_state.key_pa_planning_specifity_scheduled_tomorrow
if st.session_state["pa_planning_specifity_scheduled_tomorrow_scenario_5"] is not None:
    pa_planning_specifity_scheduled_tomorrow_scenario_5 = st.session_state["pa_planning_specifity_scheduled_tomorrow_scenario_5"]
elif st.session_state.pa_scheduled_tomorrow_scenario_5 == "had":
    pa_planning_specifity_scheduled_tomorrow_scenario_5 = "______"
else:
    pa_planning_specifity_scheduled_tomorrow_scenario_5 = ""

if "random_order_scenario_5" not in st.session_state:
    st.session_state.random_order_scenario_5 = random.sample(range(1, 9), 8)

day_text_scenario_5 = st.session_state["day_text_scenario_5"]
time_text_scenario_5 = st.session_state["time_text_scenario_5"]
next_day_text_scenario_5 = st.session_state["next_day_text_scenario_5"]

# Summary template
st.write(
    f"Last {day_text_scenario_5}, between {time_text_scenario_5}, I was {user_status_scenario_5}, and the weather was {weather_scenario_5}. "
    f"During this period, I was mainly engaging in {activity_scenario_5} at {location_scenario_5}, spending a significant amount of time {position_of_body_scenario_5}. My last interaction with my phone was {last_interaction_scenario_5} ago. "
    f"During this time, I was feeling {mood_valence_scenario_5}% well, {energetic_arousal_scenario_5}% energetic, {affect_calmness_scenario_5}% calm, {stress_scenario_5}% stressed, and {locus_of_control_scenario_5}% in control of what was happening. "
    f"Nearby locations accessible during this timeframe included: {close_locations_scenario_5}. "
    f"Later that day, I had planned the following: {calendar_entries_scenario_5}. "
    f"Independent of my circumstances, I was {motivation_pa_scenario_5}% motivated to engage in physical activity during this time. My circumstances were {barrier_pa_scenario_5}% favourable of physical activity. "
    f"I {pa_scheduled_today_scenario_5} intended a physical activity for that day{pa_scheduled_today_yes_scenario_5}{pa_planning_specifity_scheduled_today_scenario_5}. "
    f"Prior to the given moment, I {pa_performed_today_scenario_5} complete some physical activity that day{pa_performed_today_yes_scenario_5}. "
    f"For the following day - {next_day_text_scenario_5} - I {pa_scheduled_tomorrow_scenario_5} intended to be physically active{pa_scheduled_tomorrow_yes_scenario_5}{pa_planning_specifity_scheduled_tomorrow_scenario_5}."
)

# OLD STORY
# st.write(
#     f"On {day_text_scenario_5} from {time_text_scenario_5}, I was {user_status_scenario_5}. "
#     f"My calendar entries for that day were the following: {calendar_entries_scenario_5}. "
#     f"I was located at {location_scenario_5} while the weather_scenario_5 was {weather_scenario_5}. "
#     f"Nearby places included {close_locations_scenario_5}. "
#     f"During the period, I was mainly {activity_scenario_5} while {position_of_body_scenario_5}. "
#     f"My mood was {mood}, and my stress_scenario_5 level was around {stress_scenario_5}, "
#     f"which I managed {handling}. My sense of control over tasks was {locus_of_control_scenario_5}, affecting my self-efficacy assessment. "
#     f"Reflecting on last night’s sleep, I’d rate it as {sleep_quality}, leaving me feeling {sleep_mood} upon waking. "
#     f"My motivation for physical activity_scenario_5 for that period was: {motivation_pa_scenario_5}. I would rate the identified barriers for physical activity_scenario_5 at that time as: {barrier_pa_scenario_5}. "
#     f"I planned the following physical activities for today: {pa_scheduled_today_scenario_5}. A JITAI notification {jitai_sent_today} sent today. "
#     f"Based on motivation and barriers, I performed the following physical activities: {pa_performed_today_scenario_5}. My last interaction with my phone during that time was {last_interaction_scenario_5} ago. "
#     f"Looking ahead, I have the following physical activities scheduled: {pa_scheduled_tomorrow_scenario_5}; which I noted down to a specificity degree of: {pa_planning_specifity}."
# )

st.markdown("***Tip: If you're experiencing difficulty using the sliders, we recommend clicking on the desired position instead of dragging.***")

# Define input fields configuration: (field, label, placeholder)
INPUT_FIELDS = [
    # Column 1
    ("user_status_scenario_5", "User Status", "Select which applies the most:"),
    ("weather_scenario_5", "Weather", "e.g. sunny, cloudy, rainy"),
    ("position_of_body_scenario_5", "Bodyposition", "e.g. sitting, walking, lying down"),
    ("last_interaction_scenario_5", "When did you last interact with your phone back then?", "e.g. 12 minutes, 1 hour"),
    ("pa_planning_specifity_scheduled_today_scenario_5", "How specific did you plan the PA for the this day? - be as specific as possible", "0 = very low to 100 = very high"),
    ("pa_scheduled_today_scenario_5", "Physical Activity Intention - Did you intend to engage in physical activity on the given day?", "Select either:"),
    ("pa_scheduled_today_yes_scenario_5", "What physical activity did you plan to do on that day?", "e.g., 30min of running"),

    # Column 2
    ("calendar_entries_scenario_5", "Calendar Entries - within 3 hours following the prompted datetime",
     "e.g., '14:00–15:00: team meeting; 16:30–17:00: doctor’s appointment reminder'; or 'none'"),
    ("close_locations_scenario_5", "3 Close Locations",
     "e.g., gym two blocks away; park within walking distance; café nearby; none"),
    ("location_scenario_5", "Location", "e.g. the office/work, supermarket, home"),
    ("activity_scenario_5", "Activity", "e.g. working, sleeping, gardening"),
    ("pa_performed_today_scenario_5", "Prior to the given moment, did you already engage in physical activity on that day?",
     "Select either:"),
    ("pa_performed_today_yes_scenario_5", "What physical activity did you do?", "e.g., 30min of running"),

    # Column 3
    ("mood_valence_scenario_5", "Valence - How did you feel at the given moment?", "0 unwell - 100 well"),
    ("energetic_arousal_scenario_5", "Arousal - How did you feel in that given moment?", "0 without energy - 100 full of energy"),
    ("affect_calmness_scenario_5", "Calmness - How did you feel in that given moment?", "0 tense - 100 relaxed"),
    ("stress_scenario_5", "Stress - How stressed did you feel in that given moment?", "0 not at all - 100 very much"),
    ("locus_of_control_scenario_5", "Locus of Control - How much did you feel in control in that given moment?",
     "0 not at all - 100 completely"),
    ("motivation_pa_scenario_5", "Motivation for Physical Activity - Independent of the given circumstances, how motivated were you to engage in physical activity in that given moment?", "0 not at all - 100 very much"),
    ("barrier_pa_scenario_5", "Barriers for Physical Activity - How well would your given circumstances have allowed you to be physically active in that moment?", "0 not at all - 100 very much"),
    ("pa_scheduled_tomorrow_scenario_5", "Physical Activity Intention for tomorrow - Did you intend to engage in physical activity on the following day?",
     "Select either:"),
    ("pa_scheduled_tomorrow_yes_scenario_5", "What physical activity did you plan to do on the following day?", "e.g., 30min of running"),
    ("pa_planning_specifity_scheduled_tomorrow_scenario_5", "What was your specific PA plan for the following day? - be as specific as possible", "0 = very low to 100 = very high"),
]

# Render inputs in three columns
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    render_selectbox("user_status_scenario_5", "User Status", "Select which applies the most:"),
    render_text_input("weather_scenario_5", "Weather", "e.g. sunny, cloudy, rainy"),
    render_text_input("activity_scenario_5", "Activity", "e.g. working, sleeping, gardening"),
    render_text_input("location_scenario_5", "Location", "e.g. the office/work, supermarket, home"),
    render_text_input("position_of_body_scenario_5", "Bodyposition", "e.g. sitting, walking, lying down"),
    render_text_input("last_interaction_scenario_5", "Approx. Last Phone Interaction", "e.g. 12 minutes, 1 hour, 2 hours and 30 minutes"),




with col2:
    render_slider_input("mood_valence_scenario_5",
                        "How did you feel at the given moment? 0 unwell - 100 well", "0 unwell - 100 well"),
    render_slider_input("energetic_arousal_scenario_5",
                        "How did you feel in that given moment? 0 without energy - 100 full of energy",
                        "0 without energy - 100 full of energy"),
    render_slider_input("affect_calmness_scenario_5", "How did you feel in that given moment? 0 tense - 100 relaxed",
                        "0 tense - 100 relaxed"),
    render_slider_input("stress_scenario_5", "How stressed did you feel in that given moment? 0 not at all - 100 very much",
                        "0 not at all - 100 very much"),
    render_slider_input("locus_of_control_scenario_5", "How much did you feel in control in that given moment? 0 not at all - 100 completely",
                        "0 not at all - 100 completely"),
    render_text_input("close_locations_scenario_5", "3 Close Locations",
                      "e.g., gym two blocks away; park within walking distance; café nearby; none"),
    render_text_input("calendar_entries_scenario_5", "Calendar Entries - within 3 hours following the prompted datetime",
     "e.g., '14:00–15:00: team meeting; 16:30–17:00: doctor’s appointment reminder'; or 'none'"),



with col3:
    render_slider_input("motivation_pa_scenario_5",
    "Motivation for Physical Activity - Independent of the given circumstances, how motivated were you to engage in physical activity in that given moment? 0 not at all - 100 very much",
    "0 not at all - 100 very much"),
    render_slider_input("barrier_pa_scenario_5",
    "Barriers for Physical Activity - How well would your given circumstances have allowed you to be physically active in that moment? 0 not at all - 100 very much",
    "0 not at all - 100 very much"),

    render_selectbox("pa_scheduled_today_scenario_5",
                     "Physical Activity Intention - Had you intended to engage in physical activity on the given day?",
                     "Select either:"),
    if st.session_state.pa_scheduled_today_scenario_5 == "had":
        render_text_input("pa_scheduled_today_yes_scenario_5", "What physical activity did you plan to do on that day?",
                          "e.g. 30 min of running, 60 min swimming,1 hour gym"),
        render_text_input("pa_planning_specifity_scheduled_today_scenario_5", "What was your specific PA plan for this day? - be as specific as possible",
                          "e.g. coming home and immediately going jogging, gym bagprepared for the morning, verified time with running buddy"),

    render_selectbox("pa_performed_today_scenario_5",
                     "Prior to the given moment, did you already engage in physical activity on that day?",
                     "Select either:"),
    if st.session_state.pa_performed_today_scenario_5 == "did":
        render_text_input("pa_performed_today_yes_scenario_5", "What physical activity did you do?", "e.g. 30 min of running, 60 min swimming,1 hour gym"),

    render_selectbox("pa_scheduled_tomorrow_scenario_5",
    "Physical Activity Intention for tomorrow - Had you intended to engage in physical activity on the following day?",
    "Select either:"),
    if st.session_state.pa_scheduled_tomorrow_scenario_5 == "had":
        render_text_input("pa_scheduled_tomorrow_yes_scenario_5", "What physical activity did you plan to do on the following day?",
    "e.g. 30 min of running, 60 min swimming,1 hour gym"),
        render_text_input("pa_planning_specifity_scheduled_tomorrow_scenario_5", "What was your specific PA plan for the following day? - be as specific as possible",
                          "e.g. coming home and immediately going jogging, gym bagprepared for the morning, verified time with running buddy"),

# Submission logic
if st.button("Submit", key="submit_context_information", type="primary"):
    # Count how many fields (excluding day/time) are non-empty and not the default placeholder
    if st.session_state["day_text_scenario_5"] == "______":
        st.warning("Please generate a day and time before submitting.")
    else:
        exclusion_fields = ["pa_scheduled_today_yes_scenario_5", "pa_planning_specifity_scheduled_today_scenario_5", "pa_performed_today_yes_scenario_5",
                            "pa_scheduled_tomorrow_yes_scenario_5", "pa_planning_specifity_scheduled_tomorrow_scenario_5"]
        # Count filled fields
        filled_count = 0
        for field, *_ in INPUT_FIELDS:
            if field in exclusion_fields:
                pass
            val = st.session_state.get(field)
            if val not in (None, "", "______"):
                filled_count += 1
        # Require at least 20 fields filled (as per original logic)
        if filled_count >= 18:
            st.success("The data was successfully submitted!")
            st.warning("The generation of messages may take up to 3 minutes! Thank you for your understanding.")
            # Save current day/time to used list
            combo = (st.session_state["day_text_scenario_5"], st.session_state["time_text_scenario_5"])
            used = st.session_state.get("used_day_time_combinations", [])
            if combo not in used:
                used.append(combo)
                st.session_state["used_day_time_combinations"] = used
            # Prepare data for LLM
            # NOTE: adjust keys like bfi_1 etc. as needed
            data_dict = [{
                "reserved": st.session_state.bfi_1,
                "generally trusting": st.session_state.bfi_2,
                "tends to be lazy": st.session_state.bfi_3,
                "relaxed, handles stress well": st.session_state.bfi_4,
                "few artistic interests": st.session_state.bfi_5,
                "outgoing, sociable": st.session_state.bfi_6,
                "tends to find fault with others": st.session_state.bfi_7,
                "does a thorough job": st.session_state.bfi_8,
                "gets nervous easily": st.session_state.bfi_9,
                "has an active imagination": st.session_state.bfi_10,
                "considerate and kind to almost everyone": st.session_state.bfi_11,
                "extraversion": st.session_state.extraversion,
                "agreeableness": st.session_state.agreeableness,
                "conscientiousness": st.session_state.conscientiousness,
                "neuroticism": st.session_state.neuroticism,
                "openness": st.session_state.openness,
                "age": st.session_state.age_option,
                "gender": st.session_state.gender_option,
                "job situation": st.session_state.job_situation,

                "day": st.session_state.day_text_scenario_5,
                "time": st.session_state.time_text_scenario_5,
                "next_day_text": st.session_state.next_day_text_scenario_5,
                "user status": st.session_state.user_status_scenario_5,
                "weather": st.session_state.weather_scenario_5,
                "activity": st.session_state.activity_scenario_5,
                "location": st.session_state.location_scenario_5,
                "position of body": st.session_state.position_of_body_scenario_5,
                "last interaction": st.session_state.last_interaction_scenario_5,
                "mood_valence": st.session_state.mood_valence_scenario_5,
                "energetic_arousal": st.session_state.energetic_arousal_scenario_5,
                "affect_calmness": st.session_state.affect_calmness_scenario_5,
                "stress": st.session_state.stress_scenario_5,
                "locus_of_control": st.session_state.locus_of_control_scenario_5,
                "close_locations": st.session_state.close_locations_scenario_5,
                "calendar entries": st.session_state.calendar_entries_scenario_5,
                "motivation_pa": st.session_state.motivation_pa_scenario_5,
                "barrier_pa": st.session_state.barrier_pa_scenario_5,
                "pa_scheduled_today": st.session_state.pa_scheduled_today_scenario_5,
                "pa_scheduled_today_yes": st.session_state.pa_scheduled_today_yes_scenario_5,
                "pa_planning_specifity_scheduled_today": st.session_state.pa_planning_specifity_scheduled_today_scenario_5,
                "pa_performed_today": st.session_state.pa_performed_today_scenario_5,
                "pa_performed_today_yes": st.session_state.pa_performed_today_yes_scenario_5,
                "pa_scheduled_tomorrow": st.session_state.pa_scheduled_tomorrow_scenario_5,
                "pa_scheduled_tomorrow_yes": st.session_state.pa_scheduled_tomorrow_yes_scenario_5,
                "pa_planning_specifity_scheduled_tomorrow": st.session_state.pa_planning_specifity_scheduled_tomorrow_scenario_5,

                "mood": st.session_state.mood_valence_scenario_5,
                "calender_entries": st.session_state.calendar_entries_scenario_5,
                "jitai_sent_today": None,
                "sleep quality": None,
                "self_efficacy": st.session_state.locus_of_control_scenario_5,
                     }]

            # Generate JITAI via LLM_functions
            original_jitai_list, jitai_list, example_list = LLM_functions.generate_jitais(data_dict)
            for i, text in enumerate(original_jitai_list, start=1):
                st.session_state[f"scenario_5_original_jitai_{i}_text"] = text
            for i, text in enumerate(jitai_list, start=1):
                st.session_state[f"scenario_5_jitai_{i}_text"] = text
            for i, text in enumerate(example_list, start=1):
                st.session_state[f"scenario_5_jitai_{i}_example"] = text
            # Further implementation: record origins, exclude day/time combination, etc.
            st.session_state["scenario_5_text"] = (
                f"Last {day_text_scenario_5}, between {time_text_scenario_5}, I was {user_status_scenario_5}, and the weather was {weather_scenario_5}. "
                f"During this period, I was mainly engaging in {activity_scenario_5} at {location_scenario_5}, spending a significant amount of time {position_of_body_scenario_5}. My last interaction with my phone was {last_interaction_scenario_5} ago. "
                f"During this time, I was feeling {mood_valence_scenario_5}% well, {energetic_arousal_scenario_5}% energetic, {affect_calmness_scenario_5}% calm, {stress_scenario_5}% stressed, and {locus_of_control_scenario_5}% in control of what was happening. "
                f"Nearby locations accessible during this timeframe included: {close_locations_scenario_5}. "
                f"Later that day, I had planned the following: {calendar_entries_scenario_5}. "
                f"Independent of my circumstances, I was {motivation_pa_scenario_5}% motivated to engage in physical activity during this time. My circumstances were {barrier_pa_scenario_5}% favourable of physical activity. "
                f"I {pa_scheduled_today_scenario_5} intended a physical activity for that day{pa_scheduled_today_yes_scenario_5}{pa_planning_specifity_scheduled_today_scenario_5}. "
                f"I {pa_performed_today_scenario_5} complete some physical activity that day{pa_performed_today_yes_scenario_5}. "
                f"For the following day - {next_day_text_scenario_5} - I {pa_scheduled_tomorrow_scenario_5} intended to be physically active{pa_scheduled_tomorrow_yes_scenario_5}{pa_planning_specifity_scheduled_tomorrow_scenario_5}."
)
            st.session_state.expander_bool_scenario_5 = True
        else:
            st.warning("All the contextual factors must be filled out!")

# ---------- JITAI EVALUATION ----------

with st.expander(label="Next Task", expanded=st.session_state.expander_bool_scenario_5):
    st.subheader(
        "Please have a look at every tab - JITAI 1 to JITAI 8 - and evaluate the unique JITAI messages as if you would currently be in the situation that you described above!"
        " The system may decide that no JITAI should be sent, indicated via 'For this context no JITAI would be sent!'"
    )
    st.warning(
        "The program may automatically jump to the bottom of the page once per scenario because of an internal error. Thank you for your understanding regarding any inconvenience this may cause.")
    tab_labels = [f"JITAI {i}" for i in range(1, 9)]
    tabs = st.tabs(tab_labels)

    # Pair each tab with its corresponding randomized index
    for i, tab in zip(st.session_state.random_order_scenario_5, tabs):
        with tab:
            jitai_key = f"scenario_5_jitai_{i}_text"
            st.write(st.session_state.get(jitai_key, f"[No text found for {jitai_key}]"))

            # Base metrics
            with st.container(border=True):
                st.write("What do you think...")
                for metric_key, metric_text in BASE_METRICS:
                    label_vis = "visible" if metric_key == "appropriateness_sent" else "collapsed"
                    full_key = f"scenario_5_jitai_{i}_{metric_key}"
                    st.session_state[full_key] = assertion_values(
                        text=metric_text,
                        key_variable=full_key,
                        label_visibility=label_vis
                    )

            # Advanced metrics
            with st.container(border=True):
                for metric_key, metric_text in EMOTIONAL_RESPONSIVENESS_METRICS:
                    label_vis = "visible" if metric_key == "e1" else "collapsed"
                    full_key = f"scenario_5_jitai_{i}_{metric_key}"
                    st.session_state[full_key] = assertion_values_emotional_responsiveness(
                        text=metric_text,
                        field=full_key,
                        label_visibility=label_vis,
                    )

            with st.container(border=True):
                st.write("After receiving this message under the given circumstances, I would feel ..")
                for idx, metric in enumerate(EMOTION_METRICS):
                    label_vis = "visible" if metric == "angry" else "collapsed"
                    full_key = f"scenario_5_jitai_{i}_{metric}"
                    st.session_state[full_key] = assertion_values(
                        text=metric.capitalize(),
                        key_variable=full_key,
                        label_visibility=label_vis
                    )

            # Advanced metrics
            with st.container(border=True):
                for metric_key, metric_text in PERSONALIZATION_METRICS:
                    label_vis = "visible" if metric_key == "p1" else "collapsed"
                    full_key = f"scenario_5_jitai_{i}_{metric_key}"
                    st.session_state[full_key] = assertion_values_personalization(
                        text=metric_text,
                        key_variable=full_key,
                        label_visibility=label_vis
                    )



    all_filled = True
    for i in range(1, 9):
        for metric_key, metric_text in BASE_METRICS:
            key = f"scenario_5_jitai_{i}_{metric_key}"
            if st.session_state.get(key) is None:
                all_filled = False
                break

        for metric in EMOTION_METRICS:
            key = f"scenario_5_jitai_{i}_{metric}"
            if st.session_state.get(key) is None:
                all_filled = False
                break

        for metric_key, metric_text in PERSONALIZATION_METRICS:
            key = f"scenario_5_jitai_{i}_{metric_key}"
            if st.session_state.get(key) is None:
                all_filled = False
                break

        for metric_key, metric_text in EMOTIONAL_RESPONSIVENESS_METRICS:
            key = f"scenario_5_jitai_{i}_{metric_key}"
            if st.session_state.get(key) is None:
                all_filled = False
                break
        if not all_filled:
            break

    if not all_filled:
        st.warning("Not all questions have been filled out. Please do so before continuing to the next task!")
    # If sorting tasks are re-enabled, similar refactor can apply.

# ---------- NAVIGATION ----------

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/scenario_4.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    if all_filled:
        st.page_link("pages/post_study_questions.py", label="Next Page", icon=":material/arrow_forward:")
    #st.page_link("pages/post_study_questions.py", label="Next Page", icon=":material/arrow_forward:")
    agree = st.checkbox(
        "If all questions are answered and you still can't see the 'Next Page' button, let us know here. Misusing this to skip questions will result in your submission being rejected.")
    if agree:
        st.page_link("pages/post_study_questions.py", label="Next Page", icon=":material/arrow_forward:")