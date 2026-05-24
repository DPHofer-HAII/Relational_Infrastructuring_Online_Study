import streamlit as st

st.header("Socio-Demographic Data")

if "age_option" not in st.session_state:
    st.session_state["age_option"] = None
if "age_option_index" not in st.session_state:
    st.session_state["age_option_index"] = None

if "gender_option" not in st.session_state:
    st.session_state["gender_option"] = None
if "gender_option_index" not in st.session_state:
    st.session_state["gender_option_index"] = None

if "location_option" not in st.session_state:
    st.session_state["location_option"] = None
if "location_option_index" not in st.session_state:
    st.session_state["location_option_index"] = None

if "education_option" not in st.session_state:
    st.session_state["education_option"] = None
if "education_option_index" not in st.session_state:
    st.session_state["education_option_index"] = None

if "job_situation" not in st.session_state:
    st.session_state["job_situation"] = None
if "job_situation_index" not in st.session_state:
    st.session_state["job_situation_index"] = None

def set_new_index_job_situation_value():
    st.session_state.job_situation = st.session_state.key_job_situation

with st.container(border=True):
    # CHANGE TO NUMBER
    age_option_list = ["under 18", "18 - 24", "25 - 34", "35 - 44", "45 - 54", "55 - 64", "Above 64", "Don't want to say"]
    st.write(r'''$\textsf{\footnotesize Choose ONE of the following answers:}$''')
    age_option = st.selectbox(
        r'''$\textsf{\large What is your age? *}$''',
        age_option_list, index=st.session_state.age_option_index, key="key_age_option")
    st.session_state['age_option'] = age_option
    if age_option is not None:
        st.session_state["age_option_index"] = age_option_list.index(age_option)

with st.container(border=True):
    gender_option_list = ["Male", "Female", "Intersex", "Transgender", "Gender Non-Conforming", "Other"]
    st.write(r'''$\textsf{\footnotesize Choose ONE of the following answers:}$''')
    gender_option = st.selectbox(
        r'''$\textsf{\large Which gender do you identify most with? *}$''', gender_option_list,
        index=st.session_state.gender_option_index, key="key_gender_option")
    st.session_state['gender_option'] = gender_option
    if gender_option is not None:
        st.session_state.gender_option_index = gender_option_list.index(gender_option)

with st.container(border=True):
    # CHANGE TO COUNTRY NOT CONTINENT
    location_option_list = ["North / Central America", "South America", "Europe", "Africa", "Asia", "Australia"]
    st.write(r'''$\textsf{\footnotesize Choose ONE of the following answers:}$''')
    location_option = st.selectbox(
        r'''$\textsf{\large Where is your main residence? *}$''', location_option_list,
        index=st.session_state.location_option_index, key="key_location_option")
    st.session_state['location_option'] = location_option
    if location_option is not None:
        st.session_state.location_option_index = location_option_list.index(location_option)

with (st.container(border=True)):
    education_option_list =[
        "Lower secondary education or lower education",
        "Upper secondary education",
        "Post-secondary non-tertiary education",
        "Short-cycle tertiary education",
        "Bachelor's or equivalent level",
        "Master's or equivalent level",
        "Doctoral or equivalent level",
        "NN"
    ]
    st.write(r'''$\textsf{\footnotesize Choose ONE of the following answers:}$''')
    education_option = st.selectbox(
        r'''$\textsf{\large What is your highest level of education? *}$''', education_option_list,
        index=st.session_state.education_option_index, key="key_education_option")
    st.session_state['education_option'] = education_option
    if education_option is not None:
        st.session_state.education_option_index = education_option_list.index(education_option)

with st.container(border=True):
    job_situation_list = [
        "Entrepreneur / employer",
        "Self-employed / freelancer professional",
        "Manager, officer",
        "White collar / employee",
        "Craftsman",
        "Shop owner, retailer",
        "Teacher, Professor, writer, journalist, artist",
        "Manual or technical worker",
        "Student",
        "Retired",
        "Homemaker",
        "Unemployed",
        "Other" #TODO
    ]

    if st.session_state.job_situation is None:
        index_variable_job_situation = None
    else:
        index_variable_job_situation = job_situation_list.index(st.session_state.job_situation)

    st.write(r'''$\textsf{\footnotesize Please choose the response that applies the most:}$''')
    st.session_state.job_situation = st.selectbox(
        r'''$\textsf{\large What is your current occupation? *}$''', options=job_situation_list, index=index_variable_job_situation,
        placeholder="Select all that apply!", key="key_job_situation",
        on_change=set_new_index_job_situation_value)
    # st.session_state['job_situation'] = job_situation


c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/prolific_id.py", label="Previous Page", icon=":material/arrow_back:")
with (c_end_right):
    if (st.session_state.age_option != None and st.session_state.gender_option != None and
        st.session_state.location_option != None and st.session_state.education_option != None and
        st.session_state.job_situation != None):
        st.page_link("pages/breq_3.py", label="Next Page", icon=":material/arrow_forward:")
    #st.page_link("pages/breq_3.py", label="Next Page", icon=":material/arrow_forward:")

st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')