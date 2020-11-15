# I am a MarkDown Master
## This is a lot more approachable then some of the assignments we've done
### Can this be the rest of the class pls?

import pandas as pd

day_table = "../../data/raw/day.csv"
hour_table = "../../data/raw/hour.csv"

def process_day(day_table):

    df1 = (
        pd.read_csv(day_table)
        .rename()
        .dropna()
    )

    df2 = (
        df1
        .assign()
    )

    return df2

def process_hour(hour_table):

    df1 = (
        pd.read_csv(hour_table)
        .rename()
        .dropna()
    )

    df2 = (
        df1
        .assign()
    )

    return df2