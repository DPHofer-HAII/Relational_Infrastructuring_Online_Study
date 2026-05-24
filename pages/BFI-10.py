import streamlit as st

st.set_page_config(layout="wide")

if "bfi_1" not in st.session_state:
    st.session_state.bfi_1 = None
if "bfi_2" not in st.session_state:
    st.session_state.bfi_2 = None
if "bfi_3" not in st.session_state:
    st.session_state.bfi_3 = None
if "bfi_4" not in st.session_state:
    st.session_state.bfi_4 = None
if "bfi_5" not in st.session_state:
    st.session_state.bfi_5 = None
if "bfi_6" not in st.session_state:
    st.session_state.bfi_6 = None
if "bfi_7" not in st.session_state:
    st.session_state.bfi_7 = None
if "bfi_8" not in st.session_state:
    st.session_state.bfi_8 = None
if "bfi_9" not in st.session_state:
    st.session_state.bfi_9 = None
if "bfi_10" not in st.session_state:
    st.session_state.bfi_10 = None
if "bfi_11" not in st.session_state:
    st.session_state.bfi_11 = None
if "extraversion" not in st.session_state:
    st.session_state.extraversion = None
if "agreeableness" not in st.session_state:
    st.session_state.agreeableness = None
if "conscientiousness" not in st.session_state:
    st.session_state.conscientiousness = None
if "neuroticism" not in st.session_state:
    st.session_state.neuroticism = None
if "openness" not in st.session_state:
    st.session_state.openness = None

def set_new_index_bfi_1_value():
    st.session_state.bfi_1 = st.session_state.key_bfi_1
def set_new_index_bfi_2_value():
    st.session_state.bfi_2 = st.session_state.key_bfi_2
def set_new_index_bfi_3_value():
    st.session_state.bfi_3 = st.session_state.key_bfi_3
def set_new_index_bfi_4_value():
    st.session_state.bfi_4 = st.session_state.key_bfi_4
def set_new_index_bfi_5_value():
    st.session_state.bfi_5 = st.session_state.key_bfi_5
def set_new_index_bfi_6_value():
    st.session_state.bfi_6 = st.session_state.key_bfi_6
def set_new_index_bfi_7_value():
    st.session_state.bfi_7 = st.session_state.key_bfi_7
def set_new_index_bfi_8_value():
    st.session_state.bfi_8 = st.session_state.key_bfi_8
def set_new_index_bfi_9_value():
    st.session_state.bfi_9 = st.session_state.key_bfi_9
def set_new_index_bfi_10_value():
    st.session_state.bfi_10 = st.session_state.key_bfi_10
def set_new_index_bfi_11_value():
    st.session_state.bfi_11 = st.session_state.key_bfi_11
def set_new_index_extraversion_value():
    st.session_state.extraversion = st.session_state.key_extraversion
def set_new_index_agreeableness_value():
    st.session_state.agreeableness = st.session_state.key_agreeableness
def set_new_index_conscientiousness_value():
    st.session_state.conscientiousness = st.session_state.key_conscientiousness
def set_new_index_neuroticism_value():
    st.session_state.neuroticism = st.session_state.key_neuroticism
def set_new_index_openness_value():
    st.session_state.openness = st.session_state.key_openness

