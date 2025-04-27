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

while y_1 < 40.0:
    x_1 += 1
    y_1 = m * x_1 + c

print(x_1)