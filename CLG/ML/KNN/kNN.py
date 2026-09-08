

# In machine learning, a model implements a machine-learning algorithm. In scikit-learn, models are called estimators.

# Those you specify in advance when you create the scikit-learn estimator object that represents the model. The parameters specified in advance are called hyperparameters.

# here k is is a hyperparameter 

# The process of choosing the best value of k for the k-nearest neighbors algorithm is called : Answer: hyperparameter tuning.


# loading data
from sklearn.datasets import load_digits
digits = load_digits()

# print(digits.DESCR)
# The data array contains the 1797 samples (the digit images), each with 64 features, having values in the range 0–16, representing pixel intensities.

# print(digits.target[::100]) #[0 4 1 7 4 8 2 2 4 4 1 9 7 3 2 1 2 5]
# target array contains the images’ labels—that is, the classes indicating which digit each image represents.

# print(digits.data.shape)# (1797, 64)
# print(digits.target.shape)# (1797,)

# Each image is two-dimensional—it has a width and a height in pixels.


print(digits.images[10])
print(digits.target[0])


# Visualizing the Data
# Creating the Diagram
import matplotlib.pyplot as plt


figure, axes = plt.subplots(nrows = 4, ncols= 6, figsize= (6, 4))
# plt.show()


# Displaying Each Image and Removing the Axes Labels
for item in zip(axes.ravel(), digits.images, digits.target):
    axes, image, target = item
    axes.imshow(image, cmap = plt.cm.gray_r)# Calls the Axes object’s imshow method to display one image
    # axes.set_xticks([]) #Calls the Axes object’s set_xticks and set_yticks methods with empty lists to indicate that the x- and y-axes should not have tick marks.
    # axes.set_xticks([])
    # axes.set_title(target) # method to display the target value above the image—this shows the actual value that the image represents.

plt.tight_layout()
# plt.show()

# NumPy array method ravel creates a one-dimensional view of a multidimensional array. Also, recall that each tuple zip produces contains elements from the same index in each of zip’s arguments and that argument with the fewest elements determines how many tuples zip returns.
# we call tight_layout to remove the extra whitespace at the Figure’s top, right, bottom and left, so the rows and columns of digit images can fill more of the Figure.
# The process of familiarizing yourself with your data is called . Answer: data exploration.

# Splitting the Data for Training and Testing

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=11)


# print(x_train.shape)
# print(x_test.shape)
# by default, train_test_split
# reserves 75% of the data for training and 25% for testing:

# If you only give the model X_train without y_train, it's like asking the model to learn without ever being told the right answer — it would be unsupervised learning, not supervised.

# with test_size..... and this specifies 20% of the data is for testing,
#x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=11, test_size= 0.20)


# Not all dataset, It’s important to set aside a portion of your data for testing, so you can evaluate a model’s performance using data that the model has not yet seen.

# creating the model:
from sklearn.neighbors import KNeighborsClassifier

## fit
knn = KNeighborsClassifier()
print(knn.fit(x_train, y_train))

# Predicting Digit Classes
# Calling the estimator’s predict method with X_test as an argument returns an array containing the predicted class of each test image:

predicted = knn.predict(X=x_test)
print(predicted[:20])

expected = y_test
print(expected[:20])

# incorrect prediction:
wrong_predictions = []

for i, j in zip(predicted, expected):
    if i != j:
        wrong_predictions.append(   ( int(i), int(j) ) )

print(wrong_predictions)

# calculate and display the prediction accuracy percentage.
accuracy = f'{(len(expected) - len(wrong_predictions)) / len(expected):.2%}'
print(accuracy)# 97.78%

# Estimator Method score
print(f'{knn.score(x_test, y_test):.2%}')# accuracy pre-defined #res:  97.78%
# The kNeighborsClassifier’s with its default k (that is, n_neighbors=5) achieved 97.78% prediction accuracy.

