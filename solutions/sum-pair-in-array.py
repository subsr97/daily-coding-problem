# Find if a pair of numbers exist in a list that add upto the required sum

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
    print(checkSumPair(numbers, neededSum))
