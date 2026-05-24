# import streamlit as st
# from streamlit_sortables import sort_items
#
# st.set_page_config(layout="wide")
#
# st.header("Trust in Artificial Intelligence")
# st.write("Let’s talk about Artificial Intelligence. Consider a simple definition: Artificial intelligence (AI) refers to computer systems that can perform tasks that usually require intelligence (e.g. making decisions, achieving goals, planning, learning, reasoning, etc.). AI systems can perform these tasks based on objectives set by humans with a few explicit instructions.")
#
# if "tiai_1" not in st.session_state:
#     st.session_state["tiai_1"] = None
# if "tiai_1_index" not in st.session_state:
#     st.session_state["tiai_1_index"] = None
#
# if "tiai_2" not in st.session_state:
#     st.session_state["tiai_2"] = None
# if "tiai_2_index" not in st.session_state:
#     st.session_state["tiai_2_index"] = None
#
# if "tiai_3" not in st.session_state:
#     st.session_state["tiai_3"] = None
# if "tiai_3_index" not in st.session_state:
#     st.session_state["tiai_3_index"] = None
#
# if "tiai_4" not in st.session_state:
#     st.session_state["tiai_4"] = None
# if "tiai_4_index" not in st.session_state:
#     st.session_state["tiai_4_index"] = None
#
# if "tiai_5" not in st.session_state:
#     st.session_state["tiai_5"] = None
# if "tiai_5_index" not in st.session_state:
#     st.session_state["tiai_5_index"] = None
#
# if "tiai_6" not in st.session_state:
#     st.session_state["tiai_6"] = None
# if "tiai_6_index" not in st.session_state:
#     st.session_state["tiai_6_index"] = None
#
# if "tiai_7" not in st.session_state:
#     st.session_state["tiai_7"] = None
# if "tiai_7_index" not in st.session_state:
#     st.session_state["tiai_7_index"] = None
#
# if "tiai_8" not in st.session_state:
#     st.session_state["tiai_8"] = None
# if "tiai_8_index" not in st.session_state:
#     st.session_state["tiai_8_index"] = None
#
# if "tiai_9" not in st.session_state:
#     st.session_state["tiai_9"] = None
# if "tiai_9_index" not in st.session_state:
#     st.session_state["tiai_9_index"] = None
#
# if "tiai_10" not in st.session_state:
#     st.session_state["tiai_10"] = None
# if "tiai_10_index" not in st.session_state:
#     st.session_state["tiai_10_index"] = None
#
# if "tiai_11" not in st.session_state:
#     st.session_state["tiai_11"] = None
# if "tiai_11_index" not in st.session_state:
#     st.session_state["tiai_11_index"] = None
#
# if "tiai_12" not in st.session_state:
#     st.session_state["tiai_12"] = None
# if "tiai_12_index" not in st.session_state:
#     st.session_state["tiai_12_index"] = None
#
# if "tiai_13" not in st.session_state:
#     st.session_state["tiai_13"] = None
# if "tiai_13_index" not in st.session_state:
#     st.session_state["tiai_13_index"] = None
#
# if "tiai_14" not in st.session_state:
#     st.session_state["tiai_14"] = None
# if "tiai_14_index" not in st.session_state:
#     st.session_state["tiai_14_index"] = None
#
# if "tiai_15" not in st.session_state:
#     st.session_state["tiai_15"] = None
# if "tiai_15_index" not in st.session_state:
#     st.session_state["tiai_15_index"] = None
#
# if "tiai_16" not in st.session_state:
#     st.session_state["tiai_16"] = None
# if "tiai_16_index" not in st.session_state:
#     st.session_state["tiai_16_index"] = None
#
# if "tiai_17" not in st.session_state:
#     st.session_state["tiai_17"] = None
# if "tiai_17_index" not in st.session_state:
#     st.session_state["tiai_17_index"] = None
#
# if "tiai_18" not in st.session_state:
#     st.session_state["tiai_18"] = None
# if "tiai_18_index" not in st.session_state:
#     st.session_state["tiai_18_index"] = None
#
# if "tiai_19" not in st.session_state:
#     st.session_state["tiai_19"] = None
# if "tiai_19_index" not in st.session_state:
#     st.session_state["tiai_19_index"] = None
#
# if "tiai_20" not in st.session_state:
#     st.session_state["tiai_20"] = None
# if "tiai_20_index" not in st.session_state:
#     st.session_state["tiai_20_index"] = None
#
# def set_new_index_tiai_1_value():
#     st.session_state.tiai_1 = st.session_state.key_tiai_1
# def set_new_index_tiai_2_value():
#     st.session_state.tiai_2 = st.session_state.key_tiai_2
# def set_new_index_tiai_3_value():
#     st.session_state.tiai_3 = st.session_state.key_tiai_3
# def set_new_index_tiai_4_value():
#     st.session_state.tiai_4 = st.session_state.key_tiai_4
# def set_new_index_tiai_5_value():
#     st.session_state.tiai_5 = st.session_state.key_tiai_5
# def set_new_index_tiai_6_value():
#     st.session_state.tiai_6 = st.session_state.key_tiai_6
# def set_new_index_tiai_7_value():
#     st.session_state.tiai_7 = st.session_state.key_tiai_7
# def set_new_index_tiai_8_value():
#     st.session_state.tiai_8 = st.session_state.key_tiai_8
# def set_new_index_tiai_9_value():
#     st.session_state.tiai_9 = st.session_state.key_tiai_9
# def set_new_index_tiai_10_value():
#     st.session_state.tiai_10 = st.session_state.key_tiai_10
# def set_new_index_tiai_11_value():
#     st.session_state.tiai_11 = st.session_state.key_tiai_11
# def set_new_index_tiai_12_value():
#     st.session_state.tiai_12 = st.session_state.key_tiai_12
# def set_new_index_tiai_13_value():
#     st.session_state.tiai_13 = st.session_state.key_tiai_13
# def set_new_index_tiai_14_value():
#     st.session_state.tiai_14 = st.session_state.key_tiai_14
# def set_new_index_tiai_15_value():
#     st.session_state.tiai_15 = st.session_state.key_tiai_15
# def set_new_index_tiai_16_value():
#     st.session_state.tiai_16 = st.session_state.key_tiai_16
# def set_new_index_tiai_17_value():
#     st.session_state.tiai_17 = st.session_state.key_tiai_17
# def set_new_index_tiai_18_value():
#     st.session_state.tiai_18 = st.session_state.key_tiai_18
# def set_new_index_tiai_19_value():
#     st.session_state.tiai_19 = st.session_state.key_tiai_19
# def set_new_index_tiai_20_value():
#     st.session_state.tiai_20 = st.session_state.key_tiai_20
#
# #Question 1
# tiai_1_options = ["Strongly approve", "Approve", "Indifferent", "Disapprove", "Strongly disapprove"]
# with st.container(border=True):
#     if st.session_state.tiai_1 is None:
#         index_variable_tiai_1 = None
#     else:
#         index_variable_tiai_1 = tiai_1_options.index(st.session_state.tiai_1)
#     col5, col6 = st.columns([4, 10], vertical_alignment="bottom")
#     with col5:
#         st.write("How would you describe your attitude towards Artificial Intelligene (AI) and its applications?")
#     with col6:
#         st.session_state.tiai_1 = st.radio(
#             label="5 = strongly approve; 1 = strongly disapprove",
#             # captions=["Not true for me", "", "Sometimes true for me", "", "Very true for me" ],
#             options=tiai_1_options,
#             index=index_variable_tiai_1,
#             key="key_tiai_1",
#             label_visibility="collapsed",
#             horizontal=True,
#             on_change=set_new_index_tiai_1_value
#         )
#
# #Question 2
# def assertion_values(text, key_variable):
#     if st.session_state[key_variable] is None:
#         index_variable = None
#     else:
#         index_variable = tiai_1_options.index(st.session_state[key_variable])
#
#     def set_new_index_value():
#         st.session_state[key_variable] = st.session_state["key_"+key_variable]
#
#     with st.container(border=True):
#         col5, col6 = st.columns([4, 10], vertical_alignment="bottom")
#         with col5:
#             st.write(text)
#         with col6:
#             values = st.radio(
#                 label="0 = Not true for me --------------- 2 = Sometimes true for me ------------------------ 4 = Very true for me",
#                 #captions=["Not true for me", "", "Sometimes true for me", "", "Very true for me" ],
#                 options=tiai_1_options,
#                 index=index_variable,
#                 key=("key_"+key_variable),
#                 label_visibility="collapsed",
#                 horizontal=True,
#                 on_change=set_new_index_value
#             )
#     return values
#
# with st.container(border=True):
#     st.write("How would you describe your attitude towards the use of AI in the following sectors?")
#     st.session_state.tiai_2 = assertion_values(text="Healthcare (e.g. diagnostic support, personalised medicine).", key_variable="tiai_2")
#     st.session_state.tiai_3 = assertion_values(text="Insurance (e.g. fraud detection, personalzed risk assessment).", key_variable="tiai_3")
#     st.session_state.tiai_4 = assertion_values(text="Agriculture (e.g. robotic harvesting, crop optimization).", key_variable="tiai_4")
#     st.session_state.tiai_5 = assertion_values(text="Finance (e.g. fraud detection, loan decision support systems).", key_variable="tiai_5")
#     st.session_state.tiai_6 = assertion_values(text="Military (e.g. automated weapons, cybersecurity for data protection).", key_variable="tiai_6")
#     st.session_state.tiai_7 = assertion_values(text="Law enforcement (e.g. predictive policing to forecast areas where crime is likely and dispatch police units, face recognition in public places).", key_variable="tiai_7")
#     st.session_state.tiai_8 = assertion_values(text="Environmental (e.g. climate prediction, energy harvesting forecast).", key_variable="tiai_8")
#     st.session_state.tiai_9 = assertion_values(text="Transportation (e.g. self-driving vehicles).", key_variable="tiai_9")
#     st.session_state.tiai_10 = assertion_values(text="Manufacturing industry (e.g. demand forecasting, robotics).", key_variable="tiai_10")
#     st.session_state.tiai_11 = assertion_values(text="Human resource management (e.g. CV screening, workforce planning).", key_variable="tiai_11")
#
# #Question 3
# with st.container(border=True):
#     if st.session_state.tiai_12 is None:
#         index_variable_tiai_12 = None
#     else:
#         index_variable_tiai_12 = tiai_1_options.index(st.session_state.tiai_12)
#     col5, col6 = st.columns([4, 10], vertical_alignment="center")
#     with col5:
#         st.write("Imagine that you are applying for a job in a large company and the recruitment process consists of two steps. The first step is based on an AI software which scans your resume and your answers to a set of questions on strategic competencies. The software assigns you a score which is used to select those candidates who can move on to the second stage (the interview). The company claims that the software makes the process faster and more objective. Also, the company says that the data is anonymised, and no personal information is used. To what extent would you feel comfortable or uncomfortable with this process?")
#     with col6:
#         st.session_state.tiai_12 = st.radio(
#             label="5 = strongly approve; 1 = strongly disapprove",
#             # captions=["Not true for me", "", "Sometimes true for me", "", "Very true for me" ],
#             options=tiai_1_options,
#             index=index_variable_tiai_12,
#             key="key_tiai_12",
#             label_visibility="collapsed",
#             horizontal=True,
#             on_change=set_new_index_tiai_12_value
#         )
#
# #Question 4
# with st.container(border=True):
#     if st.session_state.tiai_13 is None:
#         index_variable_tiai_13 = None
#     else:
#         index_variable_tiai_13 = tiai_1_options.index(st.session_state.tiai_13)
#     col5, col6 = st.columns([4, 10], vertical_alignment="center")
#     with col5:
#         st.write("Imagine that you are looking for a smart meter to reduce energy consumption in your house, cut the cost of utilities, and adopt a more sustainable lifestyle. You are offered a smart meter that uses AI to analyse home energy consumption and make recommendations for more efficient usage. Among functionalities, this system can give you the opportunity to receive personalised offers from energy suppliers which can help you save money. The company producing the smart meter says that your data is anonymised, and no personal information is shared with third parties without your consent. To what extent would you feel comfortable or uncomfortable with this application?")
#     with col6:
#         st.session_state.tiai_13 = st.radio(
#             label="5 = strongly approve; 1 = strongly disapprove",
#             # captions=["Not true for me", "", "Sometimes true for me", "", "Very true for me" ],
#             options=tiai_1_options,
#             index=index_variable_tiai_13,
#             key="key_tiai_13",
#             label_visibility="collapsed",
#             horizontal=True,
#             on_change=set_new_index_tiai_13_value
#         )
#
# #Question 5
# with st.container(border=True):
#     st.subheader("With respect to the previous scenarios, which of the following aspects should an organisation developing or using AI consider more? Please select three items and rank them.")
#     original_items = [
#         {"header": "Aspects", "items": [
#             "Security and accurate results.",
#             "Fair treatment and equitable access to the AI application for all members of society.",
#             "Privacy and data protection.",
#             "Human supervision over the AI outcome and process.",
#             "Clear communication about the AI application's purpose and limitations.",
#             "Risk management and identification of responsibility.",
#             "Societal and environmental impact of the AI application."
#         ]},
#         {"header": "Sorted According to Preference", "items": []}
#     ]
#     sorted_items = sort_items(original_items, multi_containers=True)
#     if len(sorted_items[1]["items"]) < 3:
#         st.warning("Please make sure to pick 3 aspects and sort them according to your preferences.")
#
# #Question 6
# tiai_6_options = ["Strongly agree", "Agree", "Neutral", "Disagree", "Strongly disagree"]
# with st.container(border=True):
#     if st.session_state.tiai_14 is None:
#         index_variable_tiai_14 = None
#     else:
#         index_variable_tiai_14 = tiai_6_options.index(st.session_state.tiai_14)
#     col5, col6 = st.columns([4, 10], vertical_alignment="bottom")
#     with col5:
#         st.write("To what extent do you agree that having a better education on what AI is, as well as its current and future uses, would improve your trust in it?")
#     with col6:
#         st.session_state.tiai_14 = st.radio(
#             label="5 = strongly approve; 1 = strongly disapprove",
#             # captions=["Not true for me", "", "Sometimes true for me", "", "Very true for me" ],
#             options=tiai_6_options,
#             index=index_variable_tiai_14,
#             key="key_tiai_14",
#             label_visibility="collapsed",
#             horizontal=True,
#             on_change=set_new_index_tiai_14_value
#         )
#
# #Question 8
# tiai_8_options = ["A lot", "Somewhat", "So and so", "Not so much", "Not at all"]
# def assertion_values_2(text, key_variable):
#     if st.session_state[key_variable] is None:
#         index_variable = None
#     else:
#         index_variable = tiai_8_options.index(st.session_state[key_variable])
#
#     def set_new_index_value():
#         st.session_state[key_variable] = st.session_state["key_"+key_variable]
#
#     col5, col6 = st.columns([4, 10], vertical_alignment="bottom")
#     with col5:
#         st.write(text)
#     with col6:
#         values = st.radio(
#             label="0 = Not true for me --------------- 2 = Sometimes true for me ------------------------ 4 = Very true for me",
#             #captions=["Not true for me", "", "Sometimes true for me", "", "Very true for me" ],
#             options=tiai_8_options,
#             index=index_variable,
#             key=("key_"+key_variable),
#             label_visibility="collapsed",
#             horizontal=True,
#             on_change=set_new_index_value
#         )
#     return values
#
# with st.container(border=True):
#     st.write("How much do you trust the following entities in ensuring that AI is in the best interest of the public?")
#     st.session_state.tiai_15 = assertion_values(text="National Governments and public authorities.", key_variable="tiai_15")
#     st.session_state.tiai_16 = assertion_values(text="Universities and research centres.", key_variable="tiai_16")
#     st.session_state.tiai_17 = assertion_values(text="Consumer associations, trade unions and civil society organisations.", key_variable="tiai_17")
#     st.session_state.tiai_18 = assertion_values(text="Tech companies developing AI products.", key_variable="tiai_18")
#     st.session_state.tiai_19 = assertion_values(text="Social media companies.", key_variable="tiai_19")
#
# #Question 9
# with st.container(border=True):
#     if st.session_state.tiai_20 is None:
#         index_variable_tiai_20 = None
#     else:
#         index_variable_tiai_20 = tiai_6_options.index(st.session_state.tiai_14)
#     st.write("If you were to describe your digital skills, how would you define yourself:")
#     st.session_state.tiai_20 = st.selectbox(
#         label="no label needed",
#         options=[
#             "Very expert: I am sure of my digital skills, I am always attentive to innovation, I have no difficulty in moving in the digital world for everything I need, and I am interested in.",
#             "Expert: I am quite sure of my digital skills, I try to exploit the potential it can ofer and to be updated on the news.",
#             "Enough expert: I'm not entirely sure of my skills, but I manage to do the best I can when I need to do something online and I try to learn new skills when I need them.",
#             "Not very expert: I'm not sure of my skills and I have to get someone to help me with new things I don't understand.",
#             "Not at all expert: I use digital tools only if it is strictly necessary (e.g. email, messages)"
#         ],
#         index=index_variable_tiai_20,
#
#     )
#
# c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
# with c_end_left:
#     st.page_link("pages/regulatory_focus.py", label="Previous Page", icon=":material/arrow_back:")
#     # st.page_link("pages/scenario_5.py", label="Previous Page", icon=":material/arrow_back:")
# with c_end_right:
#     if (st.session_state.tiai_1 is not None and st.session_state.tiai_2 is not None and st.session_state.tiai_3 is not None
#     and st.session_state.tiai_4 is not None and st.session_state.tiai_5 is not None and st.session_state.tiai_6 is not None
#     and st.session_state.tiai_7 is not None and st.session_state.tiai_8 is not None and st.session_state.tiai_9 is not None
#     and st.session_state.tiai_10 is not None and st.session_state.tiai_11 is not None and st.session_state.tiai_12 is not None
#     and st.session_state.tiai_13 is not None and st.session_state.tiai_14 is not None and st.session_state.tiai_15 is not None
#     and st.session_state.tiai_16 is not None and st.session_state.tiai_17 is not None and st.session_state.tiai_18 is not None
#     and st.session_state.tiai_19 is not None and st.session_state.tiai_20 is not None and len(sorted_items[1]["items"]) >= 3):
#         st.page_link("pages/start_main_part.py", label="Next Page", icon=":material/arrow_forward:")