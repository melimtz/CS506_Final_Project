import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rawg_data = pd.read_csv(r"raw_data/game_info.csv")
rawg_data = pd.DataFrame(rawg_data)

rawg_clean = rawg_data.drop(['website', 'tba', 'metacritic'], axis =1)
rawg_clean = rawg_clean.dropna()

rawg_filtered = rawg_clean[["name", "rating", "playtime","achievements_count",'game_series_count', 'reviews_count']]

rawg_filtered_csv = rawg_clean[["id", "name", "rating", "playtime", "ratings_count"]]
no_name = rawg_filtered.drop('name', axis =1)

# Correlation matrix
no_name = rawg_filtered.drop('name', axis =1)
corr = no_name.corr()
no_name.to_csv("rawg_data_cleaned.csv", index= False)
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.savefig("correlation_matrix.png")
plt.show()