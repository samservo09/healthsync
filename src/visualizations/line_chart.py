def plot_vital_signs(data):
    import pandas as pd
    import altair as alt

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

    # Create a list to hold the charts
    charts = []

    # Generate line charts for each vital sign
    for vital in normal_ranges.keys():
        chart = (
            alt.Chart(df)
            .mark_line()
            .encode(
                x='timestamp:T',
                y=f'{vital}:Q',
                tooltip=['timestamp:T', f'{vital}:Q']
            )
            .properties(title=f'{vital.capitalize()} Over Time')
        )

        # Highlight out-of-range values
        out_of_range = df[(df[vital] < normal_ranges[vital][0]) | (df[vital] > normal_ranges[vital][1])]
        if not out_of_range.empty:
            chart = chart.mark_point(color='red').encode(
                opacity=alt.value(1)
            ).transform_filter(
                alt.datum[vital] < normal_ranges[vital][0] | alt.datum[vital] > normal_ranges[vital][1]
            ).add_selection(
                alt.selection_single(on='mouseover', fields=[f'{vital}:Q'], empty='none')
            )

        charts.append(chart)

    # Combine all charts into a single chart
    combined_chart = alt.vconcat(*charts).resolve_scale(y='independent')

    return combined_chart