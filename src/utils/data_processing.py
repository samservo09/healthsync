import pandas as pd
import os

def save_to_csv(data, filename='health_vitals.csv'):
    """
    Save the form data to a CSV file. If the file doesn't exist, create it with headers.
    """
    df = pd.DataFrame([data])  # Wrap the data in a list to create a DataFrame
    if not os.path.exists(filename):  # Check if the file exists
        df.to_csv(filename, mode='w', header=True, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)

def validate_vitals(form_data):
    """
    Returns a list of abnormal vitals. If the list is empty, everything is within normal range.
    """
    abnormal = []

    normal_ranges = {
        "temperature": (36.1, 37.2),
        "blood_pressure": (90, 120),
        "blood_sugar": (70, 140),
        "pulse_rate": (60, 100),
        "spo2": (95, 100),
    }

    for vital, (low, high) in normal_ranges.items():
        value = form_data.get(vital)

        # Try to convert value to float
        try:
            value = float(value)
        except (TypeError, ValueError):
            continue  # Skip this vital if it's not a valid number

        if not (low <= value <= high):
            abnormal.append(f"{vital.replace('_', ' ').title()}: {value}")

    return abnormal
