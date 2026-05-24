import streamlit as st
import LLM_Generators.gold_standard as gold_standard
import LLM_Generators.few_shot_cot_sc as few_shot_cot_sc
import LLM_Generators.Calling_Fine_Tuned_Models as fine_tuned
import rag_sentence
import LLM_Generators.extract_user_message as extract_user_message


def _create_information(context_data):
    user_data = (
        f"The user is between {context_data[0]['age']} years old, {context_data[0]['gender']} with a "
        f"{context_data[0]['job situation']} job. "
        f"Their contextual features are the following: "
    )

    storyline_new = (
        f"Today - {context_data[0]['day']}, between {context_data[0]['time']}, I am {context_data[0]['user status']}, and the weather is {context_data[0]['weather']}. "
        f"I am mainly engaging in {context_data[0]['activity']} at {context_data[0]['location']}, spending a significant amount of time {context_data[0]['position of body']}. My last interaction with my phone is {context_data[0]['last interaction']} ago. "
        f"I am feeling {context_data[0]['mood_valence']}% well, {context_data[0]['energetic_arousal']}% energetic, {context_data[0]['affect_calmness']}% calm, {context_data[0]['stress']}% stressed, and {context_data[0]['locus_of_control']}% in control of what is happening. "
        f"Nearby locations accessible included: {context_data[0]['close_locations']}. "
        f"Later that day, I plan the following: {context_data[0]['calendar entries']}. "
        f"Independent of my circumstances, I am {context_data[0]['motivation_pa']}% motivated to engage in physical activity. My circumstances are {context_data[0]['barrier_pa']}% favourable of physical activity. "
        f"I {context_data[0]['pa_scheduled_today']} intended a physical activity for today{context_data[0]['pa_scheduled_today_yes']}{context_data[0]['pa_planning_specifity_scheduled_today']}. "
        f"I {context_data[0]['pa_performed_today']} complete some physical activity today{context_data[0]['pa_performed_today_yes']}. "
        f"For tomorrow - {context_data[0]['next_day_text']} - I {context_data[0]['pa_scheduled_tomorrow']} intended to be physically active{context_data[0]['pa_scheduled_tomorrow_yes']}{context_data[0]['pa_planning_specifity_scheduled_tomorrow']}."
    )

    storyline_old = (
        f"It's {context_data[0]['day']} and the time is {context_data[0]['time']}. "
        f"Looking outside, I notice the weather is {context_data[0]['weather']}. "
        f"Currently, I am {context_data[0]['user status']} (status: at work/on vacation/etc.) "
        f"and {context_data[0]['activity']} (current activity). "
        f"On a scale from 0-100, my mood today is {context_data[0]['mood']}, "
        f"and my stress level is {context_data[0]['stress']}. "
        f"The last time I checked my smartphone was {context_data[0]['last interaction']} (hours/minutes ago). "
        f"When I look at my calendar for today, I see these entries: {context_data[0]['calender_entries']}. "
        f"From where I am, I can easily reach these places within a kilometer: {context_data[0]['close_locations']} (list nearby locations). "
        f"Regarding physical activity today, my motivation level is {context_data[0]['motivation_pa']} (0-100), "
        f"while my perceived barriers are {context_data[0]['barrier_pa']} (0-100). "
        f"I {context_data[0]['pa_scheduled_today']} (had/didn't have) physical activity scheduled for today, "
        f"and I {context_data[0]['pa_performed_today']} (did/didn't complete) the planned activity. "
        f"During the day, I {context_data[0]['jitai_sent_today']} (did/didn't) receive any pa intervention or support. "
        f"Looking ahead to tomorrow, I {context_data[0]['pa_scheduled_tomorrow']} (have/don't have) physical activity planned. "
        f"Thinking about my wellness, my sleep quality last night was {context_data[0]['sleep quality']} (0-100). "
        f"Considering my scheduled activities for today, my confidence in completing them under the current circumstances is {context_data[0]['self_efficacy']} (0-100). "
    )

    bfpt_information_new = (
        f"My big five personality traits are the following: I am {context_data[0]['extraversion']}; "
        f"{context_data[0]['agreeableness']}; {context_data[0]['conscientiousness']}; {context_data[0]['neuroticism']}; {context_data[0]['openness']}. "
    )

    bfpt_information_old = (
        f"My big five personality traits are the following: reserved {context_data[0]['reserved']}, trusting {context_data[0]['generally trusting']}, "
        f"lazy {context_data[0]['tends to be lazy']}, handles stress well {context_data[0]['relaxed, handles stress well']}, "
        f"few artistic interests {context_data[0]['few artistic interests']}, outgoing/sociable {context_data[0]['outgoing, sociable']}, "
        f"finds faults with others {context_data[0]['tends to find fault with others']}, does a thorough job {context_data[0]['does a thorough job']}, "
        f"gets nervous easily {context_data[0]['gets nervous easily']}, has an active imagination {context_data[0]['has an active imagination']}, "
        f"is considerate and kind to almost everyone {context_data[0]['considerate and kind to almost everyone']}."
    )



    scenario_data_without_bfpt_old = user_data + " " + storyline_old
    scenario_data_without_bfpt_new = user_data + " " + storyline_new

    scenario_data_with_bfpt_old = user_data + " " + storyline_old + " " + bfpt_information_old
    scenario_data_with_bfpt_new = user_data + " " + storyline_new + " " + bfpt_information_new

    return scenario_data_without_bfpt_old, scenario_data_with_bfpt_old, scenario_data_without_bfpt_new, scenario_data_with_bfpt_new

