# The data we’ll use is a time series in which the observations are ordered by year. Univariate
# time series have one observation per time, such as the average of the January high temperatures
# in New York City for a particular year. Multivariate time series have two or more
# observations per time, such as temperature, humidity and barometric pressure readings in
# a weather application.



# Given a collection of values representing an independent variable
# (the month/year combination) and a dependent variable (the average high temperature
# for that month/year), simple linear regression describes the relationship between these
# variables with a straight line, known as the regression line.
 # ex 
c = lambda f: 5 / 9 * (f - 32)
temps = [(f, c(f)) for f in range(0, 101, 10)]


import pandas as pd
import matplotlib.pyplot as plt
temps_df = pd.DataFrame(temps, columns=["Fahrenheit", 'Celsius'])
axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')
y_label = axes.set_ylabel('Celsius')
plt.show()

# Function linregress from the SciPy’s stats Module
# Simple linear regression determines the slope (m) and intercept (b) of a straight line that
# best fits your data.

# The simple linear regression algorithm iteratively adjusts the slope and intercept and, for
# each adjustment, calculates the square of each point’s distance from the line. The “best fit”
# occurs when the slope and intercept values minimize the sum of those squared distances.
# This is known as an ordinary least squares calculation.21
# The SciPy (Scientific Python) library is widely used for engineering, science and
# math in Python. This library’s linregress function (from the scipy.stats module) performs
# simple linear regression for you. After calling linregress, you’ll plug the resulting
# slope and intercept into the y = mx + b equation to make predictions.


