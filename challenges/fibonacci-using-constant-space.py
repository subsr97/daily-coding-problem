"""
#233
Apple

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.

"""

def findNthFibonacci(n):
    a = -1
    b = 1
    c = None

    for _ in range(n):
        c = a + b
        a = b
        b = c
    
    return c


def main():
    print(findNthFibonacci(5))

if __name__ == "__main__":
    main()