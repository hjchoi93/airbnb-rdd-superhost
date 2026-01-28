import pandas as pd
import numpy as np

def calendar_coverage(df: pd.DataFrame):
    """
    To calculate occupancy, we will limit listings within a 30-day window 

    df: dataframe that has calendar dates for the listings
    """
    df["date"] = pd.to_datetime(df["date"])
    start_date = df["date"].min()               # first date start (common choice)
    end_date = start_date + pd.Timedelta(days=29)  # inclusive 30-day window

    cal_30 = df.loc[(df["date"] >= start_date) & (df["date"] <= end_date)].copy()

    return cal_30

def occupancy_next_30d(df1: pd.DataFrame, df2: pd.DataFrame):
    """
    This function calculates the occupancy of each listing i.e. how many units are booked out of the total amount of units available per listing.
    To calculate the occupancy, we will only include listings that have enough calendar coverage. 
    This means each listing is available for enough days in the month and does not have a bunch of days where it's unavailable. 
    We will only keep listings where the total calendar coverage is at least 25 days out of 30 calendar days. 

    df1: The dataframe that includes the original listings 
    df2: The dataframe that has calendar dates for the listings
    """
    
    cal_30 = calendar_coverage(df2)

    # --- Count booked/available within window ---
    # booked proxy: available == 'f' (unavailable, could be booked or blocked)
    cal_30["is_booked"] = (cal_30["available"] == "f").astype(int)
    cal_30["is_available"] = (cal_30["available"] == "t").astype(int)

    agg = (
        cal_30.groupby("listing_id", as_index=False)
        .agg(
            n_days_observed=("date", "size"),      # number of rows/days observed
            n_booked=("is_booked", "sum"),
            n_available=("is_available", "sum"),
        )
    )

    # n_total is the total amount of days the booking is available 
    agg["n_total"] = agg["n_booked"] + agg["n_available"]

    # Occupancy rate i.e. what percent of this listing is unavailable in the next 30 days 
    agg["occupancy_next_30d"] = agg["n_booked"] / agg["n_total"]

    # --- Filter to listings with enough coverage ---
    MIN_COVERAGE = 25  # minimum number of days necessary for coverage 
    agg_filtered = agg.loc[agg["n_total"] >= MIN_COVERAGE].copy()

    # Merge the filtered listings back into original dataframe 

    listings_df = df1.merge(
    agg_filtered[["listing_id", "occupancy_next_30d", "n_total"]],
    left_on="id",
    right_on="listing_id",
    how="inner"
    ).drop(columns=["listing_id"])

    return listings_df




