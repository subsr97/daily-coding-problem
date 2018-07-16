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
