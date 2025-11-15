import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model, scaler, and feature names
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
feature_names = joblib.load('feature_names.pkl')

st.set_page_config(page_title="Carbon Intensity Predictor", layout="centered")
st.title("🌍 Carbon Intensity Predictor")
st.write("Estimate carbon intensity (Million Tons per TWh) based on energy usage data.")

# Input fields
total_energy = st.number_input("Total Energy Consumption (TWh)", value=1200.0)
fossil_pct = st.slider("Fossil Fuel Dependency (%)", 0, 100, 70)
industrial_pct = st.slider("Industrial Energy Use (%)", 0, 100, 40)
household_pct = st.slider("Household Energy Use (%)", 0, 100, 30)
per_capita = st.number_input("Per Capita Energy Use (kWh)", value=5000.0)
price_index = st.number_input("Energy Price Index (USD/kWh)", value=0.12)
renewable_pct = st.slider("Renewable Energy Share (%)", 0, 100, 25)

if st.button("Predict Carbon Intensity"):
    input_dict = {
        'Total Energy Consumption (TWh)': total_energy,
        'Fossil Fuel Dependency (%)': fossil_pct,
        'Industrial Energy Use (%)': industrial_pct,
        'Household Energy Use (%)': household_pct,
        'Per Capita Energy Use (kWh)': per_capita,
        'Energy Price Index (USD/kWh)': price_index,
        'Renewable Energy Share (%)': renewable_pct
    }

    df = pd.DataFrame([input_dict])

    # Feature engineering
    df['Fossil_Energy_Used'] = df['Total Energy Consumption (TWh)'] * (df['Fossil Fuel Dependency (%)'] / 100)
    df['Industrial × Fossil'] = df['Industrial Energy Use (%)'] * df['Fossil Fuel Dependency (%)']
    df['Household × Price'] = df['Household Energy Use (%)'] * df['Energy Price Index (USD/kWh)']
    df['Energy_Intensity'] = df['Total Energy Consumption (TWh)'] / df['Per Capita Energy Use (kWh)']
    df['Fossil_Intensity'] = df['Fossil_Energy_Used'] / df['Per Capita Energy Use (kWh)']
    df['Simulated_Population'] = df['Total Energy Consumption (TWh)'] / df['Per Capita Energy Use (kWh)']
    df['Simulated_GDP'] = df['Simulated_Population'] * df['Energy Price Index (USD/kWh)']

    # Match training features exactly
    df = df[feature_names]
    df_scaled = scaler.transform(df)
    pred_log = model.predict(df_scaled)
    pred = np.expm1(pred_log)

    st.success(f"🌱 Predicted Carbon Intensity: **{round(pred[0], 4)} Million Tons per TWh**")