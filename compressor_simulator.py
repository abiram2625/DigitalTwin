import streamlit as st
import matplotlib.pyplot as plt

# Web App Title
st.title("🛠️ Industrial Compressor Digital Twin")

# 1. Interactive Sliders
col1, col2 = st.columns(2)
with col1:
    temp = st.slider("Temperature (°C)", 50, 150, 80)
    vibration = st.slider("Vibration (mm/s)", 1.0, 10.0, 2.5)
with col2:
    efficiency = st.slider("Efficiency (%)", 30.0, 50.0, 46.2)
    flow_rate = st.slider("Flow Rate (acfm)", 5.0, 20.0, 12.6)

# 2. Failure Prediction Logic
failure_risk = 0
if temp > 100:
    failure_risk += (temp - 100) * 1.5
if vibration > 5:
    failure_risk += (vibration - 5) * 10
failure_risk = min(100, failure_risk)

# 3. Display Metrics
st.metric("🔥 Failure Risk", f"{failure_risk:.1f}%")
st.metric("⚡ Efficiency", f"{efficiency:.1f}%")

# 4. Live Graph
fig, ax = plt.subplots()
ax.bar(["Temp", "Vibration", "Efficiency"], [temp, vibration, efficiency], color=["red", "orange", "green"])
st.pyplot(fig)