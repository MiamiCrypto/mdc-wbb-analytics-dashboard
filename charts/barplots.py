import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def render_bpr_by_class(df):
    st.subheader("📊 BPR by Class Year")

    if 'box_bpr' not in df.columns:
        st.error("BPR data not found.")
        return

    bpr_class = df.groupby('class_year')['box_bpr'].mean().sort_values(ascending=False).reset_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=bpr_class, x='class_year', y='box_bpr', palette='Set2', ax=ax)
    ax.set_title("Average BPR by Class Year")
    ax.set_ylabel("Box BPR")
    ax.set_xlabel("Class")
    ax.bar_label(ax.containers[0], fmt="%.1f", padding=3)
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig)
