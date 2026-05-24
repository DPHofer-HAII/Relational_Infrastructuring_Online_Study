import streamlit as st
from streamlit_sortables import sort_items

st.set_page_config(layout="wide")

st.header("Trust in Artificial Intelligence")
st.write("""
Let’s talk about Artificial Intelligence. Consider a simple definition: 
Artificial intelligence (AI) refers to computer systems that can perform tasks that 
usually require intelligence (e.g. making decisions, achieving goals, planning, learning, reasoning, etc.). 
AI systems can perform these tasks based on objectives set by humans with a few explicit instructions.
""")

# Dynamically initialize session state
for i in range(1, 21):
    st.session_state.setdefault(f"tiai_{i}", None)

# ===============================
# Question templates and handlers
# ===============================

tiai_1_options = ["Strongly approve", "Approve", "Indifferent", "Disapprove", "Strongly disapprove"]
tiai_2_options = ["Very comfortable", "Fairly comfortable", "Neutral", "Not very comfortable", "Not at all comfortable"]
tiai_6_options = ["Strongly agree", "Agree", "Neutral", "Disagree", "Strongly disagree"]
tiai_8_options = ["A lot", "Somewhat", "So and so", "Not so much", "Not at all"]
tiai_9_options = [
    "Very expert: I am sure of my digital skills, I am always attentive to innovation, I have no difficulty in moving in the digital world for everything I need, and I am interested in.",
    "Expert: I am quite sure of my digital skills, I try to exploit the potential it can offer and to be updated on the news.",
    "Enough expert: I'm not entirely sure of my skills, but I manage to do the best I can when I need to do something online and I try to learn new skills when I need them.",
    "Not very expert: I'm not sure of my skills and I have to get someone to help me with new things I don't understand.",
    "Not at all expert: I use digital tools only if it is strictly necessary (e.g. email, messages)"
]

def radio_question(prompt, options, key):
    index = options.index(st.session_state[key]) if st.session_state[key] in options else None

    def update_value():
        st.session_state[key] = st.session_state[f"key_{key}"]

    col1, col2 = st.columns([4, 10])
    with col1:
        st.write(prompt)
    with col2:
        st.radio(
            label="",
            options=options,
            index=index,
            key=f"key_{key}",
            label_visibility="collapsed",
            horizontal=True,
            on_change=update_value
        )

def grouped_radio_questions(title, items, options):
    with st.container(border=True):
        st.write(title)
        for i, text in enumerate(items, start=2):  # Starts from tiai_2
            radio_question(text, options, f"tiai_{i}")

# ====================================
# Questions
# ====================================

# Q1
with st.container(border=True):
    radio_question(
        "How would you describe your attitude towards Artificial Intelligence (AI) and its applications? *",
        tiai_1_options,
        "tiai_1"
    )

# Q2
grouped_radio_questions(
    "How would you describe your attitude towards the use of AI in the following sectors? *",
    [
        "Healthcare (e.g. diagnostic support, personalised medicine).",
        "Insurance (e.g. fraud detection, personalzed risk assessment).",
        "Agriculture (e.g. robotic harvesting, crop optimization).",
        "Finance (e.g. fraud detection, loan decision support systems).",
        "Military (e.g. automated weapons, cybersecurity for data protection).",
        "Law enforcement (e.g. predictive policing, face recognition in public places).",
        "Environmental (e.g. climate prediction, energy harvesting forecast).",
        "Transportation (e.g. self-driving vehicles).",
        "Manufacturing industry (e.g. demand forecasting, robotics).",
        "Human resource management (e.g. CV screening, workforce planning)."
    ],
    tiai_1_options
)

# Q3
with st.container(border=True):
    radio_question(
        "Imagine that you are applying for a job in a large company and the recruitment process consists of two steps. The first step is based on an AI software which scans your resume and your answers to a set of questions on strategic competencies. The software assigns you a score which is used to select those candidates who can move on to the second stage (the interview). The company claims that the software makes the process faster and more objective. Also, the company says that the data is anonymised, and no personal information is used. To what extent would you feel comfortable or uncomfortable with this process? *",
        tiai_2_options,
        "tiai_12"
    )

# Q4
with st.container(border=True):
    radio_question(
        "Imagine that you are looking for a smart meter to reduce energy consumption in your house, cut the cost of utilities, and adopt a more sustainable lifestyle. You are offered a smart meter that uses AI to analyse home energy consumption and make recommendations for more efficient usage. Among functionalities, this system can give you the opportunity to receive personalised offers from energy suppliers which can help you save money. The company producing the smart meter says that your data is anonymised, and no personal information is shared with third parties without your consent. To what extent would you feel comfortable or uncomfortable with this application? *",
        tiai_2_options,
        "tiai_13"
    )

