def save_to_csv(data, filename='health_vitals.csv'):
    import pandas as pd

    df = pd.DataFrame(data)
    df.to_csv(filename, mode='a', header=False, index=False)

def validate_vitals(temperature, blood_pressure, blood_sugar, pulse_rate, spo2):
    valid = True
    errors = []

    if not (36.1 <= temperature <= 37.2):
        valid = False
        errors.append("Temperature out of range (36.1 - 37.2 °C)")
    
    if not (90 <= blood_pressure[0] <= 120 and 60 <= blood_pressure[1] <= 80):
        valid = False
        errors.append("Blood pressure out of range (90/60 - 120/80 mmHg)")
    
    if not (70 <= blood_sugar <= 140):
        valid = False
        errors.append("Blood sugar out of range (70 - 140 mg/dL)")
    
    if not (60 <= pulse_rate <= 100):
        valid = False
        errors.append("Pulse rate out of range (60 - 100 bpm)")
    
    if not (95 <= spo2 <= 100):
        valid = False
        errors.append("SpO2 out of range (95 - 100%)")

    return valid, errors