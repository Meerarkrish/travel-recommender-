# international_symptom_checker.py

import streamlit as st
import requests

st.set_page_config(page_title="International Symptom Checker", layout="wide")
st.title("🌍 International Symptom & Risk Checker")

# ------------------------------
# 1. Demographics
# ------------------------------
age = st.number_input("Enter your age", min_value=0, max_value=120, value=30)
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])

# ------------------------------
# 2. Symptoms
# ------------------------------
symptoms = st.multiselect(
    "Select your symptoms",
    ["Fever", "Cough", "Shortness of Breath", "Sore Throat", "Fatigue", "None"]
)

# ------------------------------
# 3. Risk Factors
# ------------------------------
risk_factors = st.multiselect(
    "Do you have any of these risk factors?",
    ["Heart Disease", "Diabetes", "COPD", "Immunocompromised", "None"]
)

# ------------------------------
# 4. Exposure
# ------------------------------
exposure = st.radio("Recent contact with sick person?", ["Yes", "No"])

# ------------------------------
# 5. Location
# ------------------------------
location = st.text_input("Enter your city/state/country")

# ------------------------------
# 6. Calculate risk score
# ------------------------------
risk_score = 0

# Symptoms scoring
if "Fever" in symptoms: risk_score += 2
if "Cough" in symptoms: risk_score += 1
if "Shortness of Breath" in symptoms: risk_score += 3
if "Sore Throat" in symptoms: risk_score += 1
if "Fatigue" in symptoms: risk_score += 1

# Exposure and demographics
if exposure == "Yes": risk_score += 2
if age > 65: risk_score += 2
if any(factor != "None" for factor in risk_factors): risk_score += 2

# ------------------------------
# 7. Epidemic/Endemic Status (Placeholder)
# ------------------------------
epidemic_score = 0
if location:
    st.info(f"Fetching epidemic data for {location}...")
    # Example: placeholder API call (replace with real API)
    # response = requests.get(f"https://api.healthmap.org/outbreaks?location={location}")
    # data = response.json()
    # epidemic_score = calculate_additional_risk(data)
    # For now, simulate
    epidemic_score = 1
    risk_score += epidemic_score

# ------------------------------
# 8. Determine Risk Level
# ------------------------------
if risk_score >= 6:
    risk_level = "High Risk"
    advice = "Stay home, contact a doctor immediately, and avoid public places."
elif risk_score >= 3:
    risk_level = "Moderate Risk"
    advice = "Monitor symptoms, limit contact with others, and consider medical advice."
else:
    risk_level = "Low Risk"
    advice = "You can go about your day but watch for symptoms and practice hygiene."

# ------------------------------
# 9. Display Results
# ------------------------------
st.subheader(f"Your Risk Level: {risk_level}")
st.success(advice)

# Optional: Display a summary table
st.subheader("Summary")
st.table({
    "Attribute": ["Age", "Gender", "Symptoms", "Risk Factors", "Exposure", "Location", "Risk Score"],
    "Value": [age, gender, ", ".join(symptoms) or "None", ", ".join(risk_factors) or "None", exposure, location or "Unknown", risk_score]
})