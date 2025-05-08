import streamlit as st
from utils.load_data import load_clean_data
from charts.radar import render_radar_chart
from charts.barplots import render_bpr_by_class
from charts.pie_charts import render_bpr_pie

# Page settings
st.set_page_config(page_title="MDC WBB Analytics Dashboard", layout="wide")

# Load the data
df = load_clean_data()

# App title
st.title("🏀 MDC Women's Basketball Analytics Dashboard (2024–25)")

# Sidebar filters
st.sidebar.header("Filter Players")
min_minutes = st.sidebar.slider("Minimum Minutes Played", 0, 800, 100)

# Optional class/position filters if those columns exist
if 'position' in df.columns:
    positions = df['position'].dropna().unique().tolist()
    selected_positions = st.sidebar.multiselect("Select Position(s)", options=positions, default=positions)
else:
    selected_positions = df['player_name'].tolist()  # fallback

if 'class_year' in df.columns:
    class_years = df['class_year'].dropna().unique().tolist()
    selected_years = st.sidebar.multiselect("Select Class Year(s)", options=class_years, default=class_years)
else:
    selected_years = df['player_name'].tolist()  # fallback

# Filter dataframe
filtered_df = df[
    (df['minutes_per_game'] >= min_minutes) &
    (df['position'].isin(selected_positions)) &
    (df['class_year'].isin(selected_years))
]

# Dashboard Tabs
tabs = st.tabs(["📋 Team Stats Table", "🥧 BPR Pie", "🎓 Class Year BPR", "📈 Radar Chart"])

with tabs[0]:
    st.subheader("📋 Player Stats Overview")
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
