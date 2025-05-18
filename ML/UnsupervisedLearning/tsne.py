# Dimensionality Reduction
#  To visualize a dataset with many features (that is, many dimensions), we’ll first reduce the data to two or three dimensions. This requires an unsupervised machine learning technique called dimensionality reduction

# Dimensionality reduction helps in other ways too. When we have a lot of data with many features (or dimensions), training machine learning models can take a long time — even days or weeks. Also, it's hard for people to understand or visualize data with many dimensions. This problem is known as the curse of dimensionality.

# If some features are very similar (highly correlated), we can remove some of them using dimensionality reduction. This can make training faster. But, doing this might also slightly reduce how accurate the model is.


from sklearn.datasets import load_digits

digits = load_digits()
# * Creating a TSNE Estimator for Dimensionality Reduction
# t-distributed Stochastic Neighbor Embedding (t-SNE)10 to analyze a dataset’s features and reduce them to the specified number of dimensions.

from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=11)
# This creates a TSNE object for reducing a dataset’s features to two dimensions, as specifiedby the keyword argument n_components.


# * Transforming the Digits Dataset’s Features into Two Dimensions
# Dimensionality reduction in scikit-learn typically involves two steps—training the estimator with the dataset, then using the estimator to transform the data into the specified number of dimensions.
# These steps can be performed separately with the TSNE methods fit and transform, or they can be performed in one statement using the fit_transform method

reduced_data = tsne.fit_transform(digits.data)

print(reduced_data.shape)
# When the method completes its task, it returns an array with the same number of rows as digits.data, but only two columns.

# * Visualizing the Reduced Data
# todo: 


#  !(True/False) Unsupervised machine learning and visualization can help you get to know your data by finding patterns and relationships among unlabeled samples.
# ?Answer: True.


