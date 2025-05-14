import streamlit as st
import pandas as pd
import os
from components.form import render_form
from utils.data_processing import save_to_csv, validate_vitals
from visualizations.line_chart import plot_vital_signs

# Set the title of the app
st.title("HealthSync - Health Vitals Monitor")

# Render the input form
form_data = render_form()

# When form is submitted
if st.button("Submit"):
    save_to_csv(form_data)
    st.success("Data submitted successfully!")
    


# Load the data after submission or if file exists
if st.session_state.get("submitted", False) or "health_vitals.csv" in os.listdir():
    try:
        data = pd.read_csv("health_vitals.csv")
        if not data.empty:
            plot_vital_signs(data)
        else:
            st.warning("No data available for visualization. Please submit some health vitals first.")
    except FileNotFoundError:
        st.warning("No data available for visualization. Please submit some health vitals first.")

