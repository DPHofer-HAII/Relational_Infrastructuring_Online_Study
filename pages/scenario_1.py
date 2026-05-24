import streamlit as st
import random
import LLM_functions

print("Hey guuurl!")

st.set_page_config(layout="wide")

if "day_text" not in st.session_state:
    st.session_state["day_text"] = "______"
if "time_text" not in st.session_state:
    st.session_state["time_text"] = "______"

if "user_status" not in st.session_state:
    st.session_state["user_status"] = None
if "location" not in st.session_state:
    st.session_state["location"] = None
if "weather" not in st.session_state:
    st.session_state["weather"] = None
if "activity" not in st.session_state:
    st.session_state["activity"] = None
if "position_of_body" not in st.session_state:
    st.session_state["position_of_body"] = None
if "mood" not in st.session_state:
    st.session_state["mood"] = None
if "stress" not in st.session_state:
    st.session_state["stress"] = None
if "handling" not in st.session_state:
    st.session_state["handling"] = None
if "LoC" not in st.session_state:
    st.session_state["LoC"] = None
if "sleep_quality" not in st.session_state:
    st.session_state["sleep_quality"] = None
if "sleep_mood" not in st.session_state:
    st.session_state["sleep_mood"] = None
if "last_interaction" not in st.session_state:
    st.session_state["last_interaction"] = None
if "calendar_entries" not in st.session_state:
    st.session_state["calendar_entries"] = None
if "close_locations" not in st.session_state:
    st.session_state["close_locations"] = None
if "locus_of_control" not in st.session_state:
    st.session_state["locus_of_control"] = None
if "motivation_pa" not in st.session_state:
    st.session_state["motivation_pa"] = None
if "barrier_pa" not in st.session_state:
    st.session_state["barrier_pa"] = None
if "pa_scheduled_today" not in st.session_state:
    st.session_state["pa_scheduled_today"] = None
if "jitai_sent_today" not in st.session_state:
    st.session_state["jitai_sent_today"] = None
if "pa_performed_today" not in st.session_state:
    st.session_state["pa_performed_today"] = None
if "pa_scheduled_tomorrow" not in st.session_state:
    st.session_state["pa_scheduled_tomorrow"] = None
if "pa_planning_specifity" not in st.session_state:
    st.session_state["pa_planning_specifity"] = None


parameters = [
    "appropriate", "engaging", "effective", "professional", "natural", "empathetic", "understanding", "tone", "regularly",
    "angry", "annoyed", "frustrated", "happy", "sad", "scared", "surprised", "tailored", "respected", "feeling", "context",
    "trust", "reliable", "follow", "continue", "reflect", "personality"
]

for i in range(1, 9):
    for param in parameters:
        key = f"scenario_1_jitai_{i}_{param}"
        index_key = f"{key}_index"

        if key not in st.session_state:
            st.session_state[key] = None
        if index_key not in st.session_state:
            st.session_state[index_key] = None

for i in range(1, 9):
    key = f"jitai_{i}_text"
    index_key = f"{key}_index"

    if key not in st.session_state:
        st.session_state[key] = "None"
    if index_key not in st.session_state:
        st.session_state[index_key] = "None"

st.header('Scenario 1')
st.subheader("You will now be asked to fill out a text with contextual information that describes one of your days at"
             " a given timeframe from last week. Please try to recall one event you experienced during the specified "
             "time. If time and day don't fit your schedule, e.g. usual 'night rest', please click the button "
             "'Regenerate Day & Time' for a new combination.")

day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_list = ["07:00 - 09:00", "09:00 - 11:00", "11:00 - 13:00", "13:00 - 15:00", "15:00 - 17:00",
             "17:00 - 19:00", "19:00 - 21:00"]

day_text = st.session_state["day_text"]
time_text = st.session_state["time_text"]

def regenerate_time_and_day():
    st.session_state.day_text = random.choice(day_list)
    st.session_state.time_text = random.choice(time_list)

with st.container(border=True):

    st.text("Day: " + day_text)
    st.text("Time: " + time_text)

    st.button("Regenerate Day & Time", key="Day&TimeGenerator", type="primary", on_click=regenerate_time_and_day)

