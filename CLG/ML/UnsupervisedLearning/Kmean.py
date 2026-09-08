# the simplest unsupervised machine learning algorithms— k-means clustering.

# The algorithm organizes samples into the number of clusters you specify in advance, using distance calculations similar to the k-nearest neighbors clustering algorithm. Each cluster of samples is grouped around a centroid—the cluster’s center point.


# Initially, the algorithm chooses k centroids at random from the dataset’s samples.

# Then the remaining samples are placed in the cluster whose centroid is the closest. The centroids are iteratively recalculated and the samples re-assigned to clusters until, for all clusters, the distances from a given centroid to the samples in its cluster are minimized.


# * The algorithm’s results are:
# • a one-dimensional array of labels indicating the cluster to which each sample
# belongs and
# • a two-dimensional array of centroids representing the center of each cluster.

#loading data

from sklearn.datasets import load_iris

iris = load_iris()

print(iris.data.shape)# (150, 4)
print(iris.target.shape)#(150,)
print(iris.target_names)
print(iris.feature_names)



# *Exploring the Iris Dataset: Descriptive Statistics with Pandas
import pandas as pd
pd.set_option('display.max_columns', 5)
pd.set_option('display.width', None)

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

iris_df['species'] = [iris.target_names[i] for i in iris.target]
#add a column containing each sample’s species name. The list comprehension in the following snippet uses each value in the target array to look up the corresponding species name in the target_names array:
pd.set_option('display.precision', 2)

print(iris_df.head())


# *Visualizing the Dataset with a Seaborn pairplot

# Seaborn function pairplot to create a grid of graphs plotting each feature against itself and the other specified features

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(font_scale=1.2)
sns.set_style('whitegrid')

# grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4], hue='species')


# *Displaying the pairplot in One Color
#grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4])
# plt.show()

# ?1 (Fill-In) Seaborn’s function creates a grid of scatter plots showing features against one another.
# Answer: pairplot.
# ?2 (True/False) A plot of a feature’s distribution shows the feature’s range of values (leftto- right) and the number of samples with those values (top-to-bottom).
# Answer: True.

# *Using a KMeans Estimator
# The KMeans estimator hides from you the algorithm’s complex mathematical details, making it straightforward to use.


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=11)

# The keyword argument n_clusters specifies the k-means clustering algorithm’s hyperparameter k, which KMeans requires to calculate the clusters and label each sample

# * Fitting the Model

kmeans.fit(iris.data)

# When the training completes, the KMeans object contains:
# • A labels_ array with values from 0 to n_clusters - 1 (in this example, 0–2),indicating the clusters to which the samples belong.
# • A cluster_centers_ array in which each row represents a centroid.

# Comparing the Computer Cluster Labels to the Iris Dataset’s Target Values


print(kmeans.labels_[0:50])
print(kmeans.labels_[50:100])
print(kmeans.labels_[100:150])


# *Dimensionality Reduction with Principal Component Analysis

# PCA estimator (from the sklearn.decomposition module) to perform dimensionality reduction. This estimator uses an algorithm called principal component analysis14 to analyze a dataset’s features and reduce them to the specified number of dimensions.

from sklearn.decomposition import PCA
pca = PCA(n_components=2, random_state=11)

# 4 dimensions down to 2 dimensions.
# *Transforming the Iris Dataset’s Features into Two Dimensions
# Train the estimator and produce the reduced data by calling the PCA estimator’s methods fit and transform methods
pca.fit(iris.data)

iris_pca = pca.transform(iris.data)

# When the method completes its task, it returns an array with the same number of rows as iris.data, but only two columns.
print(iris_pca.shape)#(150, 2) from (150, 4)

# * Visualizing the Reduced Data
# todo:
iris_pca_df = pd.DataFrame(iris_pca, columns=['comp1', 'comp2'])

iris_pca_df['species'] = iris_df.species


#axes = sns.scatterplot(iris_pca_df, x='comp1', y='comp2', hue='species', legend='brief', palette='cool')

# plt.show()


iris_centers = pca.transform(kmeans.cluster_centers_)
# This statement reduces the centroids to the number of dimensions specified when the pca object was created. In the Iris case study, we were able to plot the reduced centroids in two dimensions at the centers of their corresponding clusters.
dots = plt.scatter(iris_centers[:,0], iris_centers[:, 1], s=100, c='k')

plt.show()

# The keyword argument s=100 specifies the size of the plotted points, and the keyword argument c='k' specifies that the points should be displayed in black. 


# ?Each centroid in a KMeans object’s cluster_centers_ array has the same number of features as the original dataset.
#Answer: True.


# * Choosing the Best Clustering Estimator
from sklearn.cluster import DBSCAN, MeanShift, SpectralClustering, AgglomerativeClustering

estimators = {
    'KMeans': kmeans,
    'DBSCAN': DBSCAN(),
    'MeanShift': MeanShift(),
    'SpectralClustering': SpectralClustering(n_clusters=3),
    'AgglomerativeClustering': AgglomerativeClustering(n_clusters=3)
}


import numpy as np

for name, estimator in estimators.items():
    estimator.fit(iris.data)
    print(f'\n{name}:')
    for i in range(0, 101, 50):
        labels, counts = np.unique(
        estimator.labels_[i:i+50], return_counts=True)
        print(f'{i}-{i+50}:')
        for label, count in zip(labels, counts):
            print(f' label={label}, count={count}')


# We’re running KMeans here on the small Iris dataset. If you experience performance problems with KMeans on larger datasets, consider using the MiniBatchKMeans estimator. The scikit-learn documentation indicates that MiniBatchKMeans is faster on large datasets and the results are almost as good.

# Though these algorithms label every sample, the labels simply indicate the clusters.What do you do with the cluster information once you have it? If your goal is to use the data in supervised machine learning, typically you’d study the samples in each cluster to try to determine how they’re related and label them accordingly.
