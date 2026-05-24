import streamlit as st

if 'ipaq_1' not in st.session_state:
    st.session_state['ipaq_1'] = None
if 'ipaq_2' not in st.session_state:
    st.session_state['ipaq_2'] = None
if 'ipaq_3' not in st.session_state:
    st.session_state['ipaq_3'] = None
if 'ipaq_4' not in st.session_state:
    st.session_state['ipaq_4'] = None
if 'ipaq_5' not in st.session_state:
    st.session_state['ipaq_5'] = None
if 'ipaq_6' not in st.session_state:
    st.session_state['ipaq_6'] = None
if 'ipaq_7' not in st.session_state:
    st.session_state['ipaq_7'] = None


def set_new_index_ipaq_1_value():
    st.session_state.ipaq_1 = st.session_state.key_ipaq_1

def set_new_index_ipaq_2_value():
    st.session_state.ipaq_2 = st.session_state.key_ipaq_2

def set_new_index_ipaq_3_value():
    st.session_state.ipaq_3 = st.session_state.key_ipaq_3

def set_new_index_ipaq_4_value():
    st.session_state.ipaq_4 = st.session_state.key_ipaq_4

def set_new_index_ipaq_5_value():
    st.session_state.ipaq_5 = st.session_state.key_ipaq_5

def set_new_index_ipaq_6_value():
    st.session_state.ipaq_6 = st.session_state.key_ipaq_6

def set_new_index_ipaq_7_value():
    st.session_state.ipaq_7 = st.session_state.key_ipaq_7


st.set_page_config(layout="wide")

st.header("International Physical Activity Questionnaire")

st.write("We are interested in finding out about the kinds of physical activities that people do as "
         "part of their everyday lives. The questions will ask you about the time you spent being "
         "physically active in the last 7 days. Please answer each question even if you do not "
         "consider yourself to be an active person. Please think about the activities you do at "
         "work, as part of your house and yard work, to get from place to place, and in your spare "
         "time for recreation, exercise or sport.")

with st.container(border=True):
    st.write("Think about all the vigorous activities that you did in the last 7 days. Vigorous "
             "physical activities refer to activities that take hard physical effort and make you breathe "
             "much harder than normal. Think only about those physical activities that you did for at "
             "least 10 minutes at a time.")

    if st.session_state.ipaq_1 is None:
        index_variable_ipaq_1 = None
    else:
        index_variable_ipaq_1 = st.session_state.ipaq_1
    st.session_state.ipaq_1 = st.text_input(
        label='During the last 7 days, on how many days did you do vigorous physical '
              'activities like heavy lifting, digging, aerobics, or fast bicycling? Please insert "0" for "No vigorous '
              'physical activities"',
        placeholder="Please insert here", key="key_ipaq_1", on_change=set_new_index_ipaq_1_value,
        value=index_variable_ipaq_1)


    if st.session_state.ipaq_2 is None:
        index_variable_ipaq_2 = None
    else:
        index_variable_ipaq_2 = st.session_state.ipaq_2
    st.session_state.ipaq_2 = st.text_input(
        label='How much time did you usually spend doing vigorous physical activities on one '
              'of those days? Insert modality: hh:mm per day; 00:00 for "Do not know/Not sure"',
        placeholder="Please insert here", key="key_ipaq_2", on_change=set_new_index_ipaq_2_value,
        value=index_variable_ipaq_2)

with st.container(border=True):
    st.write('Think about all the moderate activities that you did in the last 7 days. Moderate '
             'activities refer to activities that take moderate physical effort and make you breathe '
             'somewhat harder than normal. Think only about those physical activities that you did '
             'for at least 10 minutes at a time. Please insert "0" for "No moderate physical activities"')

    if st.session_state.ipaq_3 is None:
        index_variable_ipaq_3 = None
    else:
        index_variable_ipaq_3 = st.session_state.ipaq_3
    st.session_state.ipaq_3 = st.text_input(
        label='During the last 7 days, on how many days did you do moderate physical '
              'activities like carrying light loads, bicycling at a regular pace, or doubles tennis? Do not include walking.',
        placeholder="Please insert here", key="key_ipaq_3", on_change=set_new_index_ipaq_3_value,
        value=index_variable_ipaq_3)

    if st.session_state.ipaq_4 is None:
        index_variable_ipaq_4 = None
    else:
        index_variable_ipaq_4 = st.session_state.ipaq_4
    st.session_state.ipaq_4 = st.text_input(
        label='How much time did you usually spend doing moderate physical activities on one '
              'of those days? Insert modality: hh:mm per day; 00:00 for "Do not know/Not sure"',
        placeholder="Please insert here", key="key_ipaq_4", on_change=set_new_index_ipaq_4_value,
        value=index_variable_ipaq_4
    )

with st.container(border=True):
    st.write('Think about the time you spent walking in the last 7 days. This includes at work and at '
             'home, walking to travel from place to place, and any other walking that you have done '
             'solely for recreation, sport, exercise, or leisure.')

    if st.session_state.ipaq_5 is None:
        index_variable_ipaq_5 = None
    else:
        index_variable_ipaq_5 = st.session_state.ipaq_5
    st.session_state.ipaq_5 = st.text_input(
        label='During the last 7 days, on how many days did you walk for at least 10 minutes '
              'at a time? Please insert "0" for "No walking"',
        placeholder="Please insert here", key="key_ipaq_5", on_change=set_new_index_ipaq_5_value,
        value=index_variable_ipaq_5
    )

    if st.session_state.ipaq_6 is None:
        index_variable_ipaq_6 = None
    else:
        index_variable_ipaq_6 = st.session_state.ipaq_6
    st.session_state.ipaq_6 = st.text_input(
        label='How much time did you usually spend walking on one of those days? '
              'Insert modality: hh:mm per day; 00:00 for "Do not know/Not sure"',
        placeholder="Please insert here", key="key_ipaq_6", on_change=set_new_index_ipaq_6_value,
        value=index_variable_ipaq_6)

with st.container(border=True):
    st.write('The last question is about the time you spent sitting on weekdays during the last 7 '
             'days. Include time spent at work, at home, while doing course work and during leisure '
             'time. This may include time spent sitting at a desk, visiting friends, reading, or sitting or '
             'lying down to watch television.')

    if st.session_state.ipaq_7 is None:
        index_variable_ipaq_7 = None
    else:
        index_variable_ipaq_7 = st.session_state.ipaq_7
    st.session_state.ipaq_7 = st.text_input(
        label='During the last 7 days, how much time did you spend sitting on a week day? '
              'Insert modality: hh:mm per day; 00:00 for "Do not know/Not sure"*}$''',
        placeholder="Please insert here", key="key_ipaq_7", on_change=set_new_index_ipaq_7_value,
        value=index_variable_ipaq_7)


c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/trust_in_ai_new.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    if (st.session_state.ipaq_1 is not None and st.session_state.ipaq_2 is not None and st.session_state.ipaq_3 is not None
            and st.session_state.ipaq_4 is not None and st.session_state.ipaq_5 != None and st.session_state.ipaq_6 != None
            and st.session_state.ipaq_7 != None):
        st.page_link("pages/start_main_part.py", label="Next Page", icon=":material/arrow_forward:")

    #st.page_link("pages/start_main_part.py", label="Next Page", icon=":material/arrow_forward:")


st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')