def set_new_index_user_status():
    st.session_state.user_status = st.session_state.key_user_status
if st.session_state.user_status is None:
    user_status = "______"
else:
    user_status = st.session_state.user_status

def set_new_index_location():
    st.session_state.location = st.session_state.key_location
if st.session_state.location is None:
    location = "______"
else:
    location = st.session_state["location"]

def set_new_index_weather():
    st.session_state.weather = st.session_state.key_weather
if st.session_state.weather is None:
    weather = "______"
else:
    weather = st.session_state["weather"]

def set_new_index_activity():
    st.session_state.activity = st.session_state.key_activity
if st.session_state.activity is None:
    activity = "______"
else:
    activity = st.session_state["activity"]

def set_new_index_position_of_body():
    st.session_state.position_of_body = st.session_state.key_position_of_body
if st.session_state.position_of_body is None:
    position_of_body = "______"
else:
    position_of_body = st.session_state["position_of_body"]

def set_new_index_mood():
    st.session_state.mood = st.session_state.key_mood

if st.session_state.mood is None:
    mood = "______"
else:
    mood = st.session_state["mood"]

def set_new_index_stress():
    st.session_state.stress = st.session_state.key_stress
if st.session_state.stress is None:
    stress = "_____"
else:
    stress = st.session_state["stress"]

def set_new_index_handling():
    st.session_state.handling = st.session_state.key_handling
if st.session_state.handling is None:
    handling = "______"
else:
    handling = st.session_state["handling"]

def set_new_index_LoC():
    st.session_state.LoC = st.session_state.key_LoC
if st.session_state.LoC is None:
    LoC = "______"
else:
    LoC = st.session_state["LoC"]

def set_new_index_last_interaction():
    st.session_state.last_interaction = st.session_state.key_last_interaction
if st.session_state.last_interaction is None:
    last_interaction = "______"
else:
    last_interaction = st.session_state["last_interaction"]

def set_new_index_sleep_quality():
    st.session_state.sleep_quality = st.session_state.key_sleep_quality
if st.session_state.sleep_quality is None:
    sleep_quality = "______"
else:
    sleep_quality = st.session_state["sleep_quality"]

def set_new_index_sleep_mood():
    st.session_state.sleep_mood = st.session_state.key_sleep_mood
if st.session_state.sleep_mood is None:
    sleep_mood = "______"
else:
    sleep_mood = st.session_state["sleep_mood"]

def set_new_index_calendar_entries():
    st.session_state.calendar_entries = st.session_state.key_calendar_entries
if st.session_state.calendar_entries is None:
    calendar_entries = "______"
else:
    calendar_entries = st.session_state["calendar_entries"]

def set_new_index_close_locations():
    st.session_state.close_locations = st.session_state.key_close_locations
if st.session_state.close_locations is None:
    close_locations = "______"
else:
    close_locations = st.session_state["close_locations"]
def set_new_index_locus_of_control():
    st.session_state.locus_of_control = st.session_state.key_locus_of_control
if st.session_state.locus_of_control is None:
    locus_of_control = "______"
else:
    locus_of_control = st.session_state["locus_of_control"]
def set_new_index_motivation_pa():
    st.session_state.motivation_pa = st.session_state.key_motivation_pa
if st.session_state.motivation_pa is None:
    motivation_pa = "______"
else:
    motivation_pa = st.session_state["motivation_pa"]
def set_new_index_barrier_pa():
    st.session_state.barrier_pa = st.session_state.key_barrier_pa
if st.session_state.barrier_pa is None:
    barrier_pa = "______"
else:
    barrier_pa = st.session_state["barrier_pa"]
def set_new_index_pa_scheduled_today():
    st.session_state.pa_scheduled_today = st.session_state.key_pa_scheduled_today
if st.session_state.pa_scheduled_today is None:
    pa_scheduled_today = "______"
else:
    pa_scheduled_today = st.session_state["pa_scheduled_today"]
def set_new_index_jitai_sent_today():
    st.session_state.jitai_sent_today = st.session_state.key_jitai_sent_today
if st.session_state.jitai_sent_today is None:
    jitai_sent_today = "______"
