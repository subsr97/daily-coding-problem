"""
#307
Oracle

Given a binary search tree, find the floor and ceiling of a given integer. 
The floor is the highest element in the tree less than or equal to an integer, 
while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.

"""

import math

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


floor = math.inf * -1
ceil = math.inf
floorComplete = ceilComplete = False

def floorAndCeil(bst, n):
    global floor, ceil, floorComplete, ceilComplete
    floorComplete = ceilComplete = False
    floor = math.inf * -1
    ceil = math.inf 
    
    def traverse(node):
        global floor, ceil, floorComplete, ceilComplete
        val = node.val
        
        if val < n:
            # Floor
            if val > floor:
                floor = val
            else:
                floorComplete = True
        elif val > n:
            # Ceil
            if val < ceil:
                ceil = val
            else:
                ceilComplete = True
        else:
            # val = n ie n is present in BST
            floor = ceil = n
            floorComplete = ceilComplete = True

        if floorComplete and ceilComplete:
            return
        
        if node.left:
            traverse(node.left)
        
        if node.right:
            traverse(node.right)
    
    traverse(bst)

    return (floor, ceil)
           


def main():
    BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
    print(floorAndCeil(BST, 5))     # (4, 6)
    print(floorAndCeil(BST, 6))     # (6, 6)
    

if __name__ == "__main__":
    main()