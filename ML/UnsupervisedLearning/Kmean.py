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
grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4])
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




