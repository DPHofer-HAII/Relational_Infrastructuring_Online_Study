import LLM_functions

# Example data
age = "36-year-old"
gender = "male"
job_situation = "full-time"
day_of_week = "moodonday"
time_of_day = "10:00"
weather = "rainy"
user_status = "sassy"
current_activity = "work"
mood = "50"
stress_level = "50"
last_interaction = "20 minutes"
calender_entries = "none"
close_locations = "park, bus station"
motivation_pa = "30"  # Look at it again!
barrier_pa = "70"
pa_scheduled_today = "running in a circle"
pa_performed_today = "none"
jitai_sent_today = "yes"
pa_scheduled_tomorrow = "no"
last_nights_sleep_quality = "30"
self_efficacy = "10"
reserved = "agree strongly"
trusting = "agree a little"
lazy = "disagree strongly"
handles_stress_well = "agree a little"
few_artistic_interests = "agree a little"
outgoing_sociable = "disagree a little"
find_faults_with_others = "agree strongly"
does_a_thorough_job = "agree strongly"
gets_nervous_easily = "disagree a little"
active_imagination = "agree strongly"
kind_to_almost_everyone = "agree strongly"

context_data = {"age": age, "gender": gender, "job_situation": job_situation, "reserved": reserved,
                "trusting": trusting,
                "lazy": lazy, "handles_stress_well": handles_stress_well, "calendar_entries": calender_entries,
                "few_artistic_interests": few_artistic_interests, "outgoing_sociable": outgoing_sociable,
                "find_faults_with_others": find_faults_with_others,
                "does_a_thorough_job": does_a_thorough_job, "gets_nervous_easily": gets_nervous_easily,
                "active_imagination": active_imagination,
                "kind_to_almost_everyone": kind_to_almost_everyone, "day_of_week": day_of_week,
                "time_of_day": time_of_day,
                "user_status": user_status, "close_locations": close_locations, "weather": weather,
                "current_activity": current_activity,
                "mood": mood, "stress_level": stress_level, "self_efficacy": self_efficacy,
                "last_interaction": last_interaction,
                "last_nights_sleep_quality": last_nights_sleep_quality, "motivation_pa": motivation_pa,
                "barrier_pa": barrier_pa,
                "pa_scheduled_today": pa_scheduled_today, "pa_performed_today": pa_performed_today,
                "jitai_sent_today": jitai_sent_today,
                "pa_scheduled_tomorrow": pa_scheduled_tomorrow}

original_jitai, jitai_list = LLM_functions.generate_jitais(context_data)

for i in range(len(original_jitai)):
    print(original_jitai[i])
    print(jitai_list[i])