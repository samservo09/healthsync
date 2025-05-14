import pandas as pd
import altair as alt
import streamlit as st

def plot_vital_signs(data):
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Define the normal ranges for vitals
    normal_ranges = {
        'temperature': (36.1, 37.2),
        'blood_pressure': (90, 120),  # systolic
        'blood_sugar': (70, 140),
        'pulse_rate': (60, 100),
        'SpO2': (95, 100)
    }

    # Convert numeric columns safely
    for vital in normal_ranges.keys():
        if vital in df.columns:
            df[vital] = pd.to_numeric(df[vital], errors='coerce')

    # Convert timestamp if needed
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    # Drop rows with missing timestamps
    df.dropna(subset=['timestamp'], inplace=True)

    # Create a list to hold the charts
    charts = []

    # Generate line charts for each vital sign
    for vital, (low, high) in normal_ranges.items():
        if vital not in df.columns or df[vital].dropna().empty:
            continue

        # Main line chart
        chart = (
            alt.Chart(df)
            .mark_line()
            .encode(
                x='timestamp:T',
                y=alt.Y(f'{vital}:Q', title=vital.replace('_', ' ').capitalize()),
                tooltip=['timestamp:T', f'{vital}:Q']
            )
            .properties(title=f'{vital.capitalize()} Over Time')
        )

        # Highlight out-of-range values
        highlight = (
            alt.Chart(df)
            .mark_point(color='red', size=60)
            .encode(
                x='timestamp:T',
                y=f'{vital}:Q',
                tooltip=['timestamp:T', f'{vital}:Q']
            )
            .transform_filter(
                (alt.datum[vital] < low) | (alt.datum[vital] > high)
            )
        )

        # Combine chart and highlight
        full_chart = chart + highlight
        charts.append(full_chart)

    if charts:
        combined_chart = alt.vconcat(*charts).resolve_scale(y='independent')
        st.altair_chart(combined_chart, use_container_width=True)
    else:
        st.info("No valid data to visualize.")
