"""
#116
Jane Street

Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.

"""

import random

class Node:
    def __init__(self, val=1, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right
        self._isLeftEvaluated = False
        self._isRightEvaluated = False
    
    @property
    def left(self):
        if not self._isLeftEvaluated:
            if random.random() < 0.5:
                self._left = Node()
            self._isLeftEvaluated = True
        return self._left
    
    @property
    def right(self):
        if not self._isRightEvaluated:
            if random.random() < 0.5:
                self._right = Node()
            self._isRightEvaluated = True
        return self._right

def generate():
    return Node()

def traverseAndCount(node):
    if node == None:
        return 0
    return node.val + traverseAndCount(node.left) + traverseAndCount(node.right)

def main():
    largeBinaryTree = generate()
    print("Generated", traverseAndCount(largeBinaryTree), "nodes.")

if __name__ == "__main__":
    main()