else:
    jitai_sent_today = st.session_state["jitai_sent_today"]
def set_new_index_pa_performed_today():
    st.session_state.pa_performed_today = st.session_state.key_pa_performed_today
if st.session_state.pa_performed_today is None:
    pa_performed_today = "______"
else:
    pa_performed_today = st.session_state["pa_performed_today"]
def set_new_index_pa_scheduled_tomorrow():
    st.session_state.pa_scheduled_tomorrow = st.session_state.key_pa_scheduled_tomorrow
if st.session_state.pa_scheduled_tomorrow is None:
    pa_scheduled_tomorrow = "______"
else:
    pa_scheduled_tomorrow = st.session_state["pa_scheduled_tomorrow"]
def set_new_index_pa_planning_specifity():
    st.session_state.pa_planning_specifity = st.session_state.key_pa_planning_specifity
if st.session_state.pa_planning_specifity is None:
    pa_planning_specifity = "______"
else:
    pa_planning_specifity = st.session_state["pa_planning_specifity"]


# Placeholder
sorted_items_concluded = False

with ((st.container(border=True))):
    st.subheader("Please fill in as many blanks as possible, by using the insert fields below. If you don't remember"
                 " all the details of the situation, try to guess what would most likely have been the case. "
                 "Up to three fields can be left blank. Once you are done filling in, please click the 'Submit'-button below.")

    # st.write("On " + day_text + " from " + time_text + ", I was "
    #          + user_status + " (user status - e.g. sick, on vacation, at work)"
    #          + ", which influenced my overall day. I was at " + location
    #          + " (location - e.g. the office/work, supermarket, home)" + " with " + weather
    #          + " (weather - e.g. sunny, cloudy, rainy)"
    #          + ". I was mainly " + activity + "(activity - e.g. working, sleeping, gardening)" + " while "
    #          + position_of_body + "(positon of body - e.g. sitting, walking, lying down)" + ". My mood was "
    #          + mood + "(mood - e.g. happy, angry, sad)" + ", "
    #          + "and my stress level was around " + stress + "(stress - e.g. 1 (no stress) to 100 (very stressed))"
    #          + ", which I handled " + handling + " (handling - e.g. well, poorly, mediocre). During this time, I felt "
    #          + LoC + "(Locus of Control - e.g. confident, unsure, capable, ineffective)" + "in mangaging tasks, affecting "
    #          "my sense of self-efficacy. Reflecting on last night's sleep, I'd rate it as " + sleep_quality
    #          + "(sleep quality - e.g. poor, average, good, excellent)" + ", and this made me feel "
    #          + sleep_mood + "(mood - e.g. tired, refreshed, normal)" + " upon waking."
    #          + "My last interaction with my phone is " + last_interaction + " ago.")

    st.write(
        f"On {day_text} from {time_text}, I was {user_status}. "
        f"My calendar entries for that day were the following: {calendar_entries}. "
        f"I was located at {location} while the weather was {weather}. "
        f"Nearby places included {close_locations}. "
        f"During the period, I was mainly {activity} while {position_of_body}. "
        f"My mood was {mood}, and my stress level was around {stress}, "
        f"which I managed {handling}. My sense of control over tasks was {locus_of_control}, affecting my self-efficacy assessment. "
        f"Reflecting on last night’s sleep, I’d rate it as {sleep_quality}, leaving me feeling {sleep_mood} upon waking. "
        f"My motivation for physical activity for that period was: {motivation_pa}. I would rate the identified barriers for physical activity at that time as: {barrier_pa}. "
        f"I planned the following physical activities for today: {pa_scheduled_today}. A JITAI notification {jitai_sent_today} sent today. "
        f"Based on motivation and barriers, I performed the following physical activities: {pa_performed_today}. My last interaction with my phone during that time was {last_interaction} ago. "
        f"Looking ahead, I have the following physical activities scheduled: {pa_scheduled_tomorrow}; which I noted down to a specifity degree of: {pa_planning_specifity}."
    )

    st.write(r'''$\textsf{\large !!! The insert fields can be found here - only up to three may be left empty !!!}$''')
    col1, col2, col3 = st.columns([1, 1, 1], gap="small", vertical_alignment="top")
    with col1:
        user_status = st.text_input(label="User Status", max_chars=32, key="key_user_status", value=st.session_state.user_status,
                   placeholder="e.g. sick, on vacation, at work", label_visibility="visible", on_change=set_new_index_user_status)
        weather = st.text_input(label="Weather", max_chars=32, key="key_weather", value=st.session_state.weather,
                                placeholder="e.g. sunny, cloudy, rainy", on_change=set_new_index_weather)
        position_of_body = st.text_input(label="Position of Body", max_chars=32, key="key_position_of_body",
                                         value=st.session_state.position_of_body,
                                         placeholder="e.g. sitting, walking, lying down",
                                         on_change=set_new_index_position_of_body)
        handling = st.text_input(label="Handling situation", max_chars=32, key="key_handling", value=st.session_state.handling,
                                 placeholder="e.g. well, poorly, mediocre", on_change=set_new_index_handling)
        sleep_mood = st.text_input(label="Mood after waking up", max_chars=32, key="key_sleep_mood",
                                   value=st.session_state.sleep_mood,
                                   placeholder="e.g. tired, refreshed, normal", on_change=set_new_index_sleep_mood)
        pa_scheduled_today = st.text_input(label="Physical Activity scheduled today", max_chars=32, key="key_pa_scheduled_today",
                                   value=st.session_state.pa_scheduled_today,
                                   placeholder="e.g., 30-minute walk at 18:00; none scheduled", on_change=set_new_index_pa_scheduled_today)
        last_interaction = st.text_input(label="Phone Interaction", max_chars=32, key="key_last_interaction",
                                         value=st.session_state.last_interaction,
                                         placeholder="e.g. 12 minutes, 1 hour", on_change=set_new_index_last_interaction)




    with col2:
        calendar_entries = st.text_input(label="Calendar Entries", max_chars=32, key="key_calendar_entries", value=st.session_state.calendar_entries,
                                 placeholder="e.g., '14:00–15:00: team meeting; 16:30–17:00: doctor’s appointment reminder'; or 'none'",
                                 on_change=set_new_index_calendar_entries)
        close_locations = st.text_input(label="Close Locations", max_chars=32, key="key_close_locations",
                                         value=st.session_state.close_locations,
                                         placeholder="e.g., gym two blocks away; park within walking distance; café nearby; none",
                                         on_change=set_new_index_close_locations)
        mood = st.text_input(label="Mood", max_chars=32, key="key_mood", value=st.session_state.mood,
                             placeholder="0 = very bad to 100 = very good", on_change=set_new_index_mood)
        locus_of_control = st.text_input(label="Locus of Control - how much did you feel in control in the situation", max_chars=32, key="key_locus_of_control", value=st.session_state.locus_of_control,
                             placeholder="0 = very bad to 100 = very good", on_change=set_new_index_locus_of_control)
        motivation_pa = st.text_input(label="Motivation for Physical Activity", max_chars=32, key="key_motivation_pa",
                                         value=st.session_state.motivation_pa,
                                         placeholder="0 = very low to 100 = very high",
                                         on_change=set_new_index_motivation_pa)
        jitai_sent_today = st.text_input(label="(JITAI) Notification sent today", max_chars=32, key="key_jitai_sent_today",
                                      value=st.session_state.jitai_sent_today,
                                      placeholder="was / was not",
                                      on_change=set_new_index_jitai_sent_today)
        pa_scheduled_tomorrow = st.text_input(label="Physical Activity Scheduled Tomorrow", max_chars=32,
                                         key="key_pa_scheduled_tomorrow",
                                         value=st.session_state.pa_scheduled_tomorrow,
                                         placeholder="e.g., 'Reminder: take a short walk at 16:00'; none sent",
                                         on_change=set_new_index_pa_scheduled_tomorrow)



    with col3:
        location = st.text_input(label="Location", max_chars=32, key="key_location", value=st.session_state.location,
                                 placeholder="e.g. the office/work, supermarket, home",
                                 on_change=set_new_index_location)
        activity = st.text_input(label="Activity", max_chars=32, key="key_activity", value=st.session_state.activity,
                                 placeholder="e.g. working, sleeping, gardening", on_change=set_new_index_activity)
        stress = st.text_input(label="Stress", max_chars=32, key="key_stress", value=st.session_state.stress,
                               placeholder="0 = no stress to 100 (very stressed)", on_change=set_new_index_stress)
        sleep_quality = st.text_input(label="Sleep Quality", max_chars=32, key="key_sleep_quality",
                                      value=st.session_state.sleep_quality,
                                      placeholder="0 = very bad to 100 = very good",
                                      on_change=set_new_index_sleep_quality)
        barrier_pa = st.text_input(label="Barriers for Physical Activity", max_chars=32, key="key_barrier_pa",
                                      value=st.session_state.barrier_pa,
                                      placeholder="0 = very low to 100 = very high",
                                      on_change=set_new_index_barrier_pa)
        pa_performed_today = st.text_input(label="Physical activity performed today", max_chars=32, key="key_pa_performed_today",
                                   value=st.session_state.pa_performed_today,
                                   placeholder="e.g., performed a 10-minute walk at 17:00; did not perform any activity",
                                   on_change=set_new_index_pa_performed_today)
        pa_planning_specifity = st.text_input(label="Planning specifity of upcoming Physical Activity", max_chars=32,
                                           key="key_pa_planning_specifity",
                                           value=st.session_state.pa_planning_specifity,
                                           placeholder="0 = very low to 100 = very high",
                                           on_change=set_new_index_pa_planning_specifity)

        # LoC = st.text_input(label="Locus of Control", max_chars=32, key="key_LoC", value=st.session_state.LoC,
        #                         placeholder="e.g. confident, unsure, capable, ineffective", on_change=set_new_index_LoC)


    placeholder_list = [day_text, time_text, user_status, activity, stress, sleep_quality, location, position_of_body,
                        handling, sleep_mood, weather, mood, LoC, last_interaction]

    # if jitai_1_text == "":
    #     dummy_data = "None"
    #     jitai_dummy_list = LLM_functions.generate_dummy_jitais()
    #
    #     jitai_1_text = jitai_dummy_list[0]
    #     jitai_2_text = jitai_dummy_list[1]
    #     jitai_3_text = jitai_dummy_list[2]
    #     jitai_4_text = jitai_dummy_list[3]
    #     jitai_5_text = jitai_dummy_list[4]
    #     jitai_6_text = jitai_dummy_list[5]
    #     jitai_7_text = jitai_dummy_list[6]
    #     jitai_8_text = jitai_dummy_list[7]

    if st.button("Submit", key="submit_context_information", type="primary"):
        # check if 9 or more fields had been filled out
        filled_out_counter = 0

        if placeholder_list[0] == "______":
            st.warning("Please generate a random day and timeperiod!")
            pass

        else:
            for value in placeholder_list:
                if value != None and value != "______":
                    filled_out_counter += 1

            if filled_out_counter >= 8 and placeholder_list[0] != "______":
                # if enough necessary data was ingested: send a "okay" message & start the LLM creation
                st.success("The data was successfully submitted!")
                st.warning("The generation of messages may take up to 3 minutes! Thank you for your understanding.")
                # Start the LLM process here!
                data = [{"reserved": st.session_state.bfi_1,
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
                         "day": st.session_state.day_text,
                         "time": st.session_state.time_text,
                         "user status": st.session_state.user_status,
                         "location": st.session_state.location,
                         "weather": st.session_state.weather,
                         "activity": st.session_state.activity,
                         "position of body": st.session_state.position_of_body,
                         "mood": st.session_state.mood,
                         "stress": st.session_state.stress,
                         "self_efficacy": st.session_state.handling,
                         "locus of control": st.session_state.LoC,
                         "sleep quality": st.session_state.sleep_quality,
                         "mood after waking up": st.session_state.sleep_mood,
                         "job situation": st.session_state.job_situation,
                         "age": st.session_state.age_option,
                         "gender": st.session_state.gender_option,
                         "last interaction": st.session_state.last_interaction,
                         "calender_entries": st.session_state.calendar_entries,
                         "close_locations": st.session_state.close_locations,
                         "motivation_pa": st.session_state.motivation_pa,
                         "barrier_pa": st.session_state.barrier_pa,
                         "pa_scheduled_today": st.session_state.pa_scheduled_today,
                         "pa_performed_today": st.session_state.pa_performed_today,
                         "jitai_sent_today": st.session_state.jitai_sent_today,
                         "pa_scheduled_tomorrow": st.session_state.pa_scheduled_tomorrow,
                         }]
                with open("intermediate_data.csv", "w", newline="") as csvfile:
                    fieldnames = ["reserved", "generally trusting", "tends to be lazy", "relaxed, handles stress well",
                                  "few artistic interests", "outgoing, sociable", "tends to find fault with others",
                                  "does a thorough job", "gets nervous easily", "has an active imagination",
                                  "considerate and kind to almost everyone", "day", "time", "user status",
                                  "location", "weather", "activity", "position of body", "mood", "stress", "self_efficacy",
                                  "locus of control", "sleep quality", "mood after waking up", "job situation", "age",
                                  "gender", "last interaction", "calender_entries", "close_locations", "motivation_pa",
                                  "barrier_pa", "pa_scheduled_today", "pa_performed_today", "jitai_sent_today",
                                  "pa_scheduled_tomorrow",]
                    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    # writer.writeheader()
                    # writer.writerows(data)

                original_jitai_list, jitai_list = LLM_functions.generate_jitais(data)
                # Save the JITAIs according to their origin -> so we know which model generated which JITAI
                # NEEDS IMPLEMENTATION!!!

                st.session_state.jitai_1_text = jitai_list[0]
                st.session_state.jitai_2_text = jitai_list[1]
                st.session_state.jitai_3_text = jitai_list[2]
                st.session_state.jitai_4_text = jitai_list[3]
                st.session_state.jitai_5_text = jitai_list[4]
                st.session_state.jitai_6_text = jitai_list[5]
                st.session_state.jitai_7_text = jitai_list[6]
                st.session_state.jitai_8_text = jitai_list[7]


                # Once the button was clicked, exclude the day & time combination from the realm of possibilities!!!
                # NEEDS IMPLEMENTATION!!!

            else:
                # if not: send a warning message
                st.warning("At least 9 blanks (excluding day and time) must be filled in to continue!")

