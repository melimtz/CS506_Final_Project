import numpy as np
import pandas as pd

# Read the data from game_info.csv
rawg_data = pd.read_csv(r"game_info.csv")

# Create the dataframe rawg_data
rawg_data = pd.DataFrame(rawg_data)

# Clean the dataframe rawg_data
rawg_clean = rawg_data.drop(['website', 'tba', 'metacritic'], axis =1)
rawg_clean = rawg_clean.dropna()

# Filtering the clean data, removing unwanted columns
rawg_filtered_csv = rawg_clean[["id", "name", "rating", "playtime", "ratings_count", "added_status_owned"]]
# To alter written data in csv file, add/remove/change strings to the list of column names you're interested in
# Current Columns: id, name, rating, playtime, ratings count, how many owned

# Writing filtered dataframe to filtered_rawg_info.csv. This one is NOT sorted by any specific column.
rawg_filtered_csv.to_csv("filtered_rawg_info.csv", index=False) 
# index=False removes row numbers, index=True keeps row numbers

# NOTE: Be careful about writing/altering filtered_rawg_info.csv. Both data_cleaned.py and data_cleansing.ipynb write the filtered data to the same file (filtered_rawg_info.csv) when run. 
# Changing one line in either code but not the other may cause issues or confusions after running. 



# EXTRA!
# These are the csv files in extra_data. 
# Some may be unimportant/irrelevant to our project, but I thought they'd be interesting to observe


# If you want to add/remove columns to any of the csv files below, add to this line:
rawg_df = rawg_clean[["id", "name", "rating", "playtime", "ratings_count", "added_status_owned"]]


# rawg_sorted_owned.csv 

# Sorts in descending order by number owned
rawg_owned = rawg_df.sort_values(by=["added_status_owned"], ascending=False)
# Filters out any games that have 0 owned
rawg_owned = rawg_df[rawg_df["added_status_owned"] > 0]

rawg_owned.to_csv("extra_data/rawg_sorted_owned.csv", index=False) # note: includes 9440 games


# rawg_extra_col.csv

# Adds a new column of the ratio of ratings count to number owned. The percentage of how many ratings there are out of all owned

# Sorts in descending order by number owned
rawg_rc_owned = rawg_df.sort_values(by=["added_status_owned"], ascending=False)

# Divides value in ratings by value in owned: Ratings/Owned
rawg_rc_owned["ratings_by_owned"] = rawg_rc_owned["ratings_count"]/rawg_rc_owned["added_status_owned"]

# If there are more ratings of a game than the number owned, the value is -1. Comment this line if you care about original value
rawg_rc_owned["ratings_by_owned"] = rawg_rc_owned["ratings_by_owned"].apply(lambda x: -1 if x>1 else x)

# This line filters out any games with more ratings than number owned. Currently unfiltered, uncomment the line if you want to filter all -1's out
# rawg_rc_owned = rawg_rc_owned[rawg_rc_owned["ratings_by_owned"] != -1]

rawg_rc_owned.to_csv("extra_data/rawg_extra_col.csv", index=False) 