# Confusion Matrix
from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_true=expected, y_pred=predicted)
print(confusion)
# [[45  0  0  0  0  0  0  0  0  0]
#  [ 0 45  0  0  0  0  0  0  0  0]
#  [ 0  0 54  0  0  0  0  0  0  0]
#  [ 0  0  0 42  0  1  0  1  0  0]
#  [ 0  0  0  0 49  0  0  1  0  0]
#  [ 0  0  0  0  0 38  0  0  0  0]
#  [ 0  0  0  0  0  0 42  0  0  0]
#  [ 0  0  0  0  0  0  0 45  0  0]
#  [ 0  1  1  2  0  0  0  0 39  1]
#  [ 0  0  0  0  1  0  0  0  1 41]]

# The correct predictions are shown on the diagonal from top-left to bottom-right. This is called the principal diagonal. The nonzero values that are not on the principal diagonal indicate incorrect predictions

# Each row represents one distinct class—that is, one of the digits 0–9. The columns
# within a row specify how many of the test samples were classified into each distinct class.
# For example, row 0: [45, 0, 0, 0, 0, 0, 0, 0, 0, 0] represents the digit 0 class
## According to row 0, 45 test samples were classified as the digit 0, and none of the test samples were misclassified as any of the digits 1 through 9. 100% of the 0s were correctly predicted.

#consider row 8 which represents the results for the digit 8:
# [ 0, 1, 1, 2, 0, 0, 0, 0, 39, 1]
# • The 1 at column index 1 indicates that one 8 was incorrectly classified as a 1.
# • The 1 at column index 2 indicates that one 8 was incorrectly classified as a 2.
# • The 2 at column index 3 indicates that two 8s were incorrectly classified as 3s.
# • The 39 at column index 8 indicates that 39 8s were correctly classified as 8s.
# • The 1 at column index 9 indicates that one 8 was incorrectly classified as a 9.

# So the algorithm correctly predicted 88.63% (39 of 44) of the 8s. Earlier we saw that the overall prediction accuracy of this estimator was 97.78%. The lower prediction accuracy for 8s indicates that they’re apparently harder to recognize than the other digits.


from sklearn.metrics import classification_report
names = [str(digit) for digit in digits.target_names]
print(classification_report(expected, predicted, target_names= names))

# Visualizing the Confusion Matrix
# A heat map displays values as colors, often with values of higher magnitude displayed as more intense colors.

import pandas as pd
confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))
import seaborn as sns
axes = sns.heatmap(confusion_df, annot=True, cmap='nipy_spectral_r')
#plt.show()


# K-Fold Cross-Validation
# K-fold cross-validation splits the dataset into k equal-size folds (this k is unrelated to k in the k-nearest neighbors algorithm). You then repeatedly train your model with k – 1 folds and test the model with the remaining fold.

# KFold Class
from sklearn.model_selection import KFold
kfold = KFold(n_splits=10, random_state=11, shuffle=True)

# Using the KFold Object with Function cross_val_score
from sklearn.model_selection import cross_val_score
scores = cross_val_score(estimator=knn, X=digits.data, y=digits.target, cv=kfold)
print(scores)
# cv=kfold, which specifies the cross-validation generator that defines how to split the samples and targets for training and testing.
# Function cross_val_score returns an array of accuracy scores—one for each fold.


# now getting over all model's accuracy
print(scores.mean())# use :.2% not 2f
print(scores.std())


# Running Multiple Models to Find the Best One
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

estimators = {
    'KNeighborsClassifier': knn,
    'SVC': SVC(gamma='scale'),
    'GaussianNB': GaussianNB()
}

# for est_name, est_obj in estimators.items():
#     kfold = KFold(n_splits=10, random_state=11, shuffle=True)
#     scores = cross_val_score(estimator=est_obj, X=digits.data, y=digits.target, cv=kfold)
#     print(est_name, f"Mean: {scores.mean():.2%}", f"Deviation: {scores.std():.2%}")




# The following loop creates KNeighborsClassifiers with odd k values from 1 through 19 (again, we use odd k values in kNN to avoid ties) and performs k-fold cross-validation on each.

for k in range(1, 40, 10):
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(estimator=knn, X=digits.data, y=digits.target, cv=kfold)
    print(f"Mean: {scores.mean():.2%}", f"Deviation: {scores.std():.2%}")
