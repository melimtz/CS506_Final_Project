# How Games' Player Statistics Influence Their Rating/Popularity

## CS506 Final Project by Anderson, Megha, Melissa, Mia, and Shepherd

### Video Presentation

[CS506 Final Report Video Presentation](https://www.youtube.com/watch?v=d-07WhmvOBc)

### Data Processing

After loading the data into Jupyter Notebook, we started the cleaning process by looking at the columns in the dataset and seeing which ones would be the most useful predictors for the game ratings. The original file included 97410 rows and 27 columns, but during preliminary cleaning, we got rid of the URL, TBA (to be announced), and Metacritic rating columns. The first two columns appeared unnecessary, so we removed them. Although we originally planned to include the Metacritic rating, a majority of the games had NaN values in this column. This interfered with the rest of the cleaning process when we tried to drop all NaN values, so the best course of action was to delete that column as well. Cleaning the data left us with approximately 48,000 usable entries in the set. Although this means that a decent proportion of the dataset was dropped, this action was our best choice because of how sparsely distributed some NaN values were.

We decided to filter the data further by selecting a few columns to build our model with. For our first correlation matrix, we chose the following features to predict rating: playtime, number of achievements, number of games in a series, ownership status, and number of reviews. All variables seemed well-correlated, but the ownership status and number of reviews were very heavily correlated, so we had to drop one of them to avoid problematic predictions. We ultimately dropped the ownership variable because it seemed less valuable than the number of ratings in a game when it came to determining game popularity. Our final set of predictors is as follows: playtime, number of achievements, number of games in a series, and number of reviews. 

Once we had the predictors, we needed to determine the relationship between the predictors and the response variable. We used the cleaned data to build a linear model in R. The summary statistics indicated that the relationship between the predictors and the response variable was not linear, as the R-squared value was around 0.28, meaning that the predictors do not have a significant linear relationship with the response variable. This finding told us that to accurately model the relationship between the predictors and game ratings, we would have to look into non-linear algorithms.

- [Code referenced](https://github.com/melimtz/CS506_Final_Project/tree/main/data_processing)


### Data Visualization 

![alt text](https://github.com/melimtz/CS506_Final_Project/blob/main/images/correlation_mat_v1.png "Correlation Matrix (V1)")

Correlation Matrix (Version 1)

![alt text](https://github.com/melimtz/CS506_Final_Project/blob/main/images/correlation_mat_v2.png "Correlation Matrix (V2)")

Correlation Matrix (Version 2)

![alt text](https://github.com/melimtz/CS506_Final_Project/blob/main/images/lr.png "Linear Regression Model")

Linear Regression Model

![alt text](https://github.com/melimtz/CS506_Final_Project/blob/main/images/clustering.png "K Means Clustering Model")

K-Means Clustering Model

### Data Modeling

Our data modeling focuses on predicting and grouping the cleaned RAWG data using a correlation matrix, a linear regression model, and two K-means models. We first used the correlation matrix to determine the correlation between the predictors, and then used that knowledge to decide the predictors we would use in our following data models. For our first correlation matrix’s predictors, we chose: a game’s average rating (rating), a game’s total playtime (playtime), the number of game copies owned (added_status_owned), the achievements count (achievment_count), the number of games in a series (game_series_count), and the reviews count (reviews_count). In our first correlation matrix, each predictor had a relatively stable correlation with the others. However, the correlation between added_status_owned and reviews_count was very high, so we decided to remove added_status_owned because the number of reviews would likely have a greater influence on the game's rating. After removing the number of game copies owned (added_status_owned), we were left with ratings, playtime, achievements count, game series count, and reviews count.

After carefully selecting our predictors, we used the previously processed data to create a multiple linear regression model that shows the relationship between our predicted game ratings and the actual ratings. We chose the dependent variable to be the rating, and the independent variables were playtime, achievement count, game series count, and review count. We then created a new dataset of predicted values based on the multiple linear regression model, which we used to compare the predicted rating to the linear regression graph of the actual rating. 

We also used K-means to create a clustering model using the selected features: playtime, achievement count, game series count, and review count. Given the data features, we used the K-means clustering method to create 3 main clusters, which show the groupings of game popularity. To take it a step further, we use the same approach using K-means++. We then compare the silhouette scores of K-means++ with different cluster numbers based on three distances: Euclidean, Manhattan, and cosine. Lastly, we evaluate the mean accuracy of our clusters using the K-nearest neighbor classifier on three distance metrics as well: Euclidean, Manhattan, and Minkowski. 

- [Code referenced](https://github.com/melimtz/CS506_Final_Project/tree/main/data_modeling)


### Results / Findings

Our initial data modeling gives us insight into the relationships between players' statistics and a game’s rating/popularity. We used a multiple linear regression model to predict RAWG user ratings based on variables such as playtime, achievements count, game series count, and reviews count. The model confirms that all predictors have statistical significance (p < 2e-16). It is important to note that playtime had the most significant effect on predicted rating, followed by the number of reviews. This tells us that user-led metrics are more influential to a game’s rating than its innate metrics, like the number of achievements it has.

The summary statistics indicated that the R-squared value was around 0.28. Based on our understanding, the R-squared value is a value that indicates how well our model predicts or “fits” the dataset and can take on values between 0 and 1, with 0 indicating that the independent variable doesn’t explain the dependent variable and 1 indicating a perfect explanation.

Because our R-squared value was 0.28, this means 28% of the variance in the dependent variable was explained by our predictor variables. This can mean a few different things for our model. It could mean that there is not a strong linear relationship, or it could mean that our model is missing important variables.

The model’s performance also highlights potential limitations in the initial visualization of our data. Despite moderately strong correlations, the Mean Squared Error is relatively high (0.713), leading us to believe our data is nonlinear, as we earlier assumed. Additionally, the graph showing the relationship between predicted and actual ratings reveals that a major portion of predictions are placed near the lower end of the scale. These suggest that the linear model is not suited to visualize our data, and a need to lean towards more flexible non-linear models like clustering.

As a result, we leaned away from linear models to use K-means clustering on these same features. The resulting graph revealed three distinct clusters: a large, dense grouping that does not receive much player engagement (purple), a broad middle group that represents moderately popular games (teal), and a smaller cluster of outliers that are likely blockbuster games with incredibly high playtime and review count (yellow). These clusters indicate that our predictors could influence a game’s rating differently depending on the type of game.

To do even better, we tried using K-means++, but that resulted in no change compared to K-means because the 3 groupings we found were already separated well enough by K-means on their own. We also calculated the silhouette score with different numbers of clusters (3, 5, and 10) and received very high scores with Euclidean and Manhattan distance compared to cosine distance. Our scores were between 0.8950 and 0.9596 for Euclidean and Manhattan distance and between 0.6832 and 0.7498 for cosine distance. This reveals that our data is better suited to using geometric distance over angular distances.
We also did KNN classification using Euclidean, Manhattan, and cosine distance, which resulted in accuracy values of 0.9972, 0.9975, and 0.9972. This reiterates that our data does well when using non-linear models and geometric distance. And because our data is so well-separated, it also explains why our K-means graph didn’t change when we used K-means++.

Overall, because of the statistical significance of each predictor, the R-squared value, and the MSE value, we can be confident that our initial linear model approach failed because the data was nonlinear, not because we were missing important values. This idea is confirmed by the results of K-means clustering,  the silhouette scores, and the KNN classification accuracy.

![alt text](https://github.com/melimtz/CS506_Final_Project/blob/main/images/image2.png "Summary Statistics")

Summary Statistics

![alt text](https://github.com/melimtz/CS506_Final_Project/blob/main/images/image3.png "Silhouette Scores and KNN Accuracy")

## Conclusion

From our analyses, we learned that our predictors- playtime, number of achievements, number of games in a series, and number of reviews- do not have a linear relationship in directly predicting a game's rating. Still, they influence the category that a game may fall under. Our K-means model produced three categories of games: low-rated and unpopular, average engagement, and hits. Low-rated games had a dense cluster, indicating that they all shared common characteristics that caused their low ratings. The largest category was that of average games- those which are not highly acclaimed yet still well-liked. Because the hit cluster was so spread out, we can infer that a game becoming a hit is not entirely based on the predictors and may be partially due to luck.
