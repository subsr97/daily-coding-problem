class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return "<" + str(self.val) + ">"
    
def findKthLastElementUsing1Space(linkedList, k):
    kthLastNode = linkedList

    currNode = linkedList

    for i in range(k):
        currNode = currNode.next

    while currNode:
        currNode = currNode.next
        kthLastNode = kthLastNode.next
    
    return kthLastNode

def main():
    linkedList = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print( findKthLastElementUsingKPlus1Space(linkedList, 3))
    print( findKthLastElementUsing1Space(linkedList, 3) )



if __name__ == "__main__":
    main()