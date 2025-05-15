
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Climate Model Evaluation Dashboard")
st.subheader("Actual vs Predicted for Climate Variables")

@st.cache_data
def load_data():
    y_test = pd.read_csv("y_test.csv", index_col=0)
    y_pred = pd.read_csv("y_pred.csv", index_col=0)
    return y_test, y_pred

y_test, y_pred = load_data()

target_cols = [
    'Avg_Temp (°C)',
    'Precipitation (mm)',
    'Solar_Irradiance (W/m²)',
    'Cloud_Cover (%)',
    'CO2_Concentration (ppm)'
]

selected_var = st.selectbox("Select a variable to visualize:", target_cols)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(y_test[selected_var].values, label="Actual", color="blue")
ax.plot(y_pred[selected_var].values, label="Predicted", linestyle='--', color="orange")
ax.set_title(f"{selected_var} - Actual vs Predicted", fontsize=14)
ax.set_xlabel("Sample Index")
ax.set_ylabel(selected_var)
ax.legend()
ax.grid(True)

st.pyplot(fig)