# Q5 - Sortable Ranking with State Preservation
with st.container(border=True):
    st.subheader("Which aspects should an organisation developing/using AI consider most? Select and rank three. *")
    st.write("Should an error occur, please click on 'previous page' and then come back to this page again. Do NOT refresh the page!")
    if "sorted_items" not in st.session_state:
        st.session_state.sorted_items = [
            {"header": "Aspects", "items": [
                "Security and accurate results.",
                "Fair treatment and equitable access to the AI application for all members of society.",
                "Privacy and data protection.",
                "Human supervision over the AI outcome and process.",
                "Clear communication about the AI application's purpose and limitations.",
                "Risk management and identification of responsibility.",
                "Societal and environmental impact of the AI application."
            ]},
            {"header": "Your Ranking (Top 3)", "items": []}
        ]

    st.session_state.sorted_items = sort_items(
        st.session_state.sorted_items, multi_containers=True, key="sortable_q5"
    )

    if len(st.session_state.sorted_items[1]["items"]) < 3:
        st.warning("Please make sure to pick 3 aspects and sort them according to your preferences. *")
    else:
        st.info("Your sorted preferences are saved and will persist.")

# Q6
with st.container(border=True):
    radio_question(
        "To what extent do you agree that better education on AI would improve your trust? *",
        tiai_6_options,
        "tiai_14"
    )

# Q8 - Trust Entities
def trust_question(text, key):
    index = tiai_8_options.index(st.session_state[key]) if st.session_state[key] in tiai_8_options else None

    def update_value():
        st.session_state[key] = st.session_state[f"key_{key}"]

    col1, col2 = st.columns([4, 10])
    with col1:
        st.write(text)
    with col2:
        st.radio(
            label="",
            options=tiai_8_options,
            index=index,
            key=f"key_{key}",
            label_visibility="collapsed",
            horizontal=True,
            on_change=update_value
        )

with st.container(border=True):
    st.write("How much do you trust the following entities to ensure AI is in the public's best interest? *")
    trust_question("National Governments and public authorities.", "tiai_15")
    trust_question("Universities and research centres.", "tiai_16")
    trust_question("Consumer associations, trade unions and civil society organisations.", "tiai_17")
    trust_question("Tech companies developing AI products.", "tiai_18")
    trust_question("Social media companies.", "tiai_19")

# Ensure tiai_20 exists in session state
if "tiai_20" not in st.session_state:
    st.session_state.tiai_20 = None

with st.container(border=True):
    if st.session_state.tiai_20 is None:
        index_variable_tiai_20 = None
    else:
        index_variable_tiai_20 = tiai_9_options.index(st.session_state.tiai_20)
    st.write("If you were to describe your digital skills, how would you define yourself:")
    st.session_state.tiai_20 = st.selectbox(
        label="no label needed",
        options=[
            "Very expert: I am sure of my digital skills, I am always attentive to innovation, I have no difficulty in moving in the digital world for everything I need, and I am interested in.",
            "Expert: I am quite sure of my digital skills, I try to exploit the potential it can offer and to be updated on the news.",
            "Enough expert: I'm not entirely sure of my skills, but I manage to do the best I can when I need to do something online and I try to learn new skills when I need them.",
            "Not very expert: I'm not sure of my skills and I have to get someone to help me with new things I don't understand.",
        "Not at all expert: I use digital tools only if it is strictly necessary (e.g. email, messages)"
        ],
        index=index_variable_tiai_20,

    )

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/regulatory_focus.py", label="Previous Page", icon=":material/arrow_back:")
    # st.page_link("pages/scenario_5.py", label="Previous Page", icon=":material/arrow_back:")
with c_end_right:
    if (st.session_state.tiai_1 is not None and st.session_state.tiai_2 is not None and st.session_state.tiai_3 is not None
    and st.session_state.tiai_4 is not None and st.session_state.tiai_5 is not None and st.session_state.tiai_6 is not None
    and st.session_state.tiai_7 is not None and st.session_state.tiai_8 is not None and st.session_state.tiai_9 is not None
    and st.session_state.tiai_10 is not None and st.session_state.tiai_11 is not None and st.session_state.tiai_12 is not None
    and st.session_state.tiai_13 is not None and st.session_state.tiai_14 is not None and st.session_state.tiai_15 is not None
    and st.session_state.tiai_16 is not None and st.session_state.tiai_17 is not None and st.session_state.tiai_18 is not None
    and st.session_state.tiai_19 is not None and st.session_state.tiai_20 is not None
    and len(st.session_state.sorted_items[1]["items"]) >= 3):
        st.page_link("pages/ipaq.py", label="Next Page", icon=":material/arrow_forward:")
    #st.page_link("pages/ipaq.py", label="Next Page", icon=":material/arrow_forward:")

st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')