import plotly.express as px
import streamlit as st


def fill_level_chart(df):

    fig = px.line(
        df.sort_values("id"),
        x="timestamp",
        y="fill_percentage",
        title="Fill Percentage Trend",
    )

    st.plotly_chart(fig, use_container_width=True)


def distance_chart(df):

    fig = px.line(
        df.sort_values("id"), x="timestamp", y="distance", title="Distance Trend"
    )

    st.plotly_chart(fig, use_container_width=True)
