def render_form():
    import streamlit as st

    st.header("Health Vitals Input Form")

    with st.form(key='health_vitals_form'):
        timestamp = st.date_input("Timestamp")
        temperature = st.number_input("Temperature (°C)", min_value=30.0, max_value=45.0, step=0.1)
        blood_pressure = st.text_input("Blood Pressure (mmHg)", placeholder="e.g., 120/80")
        blood_sugar = st.number_input("Blood Sugar (mg/dL)", min_value=0, max_value=400, step=1)
        pulse_rate = st.number_input("Pulse Rate (bpm)", min_value=30, max_value=200, step=1)
        spo2 = st.number_input("SpO2 (%)", min_value=0, max_value=100, step=1)
        medication_name = st.text_input("Medication Name")
        medication_dosage = st.text_input("Medication Dosage")

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.success("Health vitals submitted successfully!")