# CS506 Final Project Proposal
Group Members: Megha, Anderson, Melissa, Shepherd, Mia

2/3/2025

Description of the project:
  Title's Impact on Popularity: How do the words in the title impact how popular the game is among certain demographics 
  
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
  
What is your test plan? (e.g. withhold 20% of data for testing, train on data collected in October and test on data collected in November, etc.).
  Our plan is to split our data set into 80-20. 80% will be used for training and 20% will be used for testing.

Data Set: https://www.kaggle.com/datasets/jummyegg/rawg-game-dataset 
Data set with steam games: https://www.kaggle.com/datasets/fronkongames/steam-games-dataset


