import streamlit as st

if 'rapa_1' not in st.session_state:
    st.session_state['rapa_1'] = None
if 'rapa_2' not in st.session_state:
    st.session_state['rapa_2'] = None
if 'rapa_3' not in st.session_state:
    st.session_state['rapa_3'] = None
if 'rapa_4' not in st.session_state:
    st.session_state['rapa_4'] = None
if 'rapa_5' not in st.session_state:
    st.session_state['rapa_5'] = None
if 'rapa_6' not in st.session_state:
    st.session_state['rapa_6'] = None
if 'rapa_7' not in st.session_state:
    st.session_state['rapa_7'] = None
if 'rapa_8' not in st.session_state:
    st.session_state['rapa_8'] = None
if 'rapa_9' not in st.session_state:
    st.session_state['rapa_9'] = None

def set_new_index_rapa_1_value():
    st.session_state.rapa_1 = st.session_state.key_rapa_1
def set_new_index_rapa_2_value():
    st.session_state.rapa_2 = st.session_state.key_rapa_2
def set_new_index_rapa_3_value():
    st.session_state.rapa_3 = st.session_state.key_rapa_3
def set_new_index_rapa_4_value():
    st.session_state.rapa_4 = st.session_state.key_rapa_4
def set_new_index_rapa_5_value():
    st.session_state.rapa_5 = st.session_state.key_rapa_5
def set_new_index_rapa_6_value():
    st.session_state.rapa_6 = st.session_state.key_rapa_6
def set_new_index_rapa_7_value():
    st.session_state.rapa_7 = st.session_state.key_rapa_7
def set_new_index_rapa_8_value():
    st.session_state.rapa_8 = st.session_state.key_rapa_8
def set_new_index_rapa_9_value():
    st.session_state.rapa_9 = st.session_state.key_rapa_9

st.set_page_config(layout="wide")

st.header("Rapid Assessment of Physical Activity")

st.write("Physical Activities (PA) are activities where you move and increase your heart rate above its resting rate, whether you do them for pleasure, work, or transportation.")
st.write("The following questions ask about the amount and intensity of physical activity you usually do. The intensity of the activity is related to the amount of energy you used to do these activities.")

st.subheader("Examples of physical activity intensity levels:")
st.image("images/Rapa_Examples.png", caption="Examples of physical activity intensity levels by the University of Washington Health Promotion Research Center, © 2006.")

rapa_option_list = ["Yes", "No"]

if st.session_state.rapa_1 is None:
    index_variable_rapa_1 = None
else:
    index_variable_rapa_1 = rapa_option_list.index(st.session_state.rapa_1)
st.session_state.rapa_1 = st.radio(r'''$\textsf{\large I rarely or never do any physical activities. *}$''', rapa_option_list,
                                   index=index_variable_rapa_1, key="key_rapa_1", horizontal=True, on_change=set_new_index_rapa_1_value)

if st.session_state.rapa_2 is None:
    index_variable_rapa_2 = None
else:
    index_variable_rapa_2 = rapa_option_list.index(st.session_state.rapa_2)
st.session_state.rapa_2 = st.radio(r'''$\textsf{\large I do some light or moderate physical activities, but not every week. *}$''', rapa_option_list,
                                   index=index_variable_rapa_2, key="key_rapa_2", horizontal=True, on_change=set_new_index_rapa_2_value)

if st.session_state.rapa_3 is None:
    index_variable_rapa_3 = None
else:
    index_variable_rapa_3 = rapa_option_list.index(st.session_state.rapa_3)
st.session_state.rapa_3 = st.radio(r'''$\textsf{\large I do some light physical activity every week. *}$''', rapa_option_list,
                                   index=index_variable_rapa_3, key="key_rapa_3", horizontal=True, on_change=set_new_index_rapa_3_value)

if st.session_state.rapa_4 is None:
    index_variable_rapa_4 = None
else:
    index_variable_rapa_4 = rapa_option_list.index(st.session_state.rapa_4)
st.session_state.rapa_4 = st.radio(r'''$\textsf{\large I do moderate physical activities every week, but less than 30 minutes a day or 5 days a week. *}$''', rapa_option_list,
                                   index=index_variable_rapa_4, key="key_rapa_4", horizontal=True, on_change=set_new_index_rapa_4_value)

if st.session_state.rapa_5 is None:
    index_variable_rapa_5 = None
else:
    index_variable_rapa_5 = rapa_option_list.index(st.session_state.rapa_5)
st.session_state.rapa_5 = st.radio(r'''$\textsf{\large I do vigorous physical activities every week, but less than 20 minutes a day or 3 days a week. *}$''', rapa_option_list,
                                   index=index_variable_rapa_5, key="key_rapa_5", horizontal=True, on_change=set_new_index_rapa_5_value)

if st.session_state.rapa_6 is None:
    index_variable_rapa_6 = None
else:
    index_variable_rapa_6 = rapa_option_list.index(st.session_state.rapa_6)
st.session_state.rapa_6 = st.radio(r'''$\textsf{\large I do 30 minutes or more a day of moderate physical activities, 5 or more days a week. *}$''', rapa_option_list,
                                   index=index_variable_rapa_6, key="key_rapa_6", horizontal=True, on_change=set_new_index_rapa_6_value)

if st.session_state.rapa_7 is None:
    index_variable_rapa_7 = None
else:
    index_variable_rapa_7 = rapa_option_list.index(st.session_state.rapa_7)
st.session_state.rapa_7 = st.radio(r'''$\textsf{\large I do 20 minutes or more a day of vigorous physical activities, 3 or more days a week. *}$''', rapa_option_list,
                                   index=index_variable_rapa_7, key="key_rapa_7", horizontal=True, on_change=set_new_index_rapa_7_value)

if st.session_state.rapa_8 is None:
    index_variable_rapa_8 = None
else:
    index_variable_rapa_8 = rapa_option_list.index(st.session_state.rapa_8)
st.session_state.rapa_8 = st.radio(r'''$\textsf{\large I do activities to increase muscle strength, such as lifting weights or calisthenics, once a week or more. *}$''', rapa_option_list,
                                   index=index_variable_rapa_8, key="key_rapa_8", horizontal=True, on_change=set_new_index_rapa_8_value)

if st.session_state.rapa_9 is None:
    index_variable_rapa_9 = None
else:
    index_variable_rapa_9 = rapa_option_list.index(st.session_state.rapa_9)
st.session_state.rapa_9 = st.radio(r'''$\textsf{\large I do activities to improve flexibility, such as stretching or yoga, once a week or more. *}$''', rapa_option_list,
                                   index=index_variable_rapa_9, key="key_rapa_9", horizontal=True, on_change=set_new_index_rapa_9_value)

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/socio_demographic_data.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    if (st.session_state.rapa_1 is not None and st.session_state.rapa_2 is not None and st.session_state.rapa_3 is not None
            and st.session_state.rapa_4 is not None and st.session_state.rapa_5 != None and st.session_state.rapa_6 != None
            and st.session_state.rapa_7 != None and st.session_state.rapa_8 != None and st.session_state.rapa_9 != None):
        st.page_link("pages/BFI-10.py", label="Next Page", icon=":material/arrow_forward:")

st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')