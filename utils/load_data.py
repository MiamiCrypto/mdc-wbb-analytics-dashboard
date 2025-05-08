
import pandas as pd

def load_clean_data():
    # Load the cleaned CSV file
    df = pd.read_csv("data/player_season_stats_2024_25_cleaned.csv")

    # Basic cleaning
    df['player_name'] = df['player_name'].str.strip()

    # Calculate OBPR
    df['box_obpr'] = (
        df['pts'] * 0.5 +
        df['assist'] * 1.2 -
        df['turnovers'] * 1.0 +
        df['fg_pct'] * 10 +
        df['ft_pct'] * 5 +
        df['fg3_pct'] * 5
    ).round(2)

    # Calculate DBPR
    df['box_dbpr'] = (
        df['steals'] * 1.5 +
        df['blocks'] * 1.5 +
        df['totr'] * 0.5 -
        df['pfoul'] * 0.5
    ).round(2)

    # Final BPR
    df['box_bpr'] = df['box_obpr'] + df['box_dbpr']

    return df