def translate_and_score_bfi():
    translation_map = {
        "Disagree strongly": 1,
        "Disagree a little": 2,
        "Neither agree nor disagree": 3,
        "Agree a little": 4,
        "Agree strongly": 5
    }

    def get_score(key, reverse=False):
        score = translation_map.get(st.session_state[key], 3)
        return 6 - score if reverse else score

    extraversion_score = (get_score("bfi_1", reverse=True) + get_score("bfi_6")) / 2
    if extraversion_score == 5:
        st.session_state.extraversion = "extroverted"
    elif extraversion_score == 4:
        st.session_state.extraversion = "slightly extroverted"
    elif extraversion_score == 1: st.session_state.extraversion = "introverted"
    elif extraversion_score == 2: st.session_state.extraversion = "slightly introverted"
    else: st.session_state.extraversion = "neither extroverted nor introverted"

    agreeableness_score = (get_score("bfi_2") + get_score("bfi_7", reverse=True)) / 2
    if agreeableness_score == 5:
        st.session_state.agreeableness = "agreeable"
    elif agreeableness_score == 4:
        st.session_state.agreeableness = "slightly agreeable"
    elif agreeableness_score == 1: st.session_state.agreeableness = "antagonistic"
    elif agreeableness_score == 2: st.session_state.agreeableness = "slightly antagonistic"
    else: st.session_state.agreeableness = "neither agreeable nor antagonistic"

    conscientiousness_score = (get_score("bfi_3", reverse=True) + get_score("bfi_8")) / 2
    if conscientiousness_score == 5:
        st.session_state.conscientiousness = "conscientious"
    elif conscientiousness_score == 4:
        st.session_state.conscientiousness = "slightly conscientious"
    elif conscientiousness_score == 1: st.session_state.conscientiousness = "unconscientious"
    elif conscientiousness_score == 2: st.session_state.conscientiousness = "slightly unconscientious"
    else: st.session_state.conscientiousness = "neither conscientious nor unconscientious"

    neuroticism_score = (get_score("bfi_4", reverse=True) + get_score("bfi_9")) / 2
    if neuroticism_score == 5:
        st.session_state.neuroticism = "neurotic"
    elif neuroticism_score == 4:
        st.session_state.neuroticism = "slightly neurotic"
    elif neuroticism_score == 1: st.session_state.neuroticism = "emotionally stable"
    elif neuroticism_score == 2: st.session_state.neuroticism = "slightly emotionally stable"
    else: st.session_state.neuroticism = "neither neurotic nor emotionally stable"

    openness_score = (get_score("bfi_5", reverse=True) + get_score("bfi_10")) / 2
    if openness_score == 5:
        st.session_state.openness = "open to experience"
    elif openness_score == 4:
        st.session_state.openness = "slightly open to experience"
    elif openness_score == 1: st.session_state.openness = "closed to experience"
    elif openness_score == 2: st.session_state.openness = "slightly closed to experience"
    else: st.session_state.openness = "neither open to experience nor closed to experience"

    # st.session_state.extraversion = (get_score("bfi_1", reverse=True) + get_score("bfi_6")) / 2
    # st.session_state.agreeableness = (get_score("bfi_2") + get_score("bfi_7", reverse=True)) / 2
    # st.session_state.conscientiousness = (get_score("bfi_3", reverse=True) + get_score("bfi_8")) / 2
    # st.session_state.neuroticism = (get_score("bfi_4", reverse=True) + get_score("bfi_9")) / 2
    # st.session_state.openness = (get_score("bfi_5", reverse=True) + get_score("bfi_10")) / 2
    print("Extraversion: ", st.session_state.extraversion)
    print("Agreeableness: ", st.session_state.agreeableness)
    print("Conscientiousness: ", st.session_state.conscientiousness)
    print("Neuroticism: ", st.session_state.neuroticism)
    print("Openness: ", st.session_state.openness)


st.header("Big Five Inventory 10 Questionnaire")
st.write("How well do the following statements describe your personality? I see myself as someone who...")

bfi_10_options = ["Disagree strongly", "Disagree a little", "Neither agree nor disagree", "Agree a little", "Agree strongly"]

with st.container(border=True):
    if st.session_state.bfi_1 is None:
        index_variable_bfi_1 = None
    else:
        index_variable_bfi_1 = bfi_10_options.index(st.session_state.bfi_1)
    st.session_state.bfi_1 = st.radio(r'''$\textsf{\large ... is reserved *}$''', options=bfi_10_options,
        index=index_variable_bfi_1, key="key_bfi_1", horizontal=True, on_change=set_new_index_bfi_1_value)

with st.container(border=True):
    if st.session_state.bfi_2 is None:
        index_variable_bfi_2 = None
    else:
        index_variable_bfi_2 = bfi_10_options.index(st.session_state.bfi_2)
    st.session_state.bfi_2 = st.radio(r'''$\textsf{\large ... is generally trusting *}$''', options=bfi_10_options,
        index=index_variable_bfi_2, key="key_bfi_2", horizontal=True, on_change=set_new_index_bfi_2_value)

with st.container(border=True):
    if st.session_state.bfi_3 is None:
        index_variable_bfi_3 = None
    else:
        index_variable_bfi_3 = bfi_10_options.index(st.session_state.bfi_3)
    st.session_state.bfi_3 = st.radio(r'''$\textsf{\large ... tends to be lazy *}$''', options=bfi_10_options,
        index=index_variable_bfi_3, key="key_bfi_3", horizontal=True, on_change=set_new_index_bfi_3_value)

