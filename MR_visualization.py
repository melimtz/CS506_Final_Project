import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

#processed RAWG data
data = pd.read_csv("rawg_data_cleaned.csv")

#multiple linear reggression model
X = data[['playtime', 'achievements_count', 'game_series_count','reviews_count']]
y = data['rating']
lr = LinearRegression()
lr.fit(X, y)

#predicted rating
prediction = lr.predict(X)

#r^2 score and MSE
r2 = r2_score(y, prediction)
mse = mean_squared_error(y, prediction)

#predicted rating vs actual rating linear regression graph
plt.scatter(y, prediction, alpha=0.5)
plt.xlabel('Actual Rating')
plt.ylabel('Predicted Rating')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.grid(True)
plt.savefig("linear_reg.png")
plt.show()

#clustering model
features = ['playtime', 'achievements_count', 'game_series_count', 'reviews_count']
data_cluster = data[features]

scaler = StandardScaler()
scaled = scaler.fit_transform(data_cluster)

#kmeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled)

data_cluster['cluster'] = clusters

#clustering graph
pca = PCA(n_components=2)
X_pca = pca.fit_transform(scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis', alpha=0.6)
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.grid(True)
plt.colorbar(label='Cluster')
plt.savefig("clustering.png")
plt.show()

#KMeans++ clustering
kmeans_plusplus = KMeans(n_clusters=3, init='k-means++', n_init=20, random_state=42)
clusters_plusplus = kmeans_plusplus.fit_predict(scaled)

data_cluster['cluster_pluss'] = clusters_plusplus

# distance comparison in kmeans++ w/ silhouette scores
num_clusters = [3, 5, 10]
distance_metrics = ["euclidean", "manhattan", "cosine"]

for cluster_num in num_clusters:
    print(f"Number of clusters: {cluster_num}")
    for metric in distance_metrics:
        kmeans = KMeans(n_clusters=cluster_num, init='k-means++', n_init=10, random_state=42)
        clusters = kmeans.fit_predict(scaled)  

        ss = silhouette_score(scaled, clusters, metric=metric)
        print(f"\tSilhouette Score for KMeans ({metric} distance): {ss:.4f}")

# accuracy eval w/ distance metrics using KNN
knn_metrics = ["euclidean", "manhattan", "minkowski"]

for metric in knn_metrics:
    knn = KNeighborsClassifier(n_neighbors=5, metric=metric)
    knn.fit(scaled, clusters)
    # Evaluate accuracy with cross-validation
    scores = cross_val_score(knn, scaled, clusters, cv=5)
    print(f"Mean Accuracy for KNN ({metric} distance): {scores.mean():.4f}")