import pandas as p
grades1 = p.Series([1, 2, 3])
#print(grades1, "List")
grades2 = p.Series((1, 2, 3))
#print(grades2, "Tuple")
grades3 = p.Series({1: 'a', 2: 'b'})
#print(grades3, "Dict")

grades4 = p.Series(grades1)
#print(grades4, "Series")


#The initializer also may be a tuple, a dictionary, an array, another Series or a single value.

# Pandas displays a Series in two-column format with the indices left aligned in the left column and the values right aligned in the right column. After listing the Series elements, pandas shows the data type (dtype) of the underlying array’s elements

#print(p.Series(10, range(5)))
# The second argument is a one-dimensional iterable object (such as a list, an array or a range) containing the Series’ indices.

grades = p.Series([87, 100, 94])
print(grades[0], grades[2])

#producing Descriptive statistics for a series
grades.count()
grades.mean()
grades.min()
grades.max()


