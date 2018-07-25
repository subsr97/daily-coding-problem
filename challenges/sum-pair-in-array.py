"""
#1
Google

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""

def bruteforce(numbers, neededSum):
    l = len(numbers)
    for i in range(l-1):
        for j in range(i+1,l):
            if numbers[i]+numbers[j] == neededSum:
                return True
    return False

def checkSumPair(numbers, neededSum):
    knownNumbers = set()
    for number in numbers:
        if (neededSum-number) in knownNumbers:
            return True
        else:
            knownNumbers.add(number)
    return False

if __name__ == "__main__":
    numbers = [int(x) for x in input().strip().split()]
    neededSum = int(input().strip())
    print(bruteforce(numbers, neededSum))
    print(checkSumPair(numbers, neededSum))
