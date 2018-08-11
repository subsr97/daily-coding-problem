"""
#26
Google

Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return "<" + str(self.val) + ">"

# Uses k+1 space for nodeQueue and 1 for currentNode   
def findKthLastElement(linkedList, k):
    nodeQueue = []
    currentNode = linkedList
    
    while currentNode:
        if len(nodeQueue) == k+1:
            nodeQueue.pop(0)
        nodeQueue.append(currentNode)
        currentNode = currentNode.next
    
    if k == 1:
        # Deleting last node
        # nodeQueue has 2 elements. Deleting nodeQueue[1]
        nodeQueue[0].next = None
        return linkedList
    elif len(nodeQueue) == k:
        # Deleting first node
        # nodeQueue has as many elements as the linked list. Dropping nodeQueue[0]
        return nodeQueue[1]
    else:
        # Deleting node in the middle
        # Deleting nodeQueue[1]
        nodeQueue[0].next = nodeQueue[2]
        return linkedList

def printLinkedList(linkedList):
    print("[ ", end="")

    currentNode = linkedList
    while currentNode:
        print(currentNode, end=" ")
        currentNode = currentNode.next
    
    print("]")

def main():
    linkedList = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    printLinkedList(linkedList)
    printLinkedList( findKthLastElement(linkedList, 5) )

if __name__ == "__main__":
    main()