"""
#89
LinkedIn

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right,
and satisfies the constraint that the key in the left child must be less than or equal to the root
and the key in the right child must be greater than or equal to the root.
"""

import math

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBSThelper(root, minVal, maxVal):
    if root.val <= maxVal and root.val >= minVal:
        if root.left != None and root.right != None:
            return isBSThelper(root.left, minVal, root.val) and isBSThelper(root.right, root.val, maxVal)
        elif root.left != None:
            return isBSThelper(root.left, minVal, root.val)
        elif root.right != None:
            return isBSThelper(root.right, root.val, maxVal)
        else:
            return True
    else:
        return False

def isBST(root):
    minVal = -1 * math.inf
    maxVal = math.inf
    return isBSThelper(root, minVal, maxVal)

def main():
    binaryTreeOne = Node(4, Node(2, Node(1), Node(3)), Node(5))
    binaryTreeTwo = Node(3, Node(2, Node(1), Node(4)), Node(5))

    print(isBST(binaryTreeOne))
    print(isBST(binaryTreeTwo)) 

if __name__ == "__main__":
    main()