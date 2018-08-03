"""
#20
Google

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

def findIntersection(A, B):
    visitedIDs = set()

    currentNode = A
    while currentNode != None:
        visitedIDs.add(id(currentNode))
        currentNode = currentNode.next
    
    print(visitedIDs)

    currentNode = B
    while currentNode != None:
        currentID = id(currentNode)
        if currentID in visitedIDs:
            return currentNode
        visitedIDs.add(currentID)
        currentNode = currentNode.next
    
    return None
    
if __name__ == "__main__":

    A = Node(3, Node(7, Node(8, Node(10))))
    B = Node(99, Node(1, A.next.next))

    intersectingNode = findIntersection(A, B)

    print(intersectingNode)