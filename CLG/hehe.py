# Expanded Notes: Array-Oriented Programming with NumPy

import numpy as np

# 7.2 Creating Arrays from Existing Data
# Example: Basic array creation
# Notes: Use `np.array()` to create arrays from Python lists or tuples. Arrays must have consistent data types.
array1 = np.array([10, 20, 30, 40])
print("Array 1:", array1)

# Example: Creating a 2D array
# Notes: Arrays can have multiple dimensions defined by nested sequences.
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2:\n", array2)

# Self-Check: Verify array creation
# Question: What happens if you try to create an array with mixed data types, e.g., [1, 'a']?
# Answer: NumPy will convert all elements to a common data type (string in this case).
mixed_array = np.array([1, 'a'])
print("Mixed Array:", mixed_array)

# 7.3 Array Attributes
# Checking dimensions, shape, and data type
# Notes: Use `.ndim` for dimensions, `.shape` for size of each dimension, and `.dtype` for data type of elements.
print("Dimensions:", array2.ndim)  # Output: 2
print("Shape:", array2.shape)      # Output: (2, 3)
print("Data type:", array2.dtype)  # Output: int64 (or platform-dependent integer type)

# Self-Check: Attributes
# Question: How can you find the total number of elements in an array?
# Answer: Use the `.size` attribute.
print("Total Elements:", array2.size)

# 7.4 Filling Arrays with Specific Values
# Arrays filled with zeros
# Notes: Use `np.zeros()` for arrays initialized with 0s.
zeros_array = np.zeros((2, 3))
print("Zeros Array:\n", zeros_array)

# Arrays filled with ones
# Notes: Use `np.ones()` for arrays initialized with 1s.
ones_array = np.ones((3, 2))
print("Ones Array:\n", ones_array)

# Arrays filled with a specific value
# Notes: Use `np.full()` to create arrays with a custom fill value.
full_array = np.full((2, 2), 7)
print("Full Array:\n", full_array)

# Self-Check: Array Filling
# Question: How would you create a 3x3 array filled with the value 5?
# Answer:
five_array = np.full((3, 3), 5)
print("Five Array:\n", five_array)

# 7.5 Creating Arrays from Ranges
# Using arange for integer sequences
# Notes: Use `np.arange()` for evenly spaced integer sequences, similar to Python's range().
range_array = np.arange(0, 10, 2)
print("Range Array:", range_array)

# Using linspace for evenly spaced floating-point numbers
# Notes: Use `np.linspace()` for precise control over the number of elements.
linspace_array = np.linspace(0.0, 1.0, num=5)
print("Linspace Array:", linspace_array)

# Self-Check: Ranges
# Question: How does `arange` handle floating-point steps?
# Answer: Floating-point rounding may cause unexpected results; use `linspace` for precise control.

# 7.6 Performance Comparison: Lists vs. Arrays
# Notes: NumPy arrays are optimized for numerical computations, reducing execution time significantly.
import time
start = time.time()
sum([x for x in range(10_000_000)])  # Using Python lists
end = time.time()
print("List sum time:", end - start)

start = time.time()
np.arange(10_000_000).sum()  # Using NumPy arrays
end = time.time()
print("NumPy sum time:", end - start)

# Self-Check: Performance
# Question: Why are NumPy arrays faster than lists for numerical operations?
# Answer: NumPy arrays use contiguous memory and optimized C routines.

# 7.7 Array Operators
# Element-wise operations
# Notes: Arithmetic operations in NumPy are applied element-wise by default.
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print("Addition:", array_a + array_b)
print("Multiplication:", array_a * array_b)
print("Power:", array_a ** 2)

# Broadcasting example
# Notes: Broadcasting enables arithmetic operations between arrays of different shapes.
array_c = np.array([[1, 2, 3], [4, 5, 6]])
array_d = np.array([1, 2, 3])
print("Broadcasting Addition:\n", array_c + array_d)

# Self-Check: Broadcasting
# Question: Can broadcasting work with arrays of incompatible shapes?
# Answer: No, it raises a ValueError if the shapes are incompatible.

# 7.8 NumPy Calculation Methods
# Aggregate operations
# Notes: NumPy provides built-in functions for aggregate calculations like `sum()`, `mean()`, and `std()`.
numbers = np.array([1, 2, 3, 4, 5])
print("Sum:", numbers.sum())
print("Mean:", numbers.mean())
print("Standard Deviation:", numbers.std())

# Self-Check: Calculations
# Question: How would you calculate the product of all elements in an array?
# Answer: Use the `.prod()` method.
print("Product:", numbers.prod())

