# Codility-Python-Framework

Given the prevalence of automated logic puzzle driven evaluation systems, I put together a simple Python framework designed to run and test small functions. It's so simple, it really mostly exists as a counter-point to the [the C++ version](https://github.com/Gazoo101/Codility-Cpp11-Framework), except (obviously) using Python.

Unless your test *must* be conducted in C++ (or some non-python language) I strongly recommend using this framework as opposed to [the C++ version](https://github.com/Gazoo101/Codility-Cpp11-Framework). Assuming (at least) basic proficiency in both languages, you will utilize the testing time far more efficiently with Python.

The framework should work equally well for both Python 2.7 and 3+.

## How To Use

The included [main.py](src/main.py) file demonstrates basic usage. By default, the framework will print the output directly to the Python console. You can provide your own print function if you so desire. Here's an excerpt from the [main.py](src/main.py) file, showing basic usage. Please refer to actual [main.py](src/main.py) file for further examples.

```python
from TestHelper import TestHelper
from array import array

#####################
#   Example Tasks   #
#####################
def addIntegers(A, B, C):
	return A + B + C

def addListOrArray( listOrArray ):
	returnValue = 0
	for elem in listOrArray :
		returnValue += elem

	return returnValue


############
#   Main   #
############
if __name__ == "__main__":
	# Execute only if run as a script
	
	# Create TestHelper
	helper = TestHelper()

	# Apply TestHelper to various possible use cases
	helper.execute(addIntegers, 1, 2, 3)
	helper.execute(addIntegers, 1, 10, 100)

	# Array's work fine, but...
	helper.execute(addListOrArray, array('i', [0, 1, 2, 3, 4]))
	# you'll probably want to stick with lists
	helper.execute(addListOrArray, [0, 1, 2, 3, 4])
	helper.execute(remixChars, "Hello World", [9,7,8,10], [0,4,6,1,2,3])
```
This will result in the following output:

	addIntegers | Input: 1, 2, 3 | Output: 6
	addIntegers | Input: 1, 10, 100 | Output: 111
	addListOrArray | Input: array('i', [0, 1, 2, 3, 4]) | Output: 10
	addListOrArray | Input: [0, 1, 2, 3, 4] | Output: 10

## Version History

### 0.2

* Tweaked code and files to more closely match PEP standards.

### 0.1

* Everything