# ---------- COMPONENT FUNCTIONS ----------
def assertion_values(text, key_variable, label_visibility):
    if st.session_state.get(key_variable) is None:
        index_variable = None
    else:
        index_variable = int(st.session_state[key_variable]) - 1

    def set_new_index_value():
        st.session_state[key_variable] = st.session_state["key_" + key_variable]

    col1, col2 = st.columns([0.3, 0.7], vertical_alignment="bottom")
    with col1:
        st.write(text)
    with col2:
        value = st.radio(
            label="1 = Strongly disagree --------------------------------------------- 7 = Strongly agree",
            options=["1", "2", "3", "4", "5", "6", "7"],
            index=index_variable,
            key="key_" + key_variable,
            label_visibility=label_visibility,
            horizontal=True,
            on_change=set_new_index_value
        )
    return value

# ---------- CONFIGURATION ----------
base_metrics = [
    "appropriate", "engaging", "effective", "professional", "angry", "annoyed",
    "frustrated", "happy", "sad", "scared", "surprised"
]

advanced_metrics = [
    ("tailored", "To what extent did the message feel tailored to your style and preferences?"),
    ("natural", "How natural or human-like does the message seem?"),
    ("empathetic", "How empathetic does the message seem?"),
    ("understanding", "To what extent did the message demonstrate understanding of your feelings and/or situation?"),
    ("tone", "How appropriate is the emotional tone of the message?"),
    ("regulatory", "I would be comfortable receiving this kind of message regularly."),
    ("respected", "The message respected my individuality and personal tone."),
    ("feeling", "The message was relevant to how I was feeling or what I was doing that day."),
    ("context", "The message felt personally tailored to my current context."),
    ("trusted", "I trust the intentions behind this message."),
    ("reliable", "The message felt like it came from a reliable, emotionally aware system."),
    ("follow", "I would follow the suggestion or advice given in the message."),
    ("continue", "I would be likely to continue interacting with this specific AI in the future."),
    ("reflect", "This message increased my motivation to change or reflect on my behaviour."),
    ("personality", "The message felt consistent with my personality traits (e.g., extraversion, openness)."),
]

