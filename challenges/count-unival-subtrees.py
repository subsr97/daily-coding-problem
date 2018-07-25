"""
#8
Google

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 
"""
univalSubtreeCount = 0

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isUnival(node):
    return node.left == None and node.right == None or node.left.val == node.right.val

def countUnivalSubtrees(node):
    global univalSubtreeCount
      
    if isUnival(node):
        univalSubtreeCount += 1
    if node.right != None:
        countUnivalSubtrees(node.right)
    if node.left != None:
        countUnivalSubtrees(node.left)

if __name__ == "__main__":
    tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    countUnivalSubtrees(tree)
    print(univalSubtreeCount)
