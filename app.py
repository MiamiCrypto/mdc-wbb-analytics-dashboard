import streamlit as st
import pandas as pd
from charts.radar import render_radar_chart
from charts.barplots import render_bpr_by_class
from charts.pie_charts import render_bpr_pie

# Load data
@st.cache
def load_data():
    stats = pd.read_csv("data/player_season_stats_2024_25_cleaned.csv")
    roster = pd.read_csv("data/mdc_roster_2024_25_cleaned.csv")
    return pd.merge(stats, roster, on='player_name', how='left')

df = load_data()

st.title("🏀 MDC Women's Basketball Analytics Dashboard (2024–25)")

# Sidebar filters
st.sidebar.header("Filters")
min_minutes = st.sidebar.slider("Minimum Minutes", 0, 800, 100)
filtered_df = df[df['min'] >= min_minutes]

# Tabs for analysis views
tabs = st.tabs(["Summary Table", "Radar", "BPR Pie", "Class Breakdown"])

with tabs[0]:
    st.dataframe(filtered_df[['player_name', 'points_per_game', 'box_obpr', 'box_dbpr', 'box_bpr']])

with tabs[1]:
    render_radar_chart(filtered_df)

with tabs[2]:
    render_bpr_pie(filtered_df)

with tabs[3]:
    render_bpr_by_class(filtered_df)
