import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "models" / "asteroid_hazard_model.pkl"

model = joblib.load(MODEL_PATH)

st.title("☄️ Asteroid Hazard Prediction System")

st.write(
    "Predict whether a Near-Earth Asteroid is hazardous."
)

relative_velocity = st.number_input(
    "Relative Velocity",
    min_value=0.0,
    value=50000.0
)

miss_distance = st.number_input(
    "Miss Distance",
    min_value=0.0,
    value=30000000.0
)

absolute_magnitude = st.number_input(
    "Absolute Magnitude",
    min_value=0.0,
    value=22.0
)

avg_diameter = st.number_input(
    "Average Diameter",
    min_value=0.0,
    value=0.2
)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "relative_velocity": [relative_velocity],
        "miss_distance": [miss_distance],
        "absolute_magnitude": [absolute_magnitude],
        "avg_diameter": [avg_diameter]
    })

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction:
        st.error("⚠️ Hazardous Asteroid")
    else:
        st.success("✅ Non-Hazardous Asteroid")

    st.write(f"Hazard Probability: {probability:.2%}")