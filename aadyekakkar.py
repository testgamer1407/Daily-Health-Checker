import streamlit as st

# 1. Create the application title
st.title("Daily Health Checker")
st.write("Welcome! Enter your daily habits below to check your wellness score.")

# 2 & 3. Collect user information using Streamlit input widgets
name = st.text_input("Enter your Name:")
age = st.number_input("Enter your Age (in years):", min_value=5, max_value=100, value=14)
sleep = st.number_input("Hours of sleep per day:", min_value=0.0, max_value=24.0, value=8.0)
water = st.number_input("Glasses of water consumed today:", min_value=0, max_value=20, value=8)
exercise = st.number_input("Daily exercise duration (in minutes):", min_value=0, max_value=300, value=30)
screen_time = st.number_input("Daily screen time (in hours):", min_value=0.0, max_value=24.0, value=2.0)
mood = st.selectbox("How is your mood today?", ["Happy", "Energetic", "Sad", "Stressed"])

# Button to analyse the health data
if st.button("Check My Health"):
    if name == "":
        st.warning("Please enter your name first!")
    else:
        st.subheader("Daily Health Summary for " + name)
        st.write("Age:", age, "years | Current Mood:", mood)
        
        # Variable to keep track of the Daily Wellness Score out of 100
        score = 0
        
        st.subheader("Personalised Lifestyle Feedback & Recommendations")
        
        # 4 & 5. Apply if-elif-else statements to analyse inputs and calculate score
        
        # --- 1. Sleep Analysis (Max 25 points) ---
        if sleep >= 7 and sleep <= 9:
            st.success("Sleep: Great job! You are getting 7 to 9 hours of healthy sleep.")
            score = score + 25
        elif sleep < 7:
            st.warning("Sleep: You are not sleeping enough. Recommendation: Try to sleep at least 7-8 hours.")
            score = score + 10
        else:
            st.info("Sleep: You are sleeping more than 9 hours. Recommendation: Stick to an 8-hour schedule.")
            score = score + 15

        # --- 2. Water Analysis (Max 25 points) ---
        if water >= 8:
            st.success("Hydration: Excellent! You are drinking enough water today.")
            score = score + 25
        elif water >= 5:
            st.info("Hydration: Good effort, but try to drink at least 8 glasses of water daily.")
            score = score + 15
        else:
            st.warning("Hydration: Very low water intake! Recommendation: Carry a water bottle and drink more water.")
            score = score + 5

        # --- 3. Exercise Analysis (Max 25 points) ---
        if exercise >= 30:
            st.success("Exercise: Awesome! You are staying active with 30+ minutes of exercise.")
            score = score + 25
        elif exercise >= 15:
            st.info("Exercise: Good start! Recommendation: Increase your physical activity to 30 minutes daily.")
            score = score + 15
        else:
            st.warning("Exercise: Too little physical activity. Recommendation: Go for a brisk walk, cycle, or play a sport.")
            score = score + 5

        # --- 4. Screen Time Analysis (Max 15 points) ---
        if screen_time <= 2:
            st.success("Screen Time: Well controlled! Keeping screen time under 2 hours protects your eyes.")
            score = score + 15
        elif screen_time <= 4:
            st.info("Screen Time: Moderate screen time. Recommendation: Take breaks every 30 minutes.")
            score = score + 10
        else:
            st.warning("Screen Time: High screen time! Recommendation: Reduce mobile/TV use before bedtime.")
            score = score + 5

        # --- 5. Mood Analysis (Max 10 points) ---
        if mood == "Happy" or mood == "Energetic":
            st.success("Mood: It is wonderful that you feel " + mood + " today! Keep spreading positivity.")
            score = score + 10
        else:
            st.info("Mood: You are feeling " + mood + ". Recommendation: Listen to music, talk to family, or take deep breaths.")
            score = score + 5

        # --- Challenge Task: Wellness Score and Progress Bar ---
        st.subheader("Your Daily Wellness Score")
        st.write("Total Score:", score, "/ 100")
        st.progress(score)

        # Final Overall Message based on total score
        if score >= 80:
            st.success("Overall Status: Super Healthy Lifestyle! Keep up the amazing habits.")
        elif score >= 50:
            st.info("Overall Status: Good Lifestyle, but making a few small changes will make you healthier.")
        else:
            st.warning("Overall Status: Needs Improvement! Follow the recommendations above for a healthier routine.")

# Challenge Task: Button to reset or clear inputs
if st.button("Reset / Clear"):
    st.info("Tip: Press 'R' on your keyboard or refresh the browser page to reset all inputs to default.")
    st.rerun()
