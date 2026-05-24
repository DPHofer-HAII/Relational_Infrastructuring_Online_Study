import streamlit as st

st.header("Exercise Regulations Questionnaire (BREQ-3)")

if "breq_1" not in st.session_state:
    st.session_state["breq_1"] = None
if "breq_1_index" not in st.session_state:
    st.session_state["breq_1_index"] = None

if "breq_2" not in st.session_state:
    st.session_state["breq_2"] = None
if "breq_2_index" not in st.session_state:
    st.session_state["breq_2_index"] = None

if "breq_3" not in st.session_state:
    st.session_state["breq_3"] = None
if "breq_3_index" not in st.session_state:
    st.session_state["breq_3_index"] = None

if "breq_4" not in st.session_state:
    st.session_state["breq_4"] = None
if "breq_4_index" not in st.session_state:
    st.session_state["breq_4_index"] = None

if "breq_5" not in st.session_state:
    st.session_state["breq_5"] = None
if "breq_5_index" not in st.session_state:
    st.session_state["breq_5_index"] = None

if "breq_6" not in st.session_state:
    st.session_state["breq_6"] = None
if "breq_6_index" not in st.session_state:
    st.session_state["breq_6_index"] = None

if "breq_7" not in st.session_state:
    st.session_state["breq_7"] = None
if "breq_7_index" not in st.session_state:
    st.session_state["breq_7_index"] = None

if "breq_8" not in st.session_state:
    st.session_state["breq_8"] = None
if "breq_8_index" not in st.session_state:
    st.session_state["breq_8_index"] = None

if "breq_9" not in st.session_state:
    st.session_state["breq_9"] = None
if "breq_9_index" not in st.session_state:
    st.session_state["breq_9_index"] = None

if "breq_10" not in st.session_state:
    st.session_state["breq_10"] = None
if "breq_10_index" not in st.session_state:
    st.session_state["breq_10_index"] = None

if "breq_11" not in st.session_state:
    st.session_state["breq_11"] = None
if "breq_11_index" not in st.session_state:
    st.session_state["breq_11_index"] = None

if "breq_12" not in st.session_state:
    st.session_state["breq_12"] = None
if "breq_12_index" not in st.session_state:
    st.session_state["breq_12_index"] = None

if "breq_13" not in st.session_state:
    st.session_state["breq_13"] = None
if "breq_13_index" not in st.session_state:
    st.session_state["breq_13_index"] = None

if "breq_14" not in st.session_state:
    st.session_state["breq_14"] = None
if "breq_14_index" not in st.session_state:
    st.session_state["breq_14_index"] = None

if "breq_15" not in st.session_state:
    st.session_state["breq_15"] = None
if "breq_15_index" not in st.session_state:
    st.session_state["breq_15_index"] = None

if "breq_16" not in st.session_state:
    st.session_state["breq_16"] = None
if "breq_16_index" not in st.session_state:
    st.session_state["breq_16_index"] = None

if "breq_17" not in st.session_state:
    st.session_state["breq_17"] = None
if "breq_17_index" not in st.session_state:
    st.session_state["breq_17_index"] = None

if "breq_18" not in st.session_state:
    st.session_state["breq_18"] = None
if "breq_18_index" not in st.session_state:
    st.session_state["breq_18_index"] = None

if "breq_19" not in st.session_state:
    st.session_state["breq_19"] = None
if "breq_19_index" not in st.session_state:
    st.session_state["breq_19_index"] = None

if "breq_20" not in st.session_state:
    st.session_state["breq_20"] = None
if "breq_20_index" not in st.session_state:
    st.session_state["breq_20_index"] = None

if "breq_21" not in st.session_state:
    st.session_state["breq_21"] = None
if "breq_21_index" not in st.session_state:
    st.session_state["breq_21_index"] = None

if "breq_22" not in st.session_state:
    st.session_state["breq_22"] = None
if "breq_22_index" not in st.session_state:
    st.session_state["breq_22_index"] = None

if "breq_23" not in st.session_state:
    st.session_state["breq_23"] = None
if "breq_23_index" not in st.session_state:
    st.session_state["breq_23_index"] = None

if "breq_24" not in st.session_state:
    st.session_state["breq_24"] = None
if "breq_24_index" not in st.session_state:
    st.session_state["breq_24_index"] = None

def set_new_index_breq_1_value():
    st.session_state.breq_1 = st.session_state.key_breq_1
def set_new_index_breq_2_value():
    st.session_state.breq_2 = st.session_state.key_breq_2
