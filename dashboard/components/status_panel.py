# pyrefly: ignore [missing-import]
import streamlit as st


def show_status(status):

    if status == "EMPTY":

        st.success("Bin Status: Empty")

    elif status == "HALF_FULL":

        st.info("Bin Status: Half Full")

    elif status == "ALMOST_FULL":

        st.warning("Bin Status: Almost Full")

    elif status == "FULL":

        st.error("Bin Status: Full")
