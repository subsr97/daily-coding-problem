"""
#24
Google

Implement locking in a binary tree.
A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:
    > is_locked, which returns whether the node is locked
    > lock, which attempts to lock the node. If it cannot be locked, then it should return false.
      Otherwise, it should lock it and return true.
    > unlock, which unlocks the node. If it cannot be unlocked, then it should return false.
      Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like.
You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
Each method should run in O(h), where h is the height of the tree.

"""

class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.locked = False
    
    def __str__(self):
        return "<" + str(self.val) + ">"
    
    def is_locked(self):
        return self.locked
    
    def checkAncestors(self):
        if self.locked:
            return False

        if self.parent == None:
            return True

        return self.parent.checkAncestors()
    
    def checkDescendants(self):
        if self.locked:
            return False

        return (not self.left or self.left.checkDescendants()) and (not self.right or self.right.checkDescendants())

    def lock(self):
        if self.locked:
            return False
        
        if (not self.parent or self.parent.checkAncestors()) or ((not self.left or self.left.checkDescendants()) and (not self.right or self.right.checkDescendants())):
            self.locked = True
            print("Locked "+str(self))
            return True
        
        print("Cannot lock "+str(self))
        return False
    
    def unlock(self):
        if self.locked == False:
            return False
        
        if (not self.parent or self.parent.checkAncestors()) or ((not self.left or self.left.checkDescendants()) and (not self.right or self.right.checkDescendants())):
            self.locked = False
            print("Unlocked "+str(self))
            return True
        
        print("Cannot unlock "+str(self))
        return False

if __name__ == "__main__":
    
    """
           4
          / \
         2   5
        / \
       1   3
      /
     0
    """

    zero = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)

    four.left = two
    two.parent = four

    four.right = five
    five.parent = four

    two.left = one
    one.parent = two

    two.right = three
    three.parent = two

    one.left = zero
    zero.parent = one

    two.lock()
    zero.lock()
    one.lock()
    zero.unlock()
    one.lock()
    zero.lock()
    one.unlock()
    two.unlock()
    one.unlock()
    zero.unlock()