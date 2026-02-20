import streamlit as st
import joblib
import pandas as pd

# --- 1. THE BRAIN (LOAD DIRECTLY) ---
# We load the model here so the cloud can use it without needing a separate API
model = joblib.load("model.pkl")

# --- 2. BRANDING ---
st.set_page_config(page_title="VizDoom AI Predictor", page_icon="👹")
st.title("👹 VizDoom Combat Predictor")
st.write("This AI analyzes combat data to predict an agent's success rate.")

# --- 3. INPUTS ---
level = st.slider("Select Combat Tier (Level)", min_value=1, max_value=100, value=18)
hours = st.number_input("Agent Training Hours", min_value=1, max_value=1000, value=50)

# --- 4. PREDICTION LOGIC ---
if st.button("Calculate Probability of Survival"):
    # Create the data for the model
    new_data = pd.DataFrame([[level, hours]], columns=['level', 'hours'])
    prediction = model.predict(new_data)[0]

    if prediction == 1:
        st.success(f"Outcome: VICTORY 🏆 - The agent is likely to clear the map.")
        st.balloons()
    else:
        st.error(f"Outcome: DEFEAT 💀 - The agent is statistically likely to perish.")