def generate_jitais(context_data):
    # creating the messages for further analysis -> LLMs
    scenario_data_without_bfpt_old, scenario_data_with_bfpt_old, scenario_data_without_bfpt_new, scenario_data_with_bfpt_new = _create_information(context_data)

    original_gold_standard_without_bfpt = gold_standard.call_gold_standard(scenario_data_without_bfpt_new)
    original_gold_standard_with_bfpt = gold_standard.call_gold_standard(scenario_data_with_bfpt_new)

    original_cot_sc_without_bfpt, original_cot_sc_without_bfpt_examples = few_shot_cot_sc.few_shot_without_BFPT(scenario_data_without_bfpt_new)
    original_cot_sc_with_bfpt, original_cot_sc_with_bfpt_examples = few_shot_cot_sc.few_shot_with_BFPT(scenario_data_with_bfpt_new)

    original_fine_tuned_without_bfpt, original_fine_tuned_with_bfpt = fine_tuned.call_fine_tuned_models(scenario_data_without_bfpt_new, scenario_data_with_bfpt_new)

    # RAG uses the old prompt format because that is what the pre-computed embeddings were built from
    original_rag_without_bfpt, original_rag_with_bfpt, original_rag_without_bfpt_examples, original_rag_with_bfpt_examples = rag_sentence.get_ragging(scenario_data_without_bfpt_old, scenario_data_with_bfpt_old, scenario_data_without_bfpt_new, scenario_data_with_bfpt_new)

    original_jitai_list = [original_gold_standard_without_bfpt, original_gold_standard_with_bfpt, original_cot_sc_without_bfpt, original_cot_sc_with_bfpt,
                  original_fine_tuned_without_bfpt, original_fine_tuned_with_bfpt, original_rag_without_bfpt, original_rag_with_bfpt]

    jitai_examples_list = [original_cot_sc_without_bfpt_examples, original_cot_sc_with_bfpt_examples, original_rag_without_bfpt_examples, original_rag_with_bfpt_examples]

    jitai_list = [extract_user_message.extract_user_message(j) for j in original_jitai_list]

    return original_jitai_list, jitai_list, jitai_examples_list

if __name__ == "__main__":
    data_dict = [{
        "reserved": st.session_state.bfi_1,
        "generally trusting": st.session_state.bfi_2,
        "tends to be lazy": st.session_state.bfi_3,
        "relaxed, handles stress well": st.session_state.bfi_4,
        "few artistic interests": st.session_state.bfi_5,
        "outgoing, sociable": st.session_state.bfi_6,
        "tends to find fault with others": st.session_state.bfi_7,
        "does a thorough job": st.session_state.bfi_8,
        "gets nervous easily": st.session_state.bfi_9,
        "has an active imagination": st.session_state.bfi_10,
        "considerate and kind to almost everyone": st.session_state.bfi_11,
        "extraversion": st.session_state.extraversion,
        "agreeableness": st.session_state.agreeableness,
        "conscientiousness": st.session_state.conscientiousness,
        "neuroticism": st.session_state.neuroticism,
        "openness": st.session_state.openness,
        "age": st.session_state.age_option,
        "gender": st.session_state.gender_option,
        "job situation": st.session_state.job_situation,

        "day": st.session_state.day_text,
        "time": st.session_state.time_text,
        "user status": st.session_state.user_status,
        "weather": st.session_state.weather,
        "activity": st.session_state.activity,
        "location": st.session_state.location,
        "position of body": st.session_state.position_of_body,
        "last interaction": st.session_state.last_interaction,
        "mood_valence": st.session_state.mood_valence,
        "energetic_arousal": st.session_state.energetic_arousal,
        "affect_calmness": st.session_state.affect_calmness,
        "stress": st.session_state.stress,
        "locus_of_control": st.session_state.locus_of_control,
        "close_locations": st.session_state.close_locations,
        "calender entries": st.session_state.calendar_entries,
        "motivation_pa": st.session_state.motivation_pa,
        "barrier_pa": st.session_state.barrier_pa,
        "pa_scheduled_today": st.session_state.pa_scheduled_today,
        "pa_scheduled_today_yes": st.session_state.pa_scheduled_today_yes,
        "pa_planning_specifity_scheduled_today": st.session_state.pa_planning_specifity_scheduled_today,
        "pa_performed_today": st.session_state.pa_performed_today,
        "pa_performed_today_yes": st.session_state.pa_performed_today_yes,
        "pa_scheduled_tomorrow": st.session_state.pa_scheduled_tomorrow,
        "pa_scheduled_tomorrow_yes": st.session_state.pa_scheduled_tomorrow_yes,
        "pa_planning_specifity_scheduled_tomorrow": st.session_state.pa_planning_specifity_scheduled_tomorrow,
    }]

    generate_jitais(data_dict)