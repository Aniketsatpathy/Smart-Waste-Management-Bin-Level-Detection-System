# pyrefly: ignore [missing-import]
import streamlit as st


def show_analytics(df):

    total_readings = len(df)

    avg_fill = df["fill_percentage"].mean()

    max_fill = df["fill_percentage"].max()

    alert_count = df["alert"].sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Readings", total_readings)

    c2.metric("Average Fill %", f"{avg_fill:.2f}")

    c3.metric("Max Fill %", f"{max_fill:.2f}")

    c4.metric("Alert Count", int(alert_count))
