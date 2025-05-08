import pandas as pd

def load_clean_data():
    """
    Loads and merges the cleaned player stats and roster files.
    Assumes both are in /data and properly cleaned.
    Returns a merged DataFrame.
    """
    stats_path = "data/player_season_stats_2024_25_cleaned.csv"
    roster_path = "data/mdc_roster_2024_25_cleaned.csv"

    stats_df = pd.read_csv(stats_path)
    roster_df = pd.read_csv(roster_path)

    # Ensure consistent casing before merge
    stats_df['player_name'] = stats_df['player_name'].str.strip()
    roster_df['player_name'] = roster_df['player_name'].str.strip()

    # Merge on player_name
    df = pd.merge(stats_df, roster_df, on='player_name', how='left')

    # Optional: calculate derived metrics if needed
    df['box_bpr'] = df['box_obpr'] + df['box_dbpr']
    df['minutes'] = df['min']  # Alias for easier filtering

    return df
