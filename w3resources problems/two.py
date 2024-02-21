# W3resources.com[problem 1-150]
# https://www.w3resource.com/python-exercises/python-basic-exercise-2.php
# 2. Write a Python program to find out what version of Python you are using.

import sys #Import the sys module to access system-specific parameters and functions
import platform
print("Python version module")
print(sys.version) # sys.version attribute to get the Python version
print("Version Info")
print(sys.version_info) # sys.version_info attribute to get detailed version information 
print(platform.python_version())