def set_new_index_breq_3_value():
    st.session_state.breq_3 = st.session_state.key_breq_3
def set_new_index_breq_4_value():
    st.session_state.breq_4 = st.session_state.key_breq_4
def set_new_index_breq_5_value():
    st.session_state.breq_5 = st.session_state.key_breq_5
def set_new_index_breq_6_value():
    st.session_state.breq_6 = st.session_state.key_breq_6
def set_new_index_breq_7_value():
    st.session_state.breq_7 = st.session_state.key_breq_7
def set_new_index_breq_8_value():
    st.session_state.breq_8 = st.session_state.key_breq_8
def set_new_index_breq_9_value():
    st.session_state.breq_9 = st.session_state.key_breq_9
def set_new_index_breq_10_value():
    st.session_state.breq_10 = st.session_state.key_breq_10
def set_new_index_breq_11_value():
    st.session_state.breq_11 = st.session_state.key_breq_11
def set_new_index_breq_12_value():
    st.session_state.breq_12 = st.session_state.key_breq_12
def set_new_index_breq_13_value():
    st.session_state.breq_13 = st.session_state.key_breq_13
def set_new_index_breq_14_value():
    st.session_state.breq_14 = st.session_state.key_breq_14
def set_new_index_breq_15_value():
    st.session_state.breq_15 = st.session_state.key_breq_15
def set_new_index_breq_16_value():
    st.session_state.breq_16 = st.session_state.key_breq_16
def set_new_index_breq_17_value():
    st.session_state.breq_17 = st.session_state.key_breq_17
def set_new_index_breq_18_value():
    st.session_state.breq_18 = st.session_state.key_breq_18
def set_new_index_breq_19_value():
    st.session_state.breq_19 = st.session_state.key_breq_19
def set_new_index_breq_20_value():
    st.session_state.breq_20 = st.session_state.key_breq_20
def set_new_index_breq_21_value():
    st.session_state.breq_21 = st.session_state.key_breq_21
def set_new_index_breq_22_value():
    st.session_state.breq_22 = st.session_state.key_breq_22
def set_new_index_breq_23_value():
    st.session_state.breq_23 = st.session_state.key_breq_23
def set_new_index_breq_24_value():
    st.session_state.breq_24 = st.session_state.key_breq_24

st.write(r'''$\textsf{\large Why do you engange in exercise? *}$''')
st.write("We are interested in the reasons underlying people's decisions to engage or not engage in physical exercise. Using the scale below, please indicate to what extent each of the following items is true for you.")
st.write("Please note that there are no right or wrong answers and no trick questions. We simply want to know how you personally feel about exercise. Your responses will be held in confidence and only used for our research purposes.")

#DOING THINGS!!!
def assertion_values(text, key_variable, visibility_of_label):
    if st.session_state[key_variable] is None:
        index_variable = None
    else:
        index_variable = int(st.session_state[key_variable])

    def set_new_index_value():
        st.session_state[key_variable] = st.session_state["key_"+key_variable]

    with st.container(border=True):
        # col5, col6 = st.columns([4, 10], vertical_alignment="bottom")
        # with col5:
        #     st.write(text)
        # with col6:
        #     values = st.radio(
        #         label="0 = Not true for me --------------- 2 = Sometimes true for me ------------------------ 4 = Very true for me",
        #         #captions=["Not true for me", "", "Sometimes true for me", "", "Very true for me" ],
        #         options=["0", "1", "2", "3", "4"],
        #         index=index_variable,
        #         key=("key_"+key_variable),
        #         label_visibility=visibility_of_label,
        #         horizontal=True,
        #         on_change=set_new_index_value
        #     )
        st.write(text)
        values = st.radio(
            label="0 = Not true for me --------------- 2 = Sometimes true for me ------------------------ 4 = Very true for me",
            #captions=["Not true for me", "", "Sometimes true for me", "", "Very true for me" ],
            options=["0", "1", "2", "3", "4"],
            index=index_variable,
            key=("key_"+key_variable),
            label_visibility=visibility_of_label,
            horizontal=True,
            on_change=set_new_index_value
        )


label_visibility_variable = "collapsed"
st.write("0 = Not true for me; 2 = Sometimes true for me; 4 = Very true for me")

