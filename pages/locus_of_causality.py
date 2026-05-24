import streamlit as st

if 'LoC_1' not in st.session_state:
    st.session_state['LoC_1'] = None
if 'LoC_2' not in st.session_state:
    st.session_state['LoC_2'] = None
if 'LoC_3' not in st.session_state:
    st.session_state['LoC_3'] = None

def set_new_index_LoC_1_value():
    st.session_state['LoC_1'] = st.session_state['key_LoC_1']
def set_new_index_LoC_2_value():
    st.session_state['LoC_2'] = st.session_state['key_LoC_2']
def set_new_index_LoC_3_value():
    st.session_state['LoC_3'] = st.session_state['key_LoC_3']

st.header("Locus of Causality for Exercise Scale Items and Scoring")

if st.session_state.LoC_1 is None:
    index_variable_LoC_1 = None
else:
    index_variable_LoC_1 = int(st.session_state.LoC_1)-1

col1, col2 = st.columns([0.4, 0.7], vertical_alignment='bottom')
st.write(r'''$\textsf{\large I exercise because I like to rather than because I feel I have to. *}$''')
st.session_state.LoC_1 = st.radio(
    label="1 = Strongly disagree --------------------------------------- 7 = Strongly agree",
    options=["1", "2", "3", "4", "5", "6", "7"],
    index=index_variable_LoC_1,
    key="key_LoC_1",
    horizontal=True,
    on_change=set_new_index_LoC_1_value
)

if st.session_state.LoC_2 is None:
    index_variable_LoC_2 = None
else:
    index_variable_LoC_2 = int(st.session_state.LoC_2)-1

st.write(r'''$\textsf{\large Exercising is not something I would necessarily choose to do, rather it is something that I feel I ought to do. *}$''')
st.session_state.LoC_2 = st.radio(
    label="1 = Strongly disagree --------------------------------------- 7 = Strongly agree",
    options=["1", "2", "3", "4", "5", "6", "7"],
    index=index_variable_LoC_2,
    key="key_LoC_2",
    horizontal=True,
    on_change=set_new_index_LoC_2_value
)

if st.session_state.LoC_3 is None:
    index_variable_LoC_3 = None
else:
    index_variable_LoC_3 = int(st.session_state.LoC_3)-1

st.write(r'''$\textsf{\large Having to exercise is a bit of a bind but it has to be done. *}$''')
st.session_state.LoC_3 = st.radio(
    label="1 = Strongly disagree --------------------------------------- 7 = Strongly agree",
    options=["1", "2", "3", "4", "5", "6", "7"],
    index=index_variable_LoC_3,
    key="key_LoC_3",
    horizontal=True,
    on_change=set_new_index_LoC_3_value
)

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/BFI-10.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    if st.session_state.LoC_1 is not None and st.session_state.LoC_2 is not None and st.session_state.LoC_3 is not None:
        st.page_link("pages/scenario_1.py", label="Next Page", icon=":material/arrow_forward:")

st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')