# ---------- MAIN UI ----------
st.warning("PLEASE ONLY CONTINUE IF YOU SUCCESSFULLY SUBMITTED THE DATA!")

with st.container(border=True):
    st.subheader("Please have a look at every tab - JITAI 1 to JITAI 8 - and evaluate the unique JITAI message according to the stated metrics. "
                 "The system may decide that no JITAI should be sent, indicated via e.g. 'I am sorry, I cannot assist with that', 'None', '... does not contain a personalized message...', etc.")
    tabs = st.tabs([f"JITAI {i}" for i in range(1, 9)])

    for i, tab in enumerate(tabs, start=1):
        with tab:
            jitai_key = f"jitai_{i}_text"
            scenario_prefix = f"scenario_1_jitai_{i}_"
            st.write(st.session_state.get(jitai_key, f"[No text found for {jitai_key}]"))

            with st.container(border=True):
                for idx, metric in enumerate(base_metrics):
                    label_visibility = "visible" if metric == "appropriate" else "collapsed"
                    st.session_state[scenario_prefix + metric] = assertion_values(
                        text=metric.capitalize(),
                        key_variable=scenario_prefix + metric,
                        label_visibility=label_visibility
                    )

            with st.container(border=True):
                for metric_key, metric_text in advanced_metrics:
                    label_visibility = "visible" if metric_key == "tailored" else "collapsed"
                    st.session_state[scenario_prefix + metric_key] = assertion_values(
                        text=metric_text,
                        key_variable=scenario_prefix + metric_key,
                        label_visibility=label_visibility
                    )

