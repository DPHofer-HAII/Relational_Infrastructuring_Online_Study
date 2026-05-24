import streamlit as st
import time

st.set_page_config(layout="wide")

st.header('Beginning Main Part')
st.error("PLEASE READ CAREFULLY!!!")
st.error("By clicking the 'Next Page' icon, you will begin the main part of the study. Please note that the initialization process may take a few minutes. Do NOT refresh the page at any point while participating in the study. Doing so will result in the loss of all collected data and will require you to restart the study from the beginning. Thank you for your cooperation.")
st.error("PLEASE READ CAREFULLY!!!")

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/ipaq.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    agree = st.checkbox("I read & understood the above message")
    if agree:
        st.page_link("pages/scenario_1_new.py", label="Next Page", icon=":material/arrow_forward:")