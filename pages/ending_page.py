import streamlit as st

st.header('Thank You for Participating')
st.write("Dear Participants,")
st.write("Thank you for taking the time to complete our online questionnaire. Your input is highly valuable and plays a crucial role in advancing our research. We truly appreciate the effort you’ve made and the perspectives you’ve shared.")
st.write("To finalize your participation, please click the link below:")
url = "DELETED for publication"
st.markdown("[Link back to Prolific](%s)" % url)
st.write("With gratitude,")
st.write("Researcher")
st.write("Researcher")
st.write("Researcher")

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/post_study_questions.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    pass