import pandas as pd
import matplotlib.pyplot as plt

nyc = pd.read_csv(r'E:\Languages\Python\OOPS\SLR\ave_hi_nyc_jan_1895-2018.csv')

print(nyc.head())
print(nyc.tail())

nyc.columns = ['Date', 'Temperature', 'Anomaly']
print(nyc.head(3))
nyc.Date = nyc.Date.floordiv(100)
print(nyc.head(3))

#pd.set_option('precision', 2)
print(nyc.Temperature.describe())

# Forecasting Future January Average High Temperatures
# The SciPy (Scientific Python) library is widely used for engineering, science and math in
# Python. Its stats module provides function linregress, which calculates a regression
# line’s slope and intercept for a given set of data points:

from scipy import stats
l_r = stats.linregress(x=nyc.Date, y=nyc.Temperature)

print(l_r.slope)
print(l_r.intercept)
# y = mx + c; here x = year, y = temperature

m = l_r.slope
x_1 = 2019
x_2 = 1890
c = l_r.intercept
y_1 = m * x_1 + c
y_2 = m * x_2 + c
print(y_1)
print(y_2)



# Plotting the Average High Temperatures and a Regression Line


# use Seaborn’s regplot function to plot each data point with the dates on the
# x-axis and the temperatures on the y-axis. The regplot function creates the scatter plot or
# scattergram below in which the scattered blue dots represent the Temperatures for the
# given Dates, and the straight line displayed through the points is the regression line:

import seaborn as sns
sns.set_style('whitegrid')
axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)
# plt.show()

axes.set_ylim(10, 70)
# plt.show()

year = 2019
intercept = l_r.intercept
slope = l_r.slope
temp = temp = slope * year + intercept

while temp < 40.0:
    year += 1
    temp = slope * year + intercept
    

# print(year)

# Splitting the Data for Training and Testing

# use the LinearRegression estimator from sklearn.linear_model.
# By default, this estimator uses all the numeric features in a dataset, performing a multiple
# linear regression

# we perform simple linear
# regression using one feature as the independent variable. So, we’ll need to select one feature
# (the Date) from the dataset.

# When you select one column from a two-dimensional DataFrame, the result is a onedimensional
# Series.

# scikit-learn estimators require their training and testing
# data to be two-dimensional arrays (or two-dimensional array-like data, such as lists of lists
# or pandas DataFrames). To use one-dimensional data with an estimator, you must transform
# it from one dimension containing n elements, into two dimensions containing n rows
# and one column


from sklearn.model_selection import train_test_split
x_train ,x_test, y_train, y_test = train_test_split(nyc.Date.values.reshape(-1, 1), nyc.Temperature.values, random_state=11)


print(x_train.shape)
print(x_test.shape)

# Input Data:

# nyc.Date.values.reshape(-1, 1):

# This is the independent variable (feature) Date from the nyc DataFrame.
# nyc.Date.values converts the Date column into a NumPy array.
# .reshape(-1, 1) reshapes the 1D array into a 2D array with one column and as many rows as needed. This is required because scikit-learn estimators expect 2D input for features.
# Shape: (n_samples, 1).
# nyc.Temperature.values:

# This is the dependent variable (target) Temperature from the nyc DataFrame.
# nyc.Temperature.values converts the Temperature column into a NumPy array.
# Shape: (n_samples,).
# Splitting the Data:

# train_test_split splits the data into:
# x_train: Training subset of the independent variable (Date).
# x_test: Testing subset of the independent variable (Date).
# y_train: Training subset of the dependent variable (Temperature).
# y_test: Testing subset of the dependent variable (Temperature).
# Random State:

# random_state=11 ensures that the split is reproducible. Using the same random state will always produce the same split.

# Training the Model

# Scikit-learn does not have a separate class for simple linear regression because it’s just a special case of multiple linear regression

from sklearn.linear_model import LinearRegression
linear_regression = LinearRegression()

linear_regression.fit(X=x_train, y=y_train)

# After training the estimator, fit returns the estimator,

# The slope is stored in the estimator’s coeff_ attribute (m in the quation) and
# the intercept is stored in the estimator’s intercept_ attribute (b in the equation):

print(linear_regression.coef_)
print(linear_regression.intercept_)

# testing the model
predicted = linear_regression.predict(x_test)

expected = y_test

for p, e in zip(predicted[::5], expected[::5]):
    print(f'{p:.2f}, {e:.2f}')

# predicting data

#predict = (lambda x: linear_regression.coef_ * x + linear_regression.intercept_)

def predict(x):
    return linear_regression.coef_ * x + linear_regression.intercept_

print(f'{predict(2019)}')

#Visualizing the Dataset with the Regression Line

import seaborn as sns
axes = sns.scatterplot(data=nyc, x='Date', y="Temperature", hue='Temperature', palette='winter', legend=True)
plt.show()

# data, which specifies the DataFrame (nyc) containing the data to display.
# • x and y, which specify the names of nyc’s columns that are the source of the data
# along the x- and y-axes, respectively. In this case, x is the 'Date' and y is the
# 'Temperature'. The corresponding values from each column form x-y coordinate
# pairs used to plot the dots.

# • hue, which specifies which column’s data should be used to determine the dot
# colors. In this case, we use the 'Temperature' column. Color is not particularly
# important in this example, but we wanted to add some visual interest to the
# graph.

# • palette, which specifies a Matplotlib color map from which to choose the dots’ colors.

# • legend=False, which specifies that scatterplot should not show a legend for the graph—the default is True, but we do not need a legend for this example.

# now plot the regression line.
# create an array containing the minimum and maximum date values in nyc.Date.
import numpy as np
x = np.array([min(nyc.Date.values), max(nyc.Date.values)])

y = predict(x)

line = plt.plot(x, y)
plt.show()


# Overfitting/Underfitting
# When creating a model, a key goal is to ensure that it is capable of making accurate predictions
# for data it has not yet seen. Two common problems that prevent accurate predictions
# are overfitting and underfitting:
# • Underfitting occurs when a model is too simple to make predictions, based on
# its training data. For example, you may use a linear model, such as simple linear
# regression, when in fact, the problem really requires a non-linear model. For
# example, temperatures vary significantly throughout the four seasons. If you’re
# trying to create a general model that can predict temperatures year-round, a simple
# linear regression model will underfit the data.
# • Overfitting occurs when your model is too complex. The most extreme case,
# would be a model that memorizes its training data. That may be acceptable if
# your new data looks exactly like your training data, but ordinarily that’s not the
# case. When you make predictions with an overfit model, new data that matches
# the training data will produce perfect predictions, but the model will not know
# what to do with data it has never seen.


# Overfitting and Underfitting
# When creating a model, the aim is to predict unseen data accurately.

# Underfitting happens when the model is too simple, missing important patterns (e.g., using linear regression for seasonal temperature prediction).

# Overfitting happens when the model is too complex, memorizing training data and failing to generalize to new data.