import streamlit as st
from datetime import datetime

def render_form():
    """
    Render the input form for health vitals and return the form data as a dictionary.
    """
    st.subheader("Enter Health Vitals")

    # Input fields
    date = st.date_input("Date", value=datetime.today().date())
    time = st.time_input("Time", value=datetime.now().time())
    temperature = st.number_input("Temperature (°C)", min_value=30.0, max_value=45.0, step=0.1, value=36.0)
    blood_pressure = st.text_input("Blood Pressure (systolic/diastolic, e.g., 120/80)", value="")
    blood_sugar = st.number_input("Blood Sugar (mg/dL)", min_value=0.0, max_value=500.0, step=1.0, value=100.0)
    pulse_rate = st.number_input("Pulse Rate (bpm)", min_value=0, max_value=200, step=1, value=70)
    spo2 = st.number_input("SpO2 (%)", min_value=0, max_value=100, step=1, value=98)
    medication_name = st.text_input("Medication Name (optional)", value="")
    medication_dosage = st.text_input("Medication Dosage (optional)", value="")

    # Combine date and time into a single timestamp
    timestamp = datetime.combine(date, time).isoformat()

    # Return the form data as a dictionary
    return {
        "timestamp": timestamp,
        "temperature": temperature if temperature != 0.0 else None,
        "blood_pressure": blood_pressure if blood_pressure else None,
        "blood_sugar": blood_sugar if blood_sugar != 0.0 else None,
        "pulse_rate": pulse_rate if pulse_rate != 0 else None,
        "spo2": spo2 if spo2 != 0 else None,
        "medication_name": medication_name if medication_name else None,
        "medication_dosage": medication_dosage if medication_dosage else None,
    }