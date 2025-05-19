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