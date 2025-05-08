import matplotlib.pyplot as plt
import streamlit as st

def render_bpr_pie(df):
    st.subheader("🥧 Team Contribution by Player (BPR)")

    if 'box_bpr' not in df.columns:
        st.error("BPR data not found.")
        return

    df['bpr_share'] = (df['box_bpr'] / df['box_bpr'].sum()) * 100

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(df['bpr_share'], labels=df['player_name'], autopct='%1.1f%%', startangle=140)
    ax.set_title("Player Share of Total Team BPR")
    st.pyplot(fig)
