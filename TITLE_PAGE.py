import streamlit as st

st.set_page_config(layout="wide")

st.title("Evaluation and Comparison of Just-in-Time Adaptive Interventions")
st.write(
"In this online survey, you will be asked to evaluate AI-generated messages known as Just-in-Time Adaptive Interventions (JITAIs), which are designed to promote physical activity by leveraging contextual information such as weather, stress level, and geolocation."
" JITAIs aim to encourage healthy behavior at moments when individuals are most likely to be receptive. These interventions often utilize a combination of sensor data and self-reported inputs to identify optimal times for delivering support. For example, if a person has been sedentary for an extended period, a JITAI might prompt them to stand up and move. However, the effectiveness of JITAIs depends on ensuring that notifications are timely and not overly frequent or intrusive, as excessive messaging can lead to disengagement."
)
st.write("")
st.subheader("Your Role in the Study")
st.write("You will evaluate different AI-generated messages for five distinct scenarios. Each scenario will involve the following steps:")
st.write("  1.	Select or confirm a day and time: A random day and time from your previous week (Monday to Sunday) will be suggested, which you can adjust if needed.")
st.write("  2.	Describe the context: Answer a few questions about your situation at that specific day and time.")
st.write("  3.	Evaluate messages: Review and rate eight different JITAI messages tailored to the provided context.")
st.write("Throughout the study please respond based on your first impression or gut feeling. There are no right or wrong answers—we are interested in your intuitive, immediate reactions rather than overly considered responses.")

st.write("")
st.subheader("Time Commitment")
st.write("The full study will take approximately 90 minutes to complete:")
st.write("  •	Pre-study questionnaire: ~20 minutes")
st.write("  •	Scenario-based evaluations: ~60 minutes")
st.write("  •	Post-study questionnaire: ~10 minutes")

st.write("")
st.subheader("Voluntary Participation")
st.write("Your involvement in this research is entirely optional. You are welcome to withdraw at any point during the study without any consequences. Should you have any questions or concerns, please do not hesitate to ask.")
st.write("By clicking the button below, you acknowledge that:")
st.write("  •	Your participation in the study is voluntary.")
st.write("  •	You are 18 years of age or older.")
st.write("  •	You are aware that you may choose to terminate your participation at any time for any reason.")
st.write("If you do not consent to participate in this study, please return this submission on Prolific by selecting the 'stop without completing' button.")

st.warning("IMPORTANT: If you face a technical issue (e.g., page not loading), click the three dots in the top right and select 'Rerun.' Avoid refreshing the page as it may cause data loss. Also, watch for the loading sign in the top right and ensure a stable internet connection to avoid delays.")

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_right:
    st.page_link("pages/prolific_id.py", label="Accept & Continue", icon=":material/arrow_forward:")
    #st.page_link("pages/scenario_1_new.py", label="Next Page", icon=":material/arrow_forward:")

