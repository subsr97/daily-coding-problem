"""
#36
Dropbox

This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return "< " + str(self.val) + " >"

def findSecondMax(root):
    if root.right:
        # Finding the second max using max
        maxNode = root
        secondMaxNode = None

        while maxNode.right:
            secondMaxNode = maxNode
            maxNode = maxNode.right

        if maxNode.left:
            secondMaxNode = maxNode.left
            
            while secondMaxNode.right:
                secondMaxNode = secondMaxNode.right

        return secondMaxNode
    elif root.left:
        # Finding the right most node in the left subtree
        secondMaxNode = root.left
        while secondMaxNode.right:
            secondMaxNode = secondMaxNode.right
        return secondMaxNode
    else:
        # No second maximum node
        return None
            

def main():
    """
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
    """
    BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
    print(findSecondMax(BST))
    
    
    """
        8
       / \
      3   10
     / \    \
    1   6    14
       / \
      4   7
    """
    BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14)))
    print(findSecondMax(BST))

    """
        8
       /
      3
     / \
    1   6
       / \
      4   7
    """
    BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))))
    print(findSecondMax(BST))

if __name__ == "__main__":
    main()
