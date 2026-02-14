import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="TeleHealth Monitor", page_icon="🏥", layout="wide")

st.title("🏥 Patient Vitals Live Stream")

if 'vitals_history' not in st.session_state:
    st.session_state.vitals_history = pd.DataFrame(columns=['Time', 'BPM', 'SpO2'])

placeholder = st.empty()

for _ in range(100):
    # Simulated Medical Data from Pico W
    bpm = round(np.random.uniform(70, 85) + np.sin(_/5)*5, 1)
    spo2 = round(np.random.uniform(96, 99), 1)
    
    new_data = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), bpm, spo2]], 
                             columns=st.session_state.vitals_history.columns)
    st.session_state.vitals_history = pd.concat([st.session_state.vitals_history, new_data]).tail(30)

    with placeholder.container():
        c1, c2 = st.columns(2)
        c1.metric("Heart Rate", f"{bpm} BPM", delta="Normal")
        c2.metric("Oxygen Saturation", f"{spo2} %", delta="Stable")

        if bpm > 100 or spo2 < 94:
            st.error("🚨 CRITICAL ALERT: Abnormal Vitals Detected. Notify Medical Staff.")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=st.session_state.vitals_history['Time'], 
                                 y=st.session_state.vitals_history['BPM'], 
                                 name="Pulse (BPM)", line=dict(color="#e74c3c", width=3)))
        fig.update_layout(title="Continuous Heart Rate Monitoring (PPG)", template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
        
    time.sleep(1)
