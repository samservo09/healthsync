import streamlit as st
import pandas as pd
from components.form import render_form
from utils.data_processing import save_to_csv, validate_vitals
from visualizations.line_chart import plot_vital_signs

# Set the title of the app
st.title("HealthSync - Health Vitals Monitor")

# Render the input form
form_data = render_form()

# If the form is submitted
if st.button("Submit"):
    # Validate the input data
    if validate_vitals(form_data):
        # Save the data to a CSV file
        save_to_csv(form_data)
        st.success("Data submitted successfully!")
    else:
        st.error("Please check your input values. Some vitals are out of the normal range.")

# Load the existing data for visualization
try:
    data = pd.read_csv("health_vitals.csv")
    plot_vital_signs(data)
except FileNotFoundError:
    st.warning("No data available for visualization. Please submit some health vitals first.")