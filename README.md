# CS506 Final Project Proposal
Group Members: Megha, Anderson, Melissa, Shepherd, Mia

## Proposal (02/10)

### Player Statistics - How do player statistics impact/predict a game's rating/popularity?
  
Clear goal(s) 
  - Successfully predict average users demographics (if data is available) or popularity based on the words in the title 
  - Successfully predict metacritic rating based on pricing
  - Successfully predict when a game would be updated based on the rating
  - Successfully predict amount of players based on the date released
  - Successfully predict RAWG user rating based on metacritic rating
    
What data needs to be collected and how you will collect it (e.g. scraping xyz website or polling students).
  - Basic Gaming Data
    	- Collect it by pulling from a Kaggle data source that has compiled it into a CSV
      - RAWG API: https://rawg.io/apidocs 
      - Kaggle: https://www.kaggle.com/datasets/jummyegg/rawg-game-dataset 
  - Pricing Data
      - Collect it by pulling from a Kaggle data source that has compiled it into a CSV
      - Kaggle: https://www.kaggle.com/datasets/fronkongames/steam-games-dataset 
  We can then take the intersection of both data sources to do our analysis

How you plan on modeling the data (e.g. clustering, fitting a linear model, decision trees, XGBoost, some sort of deep learning method, etc.).
  Linear regression model
  
How do you plan on visualizing the data? (e.g. interactive t-SNE plot, scatter plot of feature x vs. feature y). 
  Linear regression model. Use a scatter plot to visualize the data points and line of best fit. We will look for patterns based on the graph.
  * From our current understanding, a regression model would be sufficient because many of the variables in our set are quantitative (amount of players, RAWG rating, etc) and we are trying to predict a numerical value. As far as visualization, it would be best to create a scatter plot to see which factors contribute most to the metrics we want to explore. However, if we see that the data does not fit well with a linear model, we would be open to a clustering approach instead (ex. Finding top-grossing games in the set and using a cluster model to determine which features are most consistent amongst some of the most successful games). A lot of our analysis would be focused on finding patterns and correlations to make predictions about the most successful games in the data set.
  
What is your test plan? (e.g. withhold 20% of data for testing, train on data collected in October and test on data collected in November, etc.).
  Our plan is to split our data set into 80-20. 80% will be used for training and 20% will be used for testing.

Data Set: https://www.kaggle.com/datasets/jummyegg/rawg-game-dataset 
Data set with steam games: https://www.kaggle.com/datasets/fronkongames/steam-games-dataset


## Midterm Report (03/31)

### Data Processing

We started with 3 potential data sets: RAWG and Steam datasets from Kaggle and a Steam API. We began cleaning the data on the two Kaggle datasets by putting both into data frames and cleaning any NaN values by removing them. This step determined which dataset we would use because the Steam dataset ended up having NaNs scattered throughout all rows in different columns, making tracing and removing them impossible without removing every row. The RAWG cleaned up much better, as most NaNs were concentrated into one column, and removing that column significantly improved the quality of the data.

Our team created a class that would allow us to access Steam’s Web API. By doing so, we would get around the issue that the dataset from Kaggle had. It would retrieve 90k+ games and put it into a CSV file. However, the Steam WebAPI has its limitations where it is only able to make a limited amount of requests per day. To get around this, our team would need more time to modify the code and have a delay of some sort to gather all the data of the 90k+ games. We would use this data in support of our models and can cross-reference them. In gathering the data of games this way we can get better results with Steam’s API. In the GitHub repo, there is a file called steam_games.csv that we were able to extract from 100 games using this API. The columns include game_name, price, achievements, total_reviews, positive_reviews, negative_reviews, and current_players.

Next, we built a correlation matrix to determine the correlation between the predictors and it is the first image in the Data Visualization step below. The specific columns we kept were: rating, playtime, added_status_owned, achievements_count, game_series_count, and reviews_count. 

Each predictor seemed to have a decent correlation with each other. However, the correlation between added_status_owned and reviews_count was very high, so we decided to remove added_status_owned because the number of reviews would likely influence the rating of a game much more. That final correlation matrix is listed as the second image in the Data Visualization step below.

The correlation coefficients between each predictor seem steady, and everything seems evenly correlated with the rating, meaning that these predictors should be suitable in our model.

### Data Visualization 

![alt text]( "Correlation Matrix (V1)")
Correlation Matrix (Version 1)

![alt text]( "Correlation Matrix (V2)")
Correlation Matrix (Version 2)

![alt text]( "Linear Regression Model")
Linear Regression Model

![alt text]( "K Means Clustering Model")
K Means Clustering Model

### Data Modeling

To model our data findings, we used three separate data models: a correlation matrix, a linear regression model, and a k-means clustering model. We first used the correlation matrix to determine the correlation between the predictors to then use that knowledge to decide the predictors we would use in our following data models. For our first correlation matrix’s predictors, we chose: a game’s average rating (rating), a game’s total playtime (playtime), the number of game copies owned (added_status_owned), the achievements count (achievment_count), the number of games in a series (game_series_count), and the reviews count (reviews_count). In our first correlation matrix, each predictor had a relatively stable correlation with each other; however, the correlation between added_status_owned and reviews_count was very high, so we decided to remove added_status_owned because the number of reviews would likely influence the rating of a game much more. After removing the number of game copies owned (added_status_owned), we were left with rating, playtime, achievements_count, game_series_count, and reviews_count. 

After carefully selecting our predictors, we used the data we processed previously to create a multiple linear regression model to show the relation between our predicted ratings of games and the actual ratings of games. We chose the dependent variable to be rating and the independent variables to be playtime, achievement_count, game_series_count, and reviews_count. We then created a new dataset of predicted values based on the multiple linear regression model, which we used to compare the predicted rating to the linear regression graph of the actual rating. We additionally used k-means clustering to create a clustering model using our selected features: playtime, achievements_count, game_series_count, and reviews_count. Given the data features, we used the k-means clustering method to create 3 main clusters to show the groupings of the popularity of games. 

### Prelimary Results / Findings

Our initial data modeling gives us insight into the relationships between players' statistics and a game’s rating/popularity. We used a multiple linear regression model to predict RAWG user ratings based on variables such as playtime, achievements count, game series count, and reviews count. The model confirms that all predictors have statistical significance (p < 2e-16). It is important to note that playtime had the most significant effect on predicted rating, followed by the number of reviews. This tells us that user-led metrics are more influential to a game’s rating than its innate metrics, like the number of achievements it has.

However, the model’s performance highlights potential limitations in the initial visualization of our data. Despite moderately strong correlations, the Mean Squared Error is relatively high (0.713), leading us to believe our data is non-linear. Additionally, the graph showing the relationship between predicted and actual ratings reveals that a major portion of predictions are placed near the lower end of the scale. These suggest that the linear model is not suited to visualize our data and a need to lean towards more flexible non-linear models like clustering. 

To better understand our data, we used K-means clustering on these same features. The resulting graph revealed three distinct clusters: a large, dense grouping that does not receive much player engagement (purple), a broad middle group that represents moderately popular games(teal), and a smaller cluster of outliers that are likely blockbuster games with incredibly high playtime and review count (yellow). These clusters indicate that our predictors could influence a game’s rating differently depending on the type of game.
