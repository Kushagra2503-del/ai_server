import streamlit as st
import joblib
import pandas as pd

# --- 1. THE BRAIN ---
model = joblib.load("model.pkl")

# --- 2. BRANDING ---
st.set_page_config(page_title="VizDoom AI Predictor", page_icon="👹")
st.title("👹 VizDoom Combat Predictor")
st.write("This AI analyzes combat data to predict an agent's success rate.")

# --- 3. INPUTS ---
level = st.slider("Select Combat Tier (Level)", min_value=1, max_value=100, value=1)
hours = st.number_input("Agent Training Hours", min_value=1, max_value=1000, value=1000)

# --- 4. PREDICTION LOGIC ---
if st.button("Calculate Probability of Survival"):
    # Create the data for the model
    new_data = pd.DataFrame([[level, hours]], columns=['level', 'hours'])

    # Get exact prediction AND the AI's confidence level (probability)
    prediction = model.predict(new_data)[0]
    probabilities = model.predict_proba(new_data)[0]
    win_prob = probabilities[1]  # The probability of class '1' (Victory)

    if prediction == 1:
        st.success(f"Outcome: VICTORY 🏆 - The agent is likely to clear the map.")
        st.balloons()
    else:
        st.error(f"Outcome: DEFEAT 💀 - The agent is statistically likely to perish.")

    # --- 5. VISUALIZATIONS ---
    st.divider()
    st.subheader("📊 AI Confidence & Analysis")

    # Visualization 1: Confidence Progress Bar
    st.write(f"**AI Confidence of Winning:** {win_prob * 100:.1f}%")
    st.progress(float(win_prob))

    # Visualization 2: The Victory Zone Graph
    st.write("### The Victory Zone Boundary")
    st.write(
        "The chart below shows the minimum hours needed to secure a win across different combat tiers based on the AI's training data.")

    # Generate the line data mathematically
    levels = range(1, 101)
    safe_hours = [lvl * 3 for lvl in levels]  # The logic we taught the AI

    # Plot it using Streamlit's native line chart
    chart_data = pd.DataFrame({
        'Minimum Hours Needed to Win': safe_hours,
    }, index=levels)

    st.line_chart(chart_data)
    st.caption("X-axis: Combat Tier (Level) | Y-axis: Training Hours")

    # --- 6. AGENT GAMEPLAY SHOWCASE ---
    st.divider()
    st.subheader("🎥 Watch the AI in Action")
    st.write("This is actual footage of my trained PPO agent navigating the VizDoom environment using raw pixel data.")

    # Streamlit will look for the video file in your repository and play it!
    try:
        st.video("doom_gameplay_long.mp4")  # Make sure this matches your exact file name
    except Exception as e:
        st.info("Video file loading... Please ensure the mp4 is in the GitHub repository.")