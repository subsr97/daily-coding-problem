"""
#215
Yelp

The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

The horizontal distance of the root is 0.
The horizontal distance of a left child is hd(parent) - 1.
The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
The bottom view of a tree, then, consists of the lowest node at each horizontal distance. If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findBottomView(node, breadth, bottomView):
    bottomView[breadth] = node.val
    
    if node.left:
        findBottomView(node.left, breadth-1, bottomView)

    if node.right:
        findBottomView(node.right, breadth+1, bottomView)
    
    return bottomView

def findBottomViewWrapper(node):
    bottomView = findBottomView(node, 0, dict())
    return [bottomView[breadth] for breadth in range(min(bottomView.keys()), max(bottomView.keys())+1)]


def main():
    tree = Node(5, Node(3, Node(1, Node(0)), Node(4)), Node(7, Node(6), Node(9, Node(8))))
    print(findBottomViewWrapper(tree))

if __name__ == "__main__":
    main()