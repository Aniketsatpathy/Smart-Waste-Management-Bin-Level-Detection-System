# pyrefly: ignore [missing-import]
import streamlit as st


def show_alert(alert):

    if alert:

        st.error(
            """
            COLLECTION REQUIRED

            Bin has reached threshold.
            """
        )

    else:

        st.success("No Active Alerts")
