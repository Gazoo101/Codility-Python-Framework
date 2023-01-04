""" Beginner template ready to copy and use. """

from TestHelper import TestHelper

def solution(A):
    return A

if __name__ == "__main__":
    helper = TestHelper()

    helper.execute(solution, [1, 3, 6, 4, 1, 2])
    helper.execute(solution, [-2, 9, 4, 3, 5, 100])
    helper.execute(solution, [1,2,3])
    helper.execute(solution, [-1,-3])