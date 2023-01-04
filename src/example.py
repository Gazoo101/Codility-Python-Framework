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

def remixChars( string, list1, list2 ):

    word1list = []
    word2list = []

    for index in list1:
        word1list.append(string[index])

    for index in list2:
        word2list.append(string[index])

    word1 = ''.join(word1list)
    word2 = ''.join(word2list)

    return word1 + " " + word2

def listLength( list ):
    length = 0

    while list != None:
        length += 1
        list = list.next

    return length

def treeDepth( tree ):

    def depthHelper(treeNode, depth):
        if treeNode == None:
            return depth
        else:
            depth += 1
            return max(depthHelper(treeNode.left, depth), depthHelper(treeNode.right, depth))

    return depthHelper(tree, 0)

#######################
#   Example Objects   #
#######################
# Not unlike those used at https://leetcode.com/
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

############
#   Main   #
############
if __name__ == "__main__":
    # Execute only if run as a script
	
    helper = TestHelper()

    # Apply TestHelper to various possible use cases
    helper.execute(addIntegers, 1, 2, 3)
    helper.execute(addIntegers, 1, 10, 100)

    # Array's work fine, but...
    helper.execute(addListOrArray, array('i', [0, 1, 2, 3, 4]))
    # you'll probably want to stick with lists
    helper.execute(addListOrArray, [0, 1, 2, 3, 4])
    helper.execute(remixChars, "Hello World", [9,7,8,10], [0,4,6,1,2,3])

    # A List example could also be of some use
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)

    helper.execute(listLength, list)

    # A Tree example might also be useful
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.right.right = TreeNode(4)

    helper.execute(treeDepth, tree)
