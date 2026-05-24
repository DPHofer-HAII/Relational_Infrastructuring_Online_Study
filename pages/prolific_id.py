import streamlit as st
from datetime import datetime

if "prolific_id" not in st.session_state:
    st.session_state.prolific_id = ""
if "start_time" not in st.session_state:
    st.session_state["start_time"] = datetime.now().isoformat()

st.header("Prolific ID *")
with st.container(border=True):
    st.session_state.prolific_id = st.text_input("Please enter your unique prolific ID:", value=st.session_state.prolific_id)

# Only if prolific_id is not Null can they continue
c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("TITLE_PAGE.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    if st.session_state.prolific_id != "":
        st.page_link("pages/socio_demographic_data.py", label="Save & Continue", icon=":material/arrow_forward:")
    #st.page_link("pages/socio_demographic_data.py", label="Save & Continue", icon=":material/arrow_forward:")

st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')