assertion_values(text="It's important to me to exercise regularly *", key_variable="breq_1", visibility_of_label=label_visibility_variable)
assertion_values(text="I don't see why I should have to exercise *", key_variable="breq_2", visibility_of_label=label_visibility_variable)
assertion_values(text="I exercise because It's fun *", key_variable="breq_3", visibility_of_label=label_visibility_variable)
assertion_values(text="I feel guilty when I don't exercise *", key_variable="breq_4", visibility_of_label=label_visibility_variable)
assertion_values(text="I exercise because it is consistent with my life goals *", key_variable="breq_5", visibility_of_label=label_visibility_variable)
assertion_values(text="I exercise because other people say I should *", key_variable="breq_6", visibility_of_label=label_visibility_variable)
assertion_values(text="I value the benefits of exercise *", key_variable="breq_7", visibility_of_label=label_visibility_variable)
assertion_values(text="I can't see why I should bother exercising *", key_variable="breq_8", visibility_of_label=label_visibility_variable)
assertion_values(text="I enjoy my exercise sessions *", key_variable="breq_9", visibility_of_label=label_visibility_variable)
assertion_values(text="I feel ashamed when I miss an exercise session *", key_variable="breq_10", visibility_of_label=label_visibility_variable)
assertion_values(text="I consider exercise part of my identity *", key_variable="breq_11", visibility_of_label=label_visibility_variable)
assertion_values(text="I take part in exercise because my friends / family / partner say I should *", key_variable="breq_12", visibility_of_label=label_visibility_variable)
assertion_values(text="I think it is important to make the effort to exercise regularly *", key_variable="breq_13", visibility_of_label=label_visibility_variable)
assertion_values(text="I don't see the point in exercising *", key_variable="breq_14", visibility_of_label=label_visibility_variable)
assertion_values(text="I find exercise a pleasurable activity *", key_variable="breq_15", visibility_of_label=label_visibility_variable)
assertion_values(text="I feel like a failure when I haven't exercised in a while *", key_variable="breq_16", visibility_of_label=label_visibility_variable)
assertion_values(text="I consider exercise a fundamental part of who I am *", key_variable="breq_17", visibility_of_label=label_visibility_variable)
assertion_values(text="I exercise because others will not be pleased with me if I don't *", key_variable="breq_18", visibility_of_label=label_visibility_variable)
assertion_values(text="I get restless if I don't exercise regularly *", key_variable="breq_19", visibility_of_label=label_visibility_variable)
assertion_values(text="I think exercising is a waste of time *", key_variable="breq_20", visibility_of_label=label_visibility_variable)
assertion_values(text="I get pleasure and satisfaction from participating in exercise *", key_variable="breq_21", visibility_of_label=label_visibility_variable)
assertion_values(text="I would feel bad about myself if I was not making time to exercise *", key_variable="breq_22", visibility_of_label=label_visibility_variable)
assertion_values(text="I consider exercise consistent with my values *", key_variable="breq_23", visibility_of_label=label_visibility_variable)
assertion_values(text="I feel under pressure from my friends / family to exercise *", key_variable="breq_24", visibility_of_label=label_visibility_variable)

c_end_left, c_end_middle, c_end_right = st.columns([1, 5, 1])
with c_end_left:
    st.page_link("pages/socio_demographic_data.py", label="Previous Page", icon=":material/arrow_back:")
with (c_end_right):
    if (st.session_state.breq_1 is not None and st.session_state.breq_2 is not None and
        st.session_state.breq_3 is not None and st.session_state.breq_4 is not None and
        st.session_state.breq_5 is not None and st.session_state.breq_6 is not None and
        st.session_state.breq_7 is not None and st.session_state.breq_8 is not None and
        st.session_state.breq_9 is not None and st.session_state.breq_10 is not None and
        st.session_state.breq_11 is not None and st.session_state.breq_12 is not None and
        st.session_state.breq_13 is not None and st.session_state.breq_14 is not None and
        st.session_state.breq_15 is not None and st.session_state.breq_16 is not None and
        st.session_state.breq_17 is not None and st.session_state.breq_18 is not None and
        st.session_state.breq_19 is not None and st.session_state.breq_20 is not None and
        st.session_state.breq_21 is not None and st.session_state.breq_22 is not None and
        st.session_state.breq_23 is not None and st.session_state.breq_24 is not None
        ):
        st.page_link("pages/BFI-10.py", label="Next Page", icon=":material/arrow_forward:")
    #st.page_link("pages/BFI-10.py", label="Next Page", icon=":material/arrow_forward:")
#
st.write(r'''$\textsf{\footnotesize * Mandatory questions!}$''')