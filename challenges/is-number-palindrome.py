"""
#202
Palantir

Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. 
Do not convert the integer into a string.
"""

class Dequeue:
    def __init__(self, arr=None):
        self.arr = arr or []
    
    def enqueue(self, val=None):
        self.arr.append(val)
    
    def dequeueFront(self):
        if not self.isEmpty():
            return self.arr.pop(0)
        else:
            return None
    
    def dequeueBack(self):
        if not self.isEmpty():
            return self.arr.pop()
        else:
            return None
    
    def isEmpty(self):
        return len(self.arr) == 0
    
    def __str__(self):
        return repr(self.arr)

def isPalindrome(num):
    dequeue = Dequeue()
    digitCount = 0

    while num > 0:
        digit = num % 10
        num //= 10
        dequeue.enqueue(digit)
        digitCount += 1
    
    # print(dequeue)
    
    for _ in range(digitCount//2):

        if dequeue.dequeueFront() != dequeue.dequeueBack():
            return False
    
    return True


def main():
    print(isPalindrome(121))
    print(isPalindrome(888))
    print(isPalindrome(678))
    
if __name__ == "__main__":
    main()