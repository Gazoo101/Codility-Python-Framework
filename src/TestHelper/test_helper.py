# Enables print() to be used in a lambda function
from __future__ import print_function

class TestHelper:
    """C0d1l1ty Test Framework"""
    def __init__(self):
        self.mPrintFunc = lambda text: print(text)
        pass

    def argsToString(self, *args):
        argStringList = []

        for count, thing in enumerate(args):
            argStringList.append(str(thing))

        return ", ".join(argStringList)

    def execute(self, taskFunc, *args):

        inputStr = self.argsToString(*args)
        outputStr = str(taskFunc(*args))

        self.mPrintFunc(taskFunc.__name__ + " | Input: " + inputStr + " | Output: " + outputStr)
