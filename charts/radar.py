import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def render_radar_chart(df):
    st.subheader("🔘 Player Comparison Radar Chart")

    players = st.multiselect("Select Players", options=df['player_name'].unique(), default=df['player_name'].head(3).tolist())
    if len(players) < 2:
        st.warning("Please select at least 2 players.")
        return

    metrics = {
        'points_per_game': 'Scoring',
        'assists_per_game': 'Assists',
        'turnovers_per_game': 'Turnovers',
        'steals_per_game': 'Steals',
        'blocks_per_game': 'Blocks',
        'rebounds_per_game': 'Rebounds'
    }

    radar_df = df[df['player_name'].isin(players)][['player_name'] + list(metrics.keys())].set_index('player_name')
    radar_df = (radar_df - radar_df.min()) / (radar_df.max() - radar_df.min())  # normalize

    labels = list(metrics.values())
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    labels += labels[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    for player in radar_df.index:
        values = radar_df.loc[player].tolist()
        values += values[:1]
        ax.plot(angles, values, label=player)
        ax.fill(angles, values, alpha=0.1)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.set_ylim(0, 1)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    st.pyplot(fig)
