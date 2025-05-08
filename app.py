import streamlit as st
import pandas as pd
from utils.load_data import load_clean_data
from charts.radar import render_radar_chart
from charts.barplots import render_bpr_by_class
from charts.pie_charts import render_bpr_pie

# Page config
st.set_page_config(page_title="MDC WBB Analytics", layout="wide")

# Load data
df = load_clean_data()

# App title
st.title("🏀 MDC Women's Basketball Analytics Dashboard (2024–25)")

# Sidebar
st.sidebar.header("Filters")
min_minutes = st.sidebar.slider("Minimum Minutes Played", 0, 800, 100)
selected_position = st.sidebar.multiselect("Filter by Position", options=df['position'].dropna().unique(), default=df['position'].dropna().unique())
selected_class = st.sidebar.multiselect("Filter by Class Year", options=df['class_year'].dropna().unique(), default=df['class_year'].dropna().unique())

# Apply filters
filtered_df = df[
    (df['minutes'] >= min_minutes) &
    (df['position'].isin(selected_position)) &
    (df['class_year'].isin(selected_class))
]

# Tabs
tabs = st.tabs(["📋 Player Table", "📊 BPR Pie Chart", "🎓 Class BPR", "📈 Radar Comparison"])

with tabs[0]:
    st.subheader("📋 Team Roster Stats")
    st.dataframe(
        filtered_df[
            ['player_name', 'points_per_game', 'box_obpr', 'box_dbpr', 'box_bpr', 'minutes_per_game', 'class_year', 'position']
        ].sort_values(by='box_bpr', ascending=False),
        use_container_width=True
    )

with tabs[1]:
    render_bpr_pie(filtered_df)

with tabs[2]:
    render_bpr_by_class(filtered_df)

with tabs[3]:
    render_radar_chart(filtered_df)
