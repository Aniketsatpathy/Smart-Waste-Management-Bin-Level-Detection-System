# pyrefly: ignore [missing-import]
import streamlit as st


def show_kpis(latest):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Fill Level", f"{latest['fill_percentage']:.2f}%")

    with col2:
        st.metric("Distance", f"{latest['distance']:.2f} cm")

    with col3:
        st.metric("Status", latest["status"])

    with col4:

        alert_text = "ACTIVE" if latest["alert"] else "NORMAL"

        st.metric("Alert", alert_text)
