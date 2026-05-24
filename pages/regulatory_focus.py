import streamlit as st

st.set_page_config(layout="wide")

st.header("Regulatory Focus Questionnaire")

st.write("This set of questions asks you about specific events in your life. Please indicate your answer to each question.")
st.write("Response scale: 1 (never or seldom) to 3 (sometimes) to 5 (very often)")

# Option list and question prompts
regulatory_focus_option_list = ["1", "2", "3", "4", "5"]
regulatory_focus_questions = {
    1: "Compared to most people, are you typically unable to get what you want out of life? *",
    2: "Growing up, would you ever 'cross the line' by doing things that your parents would not tolerate? *",
    3: "How often have you accomplished things that got you 'psyched' to work even harder? *",
    4: "Did you get on your parents' nerves often when you were growing up? *",
    5: "How often did you obey rules and regulations that were established by your parents? *",
    6: "Growing up, did you ever act in ways that your parents thought were objectionable? *",
    7: "Do you often do well at different things that you try? *",
    8: "Not being careful enough has gotten me into trouble at times. *",
    9: "When it comes to achieving things that are important to me, I find that I don't perform as well as I ideally would like to do. *",
    10: "I feel like I have made progress toward being successful in my life. *",
    11: "I have found very few hobbies or activities in my life that capture my interest or motivate me to put effort into them. *"
}


# Session state initialization
for i in range(1, 12):
    with st.container(border=True):
        regulatory_focus_key = f'regulatory_focus_{i}'
        key_key = f'key_regulatory_focus_{i}'
        if regulatory_focus_key not in st.session_state:
            st.session_state[regulatory_focus_key] = None

        # Define the callback dynamically
        def make_callback(index):
            def callback():
                st.session_state[f'regulatory_focus_{index}'] = st.session_state[f'key_regulatory_focus_{index}']
            return callback

        # Determine radio index
        current_value = st.session_state[f'regulatory_focus_{i}']
        index_variable = regulatory_focus_option_list.index(current_value) if current_value in regulatory_focus_option_list else None

        # Render radio button
        st.session_state[f'regulatory_focus_{i}'] = st.radio(
            regulatory_focus_questions[i],
            regulatory_focus_option_list,
            index=index_variable,
            key=f'key_regulatory_focus_{i}',
            horizontal=True,
            on_change=make_callback(i)
        )

# Navigation buttons
c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/BFI-10.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    if all(st.session_state[f'regulatory_focus_{i}'] is not None for i in range(1, 12)):
        st.page_link("pages/trust_in_ai_new.py", label="Next Page", icon=":material/arrow_forward:")
    #st.page_link("pages/trust_in_ai_new.py", label="Next Page", icon=":material/arrow_forward:")

st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')
