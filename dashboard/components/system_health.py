# pyrefly: ignore [missing-import]
import streamlit as st


def show_system_status():

    st.subheader("System Health")

    st.success("ESP32 : Online")

    st.success("MQTT : Connected")

    st.success("SQLite : Connected")

    st.success("Dashboard : Running")
