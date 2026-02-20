import streamlit as st
import requests

# --- 1. BRANDING & CONTEXT ---
st.set_page_config(page_title="VizDoom AI Predictor", page_icon="👹")
st.title("👹 VizDoom Combat Predictor")
st.write("This AI analyzes combat data from the VizDoom environment to predict an agent's success rate.")

with st.expander("🎮 About the VizDoom AI Model"):
    st.write("""
    **What game is this for?**
    This model specifically analyzes data from **VizDoom**, an AI research platform based on the classic game DOOM.

    **What do the numbers mean?**
    * **Player Level:** Represents the difficulty tier of the Doom environment (e.g., *'I'm Too Young to Die'* vs *'Nightmare'*).
    * **Total Hours:** Represents the training time the Deep Reinforcement Learning agent (PPO) has spent in the gym environment.
    """)

st.divider()

# --- 2. INPUTS WITH CONTEXT ---
level = st.slider("Select Combat Tier (Level)", min_value=1, max_value=100, value=18)
hours = st.number_input("Agent Training Hours", min_value=1, max_value=1000, value=50)

# --- 3. THE PREDICTION ---
if st.button("Calculate Probability of Survival"):
    api_url = "http://localhost:8000/predict"
    data = {"level": level, "hours": hours}

    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            result = response.json()
            prediction = result["ai_prediction"]

            if "Victory" in prediction:
                st.success(f"Outcome: VICTORY 🏆 - The agent is likely to clear the map.")
                st.balloons()
            else:
                st.error(f"Outcome: DEFEAT 💀 - The agent is statistically likely to perish.")
        else:
            st.warning("Communication error with the combat server.")

    except requests.exceptions.ConnectionError:
        st.error("🚨 Combat Server (Docker) is offline.")


level = st.slider("Player Level", min_value=0, max_value=100, value=10)
hours = st.number_input("Total Hours Played", min_value=0, max_value=1000, value=50)


if st.button("Predict Match Outcome"):

    api_url = "http://localhost:8000/predict"
    data = {"level": level, "hours": hours}

    try:
        response = requests.post(api_url, json=data)

        if response.status_code == 200:
            result = response.json()
            prediction = result["ai_prediction"]

            if "Victory" in prediction:
                st.success(f"AI Says: {prediction}")
                st.balloons()
            else:
                st.error(f"AI Says: {prediction}")
        else:
            st.warning("Uh oh! The API rejected the data.")

    except requests.exceptions.ConnectionError:
        st.error("🚨 Could not connect to the API. Is your Docker container running?")