# Checking if all the assertion values have been filled out by the participants
#MUST BE ADAPTED FOR EVERY SCENARIO!!!
assertion_value_list = ["appropriate", "engaging", "effective", "professional", "angry", "annoyed", "frustrated", "happy", "sad", "scared", "surprised"]
jitai_assertion = False
jitai_assertion_count=0
for i in range(1, 7):
    for assertion_value_text in assertion_value_list:
        if st.session_state["scenario_1_jitai_"+str(i)+"_"+assertion_value_text] is not None:
            jitai_assertion_count += 1
if jitai_assertion_count == 66:
    jitai_assertion = True

# Telling participant that not all assertion values have been filled out
if jitai_assertion == False:
    st.warning("Not all metrics have been filled out. Please do so before continuing to the next task!")

# Add the sorting task here
# with st.container(border=True):
#     st.subheader("Please rank the JITAIs according to your liking based on how motivational you perceived them by dragging "
#                  "them to the field 'Sorted According to Preference'. The most motivational should be at the top (left) "
#                  "and the least motivational at the bottom (right). "
#                  "Please use all JITAIs.")
#     if "original_items" not in st.session_state:
#         st.session_state["original_items"] = [
#             {"header": "Messages",
#              "items": [st.session_state.jitai_1_text, st.session_state.jitai_2_text, st.session_state.jitai_3_text,
#                        st.session_state.jitai_4_text, st.session_state.jitai_5_text, st.session_state.jitai_6_text,
#                        st.session_state.jitai_7_text, st.session_state.jitai_8_text]},
#             {"header": "Sorted According to Preference", "items": []}
#         ]
#
#     st.session_state.original_items = sort_items(st.session_state.original_items, multi_containers=True, key="sortable_scenario_1")
#     if len(st.session_state.original_items[1]["items"]) < 8:
#         st.warning("Please make sure to sort all 8 messages according to your preferences.")
#     else:
#         sorted_items_concluded = True
#         st.info("Your sorted preferences are saved and will persist.")

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/start_main_part.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    #if len(sorted_items[1]["items"]) == 8 and jitai_assertion == True:
    #if sorted_items_concluded == True and jitai_assertion == True:
    st.page_link("pages/post_study_questions.py", label="Next Page", icon=":material/arrow_forward:")
    #st.page_link("pages/scenario_2.py", label="Next Page", icon=":material/arrow_forward:")