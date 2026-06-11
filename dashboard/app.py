# pyrefly: ignore [missing-import]
import streamlit as st

from utils import load_data

from components.kpi_cards import show_kpis

from components.status_panel import show_status

from components.alert_panel import show_alert

from components.charts import fill_level_chart, distance_chart

# pyrefly: ignore [missing-import]
from streamlit_autorefresh import st_autorefresh
from components.gauge import show_fill_gauge
from components.bin_visual import show_bin

st_autorefresh(interval=5000, key="dashboard_refresh")


st.set_page_config(page_title="Smart Waste Management", layout="wide")


st.title("Smart Waste Management Dashboard")

st.caption("IoT Bin Monitoring Platform")


df = load_data()

if df.empty:

    st.warning("No data available.")

    st.stop()


latest = df.iloc[0]

status_display = latest["status"].replace("_", " ").title()
st.metric("Status", status_display)


show_kpis(latest)

st.divider()

col1, col2 = st.columns(2)

with col1:
    show_fill_gauge(latest["fill_percentage"])

with col2:
    show_bin(latest["fill_percentage"])

st.divider()

show_status(latest["status"])

show_alert(latest["alert"])

st.divider()

fill_level_chart(df)

distance_chart(df)

st.divider()

st.subheader("Recent Readings")

st.dataframe(df.head(20), use_container_width=True)

st.subheader("Alert History")

alerts_df = df[df["alert"] == 1]

st.dataframe(alerts_df.head(20))