# 7.9 Universal Functions (ufuncs)
# Applying trigonometric functions
# Notes: Universal functions apply operations element-wise efficiently.
angles = np.array([0, np.pi / 2, np.pi])
print("Sin values:", np.sin(angles))
print("Cos values:", np.cos(angles))

# Comparison functions
# Notes: Logical comparisons return arrays of boolean values.
comparison = np.greater(array_a, array_b)
print("Comparison (A > B):", comparison)

# Bitwise operations
# Notes: Bitwise operators are supported for boolean and integer arrays.
bitwise_array1 = np.array([1, 0, 1], dtype=bool)
bitwise_array2 = np.array([0, 1, 1], dtype=bool)
print("Bitwise AND:", np.bitwise_and(bitwise_array1, bitwise_array2))

# Self-Check: Universal Functions
# Question: What does `np.sqrt([-1, 0, 1])` return?
# Answer: It raises a warning and returns `nan` for invalid operations.

# 7.10 Indexing and Slicing
# Accessing elements in a 2D array
# Notes: Use standard indexing and slicing syntax for multi-dimensional arrays.
matrix = np.array([[10, 20, 30], [40, 50, 60]])
print("Element at row 0, column 1:", matrix[0, 1])  # Output: 20

# Slicing a 2D array
print("First row:", matrix[0, :])  # Output: [10, 20, 30]
print("First column:", matrix[:, 0])  # Output: [10, 40]

# Advanced indexing
# Notes: Use lists or arrays for advanced indexing to select specific elements.
indices = [0, 2]
print("Selected elements:", matrix[0, indices])  # Output: [10, 30]

# Self-Check: Indexing
# Question: How do you select every other element from the first row?
# Answer: Use slicing with a step: `matrix[0, ::2]`

# 7.11 Views: Shallow Copies
# Notes: A view is a shallow copy; modifying the view affects the original array.
original = np.array([1, 2, 3, 4])
view = original.view()
view[0] = 99
print("Original after modifying view:", original)  # Output: [99, 2, 3, 4]

# 7.12 Deep Copies
# Notes: A deep copy is an independent copy; changes to the copy do not affect the original array.
copy = original.copy()
copy[0] = 100
print("Original after modifying copy:", original)  # Output: [99, 2, 3, 4]

# Self-Check: Copies
# Question: What is the difference between `view()` and `copy()`?
# Answer: `view()` reflects changes in the original array; `copy()` does not.

# 7.13 Reshaping and Transposing
# Notes: Use `reshape()` to change dimensions and `.T` to transpose an array.
reshaped = np.arange(1, 21).reshape(4, 5)
print("Reshaped Array:\n", reshaped)

transposed = reshaped.T
print("Transposed Array:\n", transposed)

# Flattening arrays
# Notes: `flatten()` creates a copy; `ravel()` creates a view if possible.
flattened = reshaped.flatten()
print("Flattened Array:", flattened)

raveled = reshaped.ravel()
print("Raveled Array:", raveled)

# Self-Check: Reshaping
# Question: What is the difference between `flatten()` and `ravel()`?
# Answer: `ravel()` returns a view if possible; `flatten()` always returns a copy.

# 7.14 pandas Integration
# Notes: pandas integrates seamlessly with NumPy arrays for tabular data manipulation.
import pandas as pd
# Creating a pandas Series
series = pd.Series(np.array([10, 20, 30, 40]))
print("Pandas Series:\n", series)

# Creating a pandas DataFrame
dataframe = pd.DataFrame(np.arange(1, 10).reshape(3, 3), columns=['A', 'B', 'C'])
print("Pandas DataFrame:\n", dataframe)

# Self-Check: pandas Integration
# Question: How can you convert a pandas DataFrame back to a NumPy array?
# Answer: Use the `.values` attribute or `.to_numpy()` method.

# Exception Handling Example
# Notes: NumPy raises exceptions like `ValueError` for invalid operations such as reshaping with mismatched dimensions.
try:
    invalid_reshape = np.arange(10).reshape(3, 4)  # Mismatched dimensions
except ValueError as e:
    print("Reshape Error:", e)

# Handling large arrays
# Notes: Use `np.set_printoptions()` to customize the display of large arrays.
large_array = np.arange(10000)
print("Large Array Display:", large_array)  # Truncated by default

# Self-Check: Large Arrays
# Question: How can you force NumPy to display the full content of a large array?
# Answer: Use `np.set_printoptions(threshold=np.inf)`.
 