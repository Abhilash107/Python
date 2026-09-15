# Packages
# A package is a way of organizing related modules into a directory.

# For example:

# project/
# │
# ├── main.py
# │
# └── utilities/
#     ├── __init__.py
#     ├── calculator.py
#     └── converter.py

# Here:

# utilities → package
# calculator.py → module
# converter.py → module

# You can import:

# from utilities.calculator import add


# __init__.py ⭐⭐

# You will often see:

# utilities/
# ├── __init__.py
# ├── calculator.py
# └── converter.py

# __init__.py can contain package initialization code and can also be used to control what the package exposes.

# For modern Python, a directory can also function as a namespace package without __init__.py, but for your current learning level, understand the conventional structure:

# package/
# └── __init__.py



# __name__ ⭐⭐⭐

# Every Python module has a special variable:

# __name__

# Its value depends on how the file is being used.

# If you run a file directly:

# python main.py

# then inside main.py:

print(__name__)




# __main__ ⭐⭐⭐

# This is commonly used with:
# if __name__ == "__main__":

# Example:

# calculator.py
# def add(a, b):
#     return a + b


# if __name__ == "__main__":
#     print(add(10, 20))

# If you run:
# python calculator.py

# Output:
# 30

# because:
# __name__ == "__main__"
# is True.




# pip ⭐⭐⭐

# pip is Python's package installer.

# It allows you to install third-party Python packages.

# For example:

# pip install requests

# Then:

# import requests

# You can check pip:

# pip --version

# Depending on your environment, you may also use:

# python -m pip install requests

# The latter is often useful because it makes it clearer which Python installation's pip you're using.


# Python Packages ⭐⭐⭐

# Don't confuse these two meanings:

# Package as a Python concept

# A directory that organizes Python modules.

# myproject/
# └── utilities/
#     ├── __init__.py
#     └── calculator.py
# Package from PyPI

# A distributable third-party library that you can install with pip.

# For example:

# pip install requests

# Packages such as:

# NumPy
# Pandas
# Matplotlib
# Requests
# scikit-learn

# are commonly installed this way.

# For your AI/ML journey, you'll eventually use:

# pip install numpy pandas matplotlib scikit-learn


# requirements.txt ⭐⭐⭐

# requirements.txt contains the Python packages required by a project.

# Example:

# numpy
# pandas
# matplotlib
# requests

# Someone can install all of them with:

# pip install -r requirements.txt

