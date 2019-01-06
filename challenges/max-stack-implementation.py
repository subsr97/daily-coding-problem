"""
#43
Amazon

Implement a stack that has the following methods:
    ->  push(val), which pushes an element onto the stack
    
    ->  pop(), which pops off and returns the topmost element of the stack. 
        If there are no elements in the stack, then it should throw an error or return null.
    
    ->  max(), which returns the maximum value in the stack currently. 
        If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""

# Node represents a single stack element
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
    
    def __str__(self):
        return "<" + str(self.val)  + ">"

# Ordinary stack implementation with linked-list
class Stack:
    def __init__(self):
        self.top = Node(None)
    
    def __str__(self):
        stringRepresentation = "< "
        currentNode = self.top
        while currentNode.val != None:
            stringRepresentation += str(currentNode)
            currentNode = currentNode.prev
        stringRepresentation += " >"
        return stringRepresentation
    
    def push(self, val):
        newNode = Node(val)
        newNode.prev = self.top
        self.top = newNode
    
    def pop(self):
        temp = self.top
        if temp.val != None:
            self.top = self.top.prev
        return temp
    
    def peek(self):
        return self.top.val

# Special Stack inherits Stack and has additional features like max()
class SpecialStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.maxStack = Stack() # maxStack is an ordinary stack that is used to hold the max values.
    
    """
    push(x)
        1) Push x into Special Stack
        2) Compare x with the maxStack's top (y)
            ->  If x > y, push x onto maxStack
            ->  If y > x, push y onto maxStack
    """
    def push(self, val):
        Stack.push(self,val)
        maxTop = self.getMaxTop()
        if maxTop == None or maxTop <= val:
            self.maxStack.push(val)
        else:
            self.maxStack.push(maxTop)
    
    """
    pop()
        1) Pop an element from maxStack
        2) Pop and return an element from Special Stack
    """
    def pop(self):
        self.maxStack.pop()
        return Stack.pop(self)

    def getMaxTop(self):
        return self.maxStack.peek()

    def max(self):
        return self.getMaxTop()


def main():
    s = SpecialStack()
    
    s.push(18)
    print(s, s.maxStack, s.max())
    s.push(19)
    print(s, s.maxStack, s.max())
    s.push(29)
    print(s, s.maxStack, s.max())
    s.push(15)
    print(s, s.maxStack, s.max())
    s.push(16)
    print(s, s.maxStack, s.max())

    s.pop()
    print(s, s.maxStack, s.max())
    s.pop()
    print(s, s.maxStack, s.max())
    s.pop()
    print(s, s.maxStack, s.max())
    s.pop()
    print(s, s.maxStack, s.max())
    s.pop()
    print(s, s.maxStack, s.max())

if __name__ == "__main__":
    main()