with st.container(border=True):
    if st.session_state.bfi_4 is None:
        index_variable_bfi_4 = None
    else:
        index_variable_bfi_4 = bfi_10_options.index(st.session_state.bfi_4)
    st.session_state.bfi_4 = st.radio(r'''$\textsf{\large ... is relaxed, handles stress well *}$''', options=bfi_10_options,
        index=index_variable_bfi_4, key="key_bfi_4", horizontal=True, on_change=set_new_index_bfi_4_value)

with st.container(border=True):
    if st.session_state.bfi_5 is None:
        index_variable_bfi_5 = None
    else:
        index_variable_bfi_5 = bfi_10_options.index(st.session_state.bfi_5)
    st.session_state.bfi_5 = st.radio(r'''$\textsf{\large ... has few artistic interests *}$''', options=bfi_10_options,
        index=index_variable_bfi_5, key="key_bfi_5", horizontal=True, on_change=set_new_index_bfi_5_value)

with st.container(border=True):
    if st.session_state.bfi_6 is None:
        index_variable_bfi_6 = None
    else:
        index_variable_bfi_6 = bfi_10_options.index(st.session_state.bfi_6)
    st.session_state.bfi_6 = st.radio(r'''$\textsf{\large ... is outgoing, sociable *}$''', options=bfi_10_options,
        index=index_variable_bfi_6, key="key_bfi_6", horizontal=True, on_change=set_new_index_bfi_6_value)

with st.container(border=True):
    if st.session_state.bfi_7 is None:
        index_variable_bfi_7 = None
    else:
        index_variable_bfi_7 = bfi_10_options.index(st.session_state.bfi_7)
    st.session_state.bfi_7 = st.radio(r'''$\textsf{\large ... tends to find fault with others *}$''', options=bfi_10_options,
        index=index_variable_bfi_7, key="key_bfi_7", horizontal=True, on_change=set_new_index_bfi_7_value)

with st.container(border=True):
    if st.session_state.bfi_8 is None:
        index_variable_bfi_8 = None
    else:
        index_variable_bfi_8 = bfi_10_options.index(st.session_state.bfi_8)
    st.session_state.bfi_8 = st.radio(r'''$\textsf{\large ... does a thorough job *}$''', options=bfi_10_options,
        index=index_variable_bfi_8, key="key_bfi_8", horizontal=True, on_change=set_new_index_bfi_8_value)

with st.container(border=True):
    if st.session_state.bfi_9 is None:
        index_variable_bfi_9 = None
    else:
        index_variable_bfi_9 = bfi_10_options.index(st.session_state.bfi_9)
    st.session_state.bfi_9 = st.radio(r'''$\textsf{\large ... gets nervous easily *}$''', options=bfi_10_options,
        index=index_variable_bfi_9, key="key_bfi_9", horizontal=True, on_change=set_new_index_bfi_9_value)

with st.container(border=True):
    if st.session_state.bfi_10 is None:
        index_variable_bfi_10 = None
    else:
        index_variable_bfi_10 = bfi_10_options.index(st.session_state.bfi_10)
    st.session_state.bfi_10 = st.radio(r'''$\textsf{\large ... has an active imagination *}$''', options=bfi_10_options,
        index=index_variable_bfi_10, key="key_bfi_10", horizontal=True, on_change=set_new_index_bfi_10_value)

with st.container(border=True):
    if st.session_state.bfi_11 is None:
        index_variable_bfi_11 = None
    else:
        index_variable_bfi_11 = bfi_10_options.index(st.session_state.bfi_11)
    st.session_state.bfi_11 = st.radio(r'''$\textsf{\large ... is considerate and kind to almost everyone *}$''', options=bfi_10_options,
        index=index_variable_bfi_11, key="key_bfi_11", horizontal=True, on_change=set_new_index_bfi_11_value)

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/breq_3.py", label="Previous Page", icon=":material/arrow_back:")
with ((c_end_right)):
    if (st.session_state.bfi_1 is not None and st.session_state.bfi_2 is not None and st.session_state.bfi_3 is not None
        and st.session_state.bfi_4 is not None and st.session_state.bfi_5 is not None and st.session_state.bfi_6 is not None
        and st.session_state.bfi_7 is not None and st.session_state.bfi_8 is not None and st.session_state.bfi_9 is not None
        and st.session_state.bfi_10 is not None and st.session_state.bfi_11 is not None):
    #         st.page_link("pages/regulatory_focus.py", label="Next Page", icon=":material/arrow_forward:")
        translate_and_score_bfi()
        st.page_link("pages/regulatory_focus.py", label="Next Page", icon=":material/arrow_forward:")
    #st.page_link("pages/regulatory_focus.py", label="Next Page", icon=":material/arrow_forward:")

st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')