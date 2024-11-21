from sklearn.datasets import load_iris 
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt 
import numpy as np 

data = load_iris() 
X = data.data 

kmeans = KMeans(n_clusters=3, random_state=42) 
kmeans.fit(X) 

print(f"K-Means Inertia: {kmeans.inertia_}") 

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis') 
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', label='Centroids') 
plt.xlabel(data.feature_names[0]) 
plt.ylabel(data.feature_names[1]) 
plt.legend() 
plt.title("K-Means Clustering") 
plt.show() 
