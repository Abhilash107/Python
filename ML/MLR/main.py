 # *Loading data
from sklearn.datasets import fetch_california_housing

california = fetch_california_housing()

# • Number of Instances—this dataset contains 20,640 samples.
# • Number of Attributes—there are 8 features (attributes) per sample.
# • Attribute Information—feature descriptions.
# • Missing Attribute Values—none are missing in this dataset.

# print(california.DESCR )

print(california.data.shape)#(20640, 8)
print(california.target.shape)#(20640,)
print(california.feature_names)#['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

# *exploring data
import pandas as pd
pd.set_option('display.precision', 4)#'precision' is the maximum number of digits to display to the right of each decimal point.
pd.set_option('display.max_columns', 9)#'max_columns' is the maximum number of columns to display when you output the DataFrame’s string representation.
pd.set_option('display.width', None)


california_df = pd.DataFrame(california.data, columns=california.feature_names)
#The first snippet below creates the initial DataFrame using the data in california.data and with the column names specified by california.feature_names.

california_df['MedHouseValue'] = pd.Series(california.target)
# The second statement adds a column for the median house values stored in california.target: 

# print(california_df.head())
# print(california_df.describe())



# *Visualizing the Features

sample_df = california_df.sample(frac=0.1, random_state=17)
# The keyword argument frac specifies the fraction of the data to select (0.1 for 10%), and the keyword argument random_state enables you to seed the random number generator.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=2)

sns.set_style('whitegrid')

# for feature in california.feature_names:
#     plt.figure(figsize=(16, 9)) #the snippet first creates a 16-inch-by-9-inch Matplotlib Figure
#     sns.scatterplot(data=sample_df, x=feature, y='MedHouseValue', hue='MedHouseValue', palette='cool', legend=False)
    
# plt.show()# 8 graphs as we r plotting features against target


# *Splitting the Data for Training and Testing

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(california.data, california.target, random_state=11)

print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

# *Training the model

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)


for i, name in enumerate(california.feature_names):
    print(f'{name} : {lr.coef_[i]}')



# ?By default, a LinearRegression estimator uses all the features in the dataset’s data array to perform a multiple linear regression. An error occurs if any of the features are categorical rather than numeric.

# If a dataset contains categorical data, you either must preprocess the categorical features into numerical ones (which you’ll do in the next chapter) or must exclude the categorical features from the training process

# ?For positive coefficients, the median house value increases as the feature value increases.
# ?For negative coefficients, the median house value "decreases" as the feature value increases.

# *y = m1x1 + m2x2 + … mnxn + b


# !1 (True/False) By default, a LinearRegression estimator uses all the features in the dataset to perform a multiple linear regression.
# ?Answer: False. By default, a LinearRegression estimator uses all the numeric features in the dataset to perform a multiple linear regression. An error occurs if any of the features are categorical rather than numeric. Categorical features must be preprocessed into numerical ones or must be excluded from the training process.


# * Testing the Model

predicted = lr.predict(X_test)

expected = y_test

print(predicted[:10])
print(expected[:10])

# ?With classification, we saw that the predictions were distinct classes that matched existing classes in the dataset. With regression, it’s tough to get exact predictions, because you have continuous outputs.

# Visualizing the Expected vs. Predicted Prices
# todo: 









# * Regression Model Metrics
#for comparing estimators to choose the best one(s) for your particular study.

# Among the many metrics for regression estimators is the model’s coefficient of determination,
# which is also called the R2 score. To calculate an estimator’s R2 score, call the
# sklearn.metrics module’s r2_score function with the arrays representing the expected
# and predicted results

from sklearn import metrics
print(metrics.r2_score(expected, predicted))


# To calculate an estimator’s mean squared error, call function mean_squared_error (from
# module sklearn.metrics) with the arrays representing the expected and predicted results
print(metrics.mean_squared_error(expected, predicted))
# ?imp: the one with the value closest to 0 best fits your data.

# An R2 score of indicates that an estimator perfectly predicts the dependent variable’s value, given the independent variable(s) value(s).
# Answer: 1.0.

# * Choosing the Best Model

from sklearn.linear_model import ElasticNet, Lasso, Ridge

estimators = {
    'LR': lr,
    'ElasticNet': ElasticNet(),
    'Lasso': Lasso(),
    'Ridge': Ridge()
}

from sklearn.model_selection import KFold, cross_val_score

for est_name, est_val in estimators.items():
    kFold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=est_val, X=california.data, y=california.target, cv=kFold, scoring='r2')
    print(f'{scores.mean():.2f}')


