# pyrefly: ignore [missing-import]
import plotly.graph_objects as go

# pyrefly: ignore [missing-import]
import streamlit as st


def show_fill_gauge(fill_percentage):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=fill_percentage,
            title={"text": "Bin Fill Level"},
            gauge={
                "axis": {"range": [0, 100]},
                "steps": [
                    {"range": [0, 30], "color": "green"},
                    {"range": [30, 70], "color": "yellow"},
                    {"range": [70, 100], "color": "red"},
                ],
            },
        )
    )

    st.plotly_chart(fig, use_container_width=True)
