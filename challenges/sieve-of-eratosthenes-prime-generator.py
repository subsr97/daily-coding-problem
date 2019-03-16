"""
#244
Square

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N.
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two),then [6, 9, 12, ...] (multiples of three), and so on.
Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""

import math

# Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode
def sieveOfEratosthenes(n):
    # Setting all numbers.
    numberList = [True for _ in range(n+1)]

    for i in range(2, int(math.sqrt(n))+1):
        # If not already unset, i is prime.
        if numberList[i]:
            # Unsetting all multiples of i.
            for j in range(i*i, n+1, i):
                numberList[j] = False
    
    # All set numbers are prime.
    return [i for i in range(2,n+1) if numberList[i]]


# Reference: https://github.com/ActiveState/code/blob/master/recipes/Python/117119_Sieve_of_Eratosthenes/recipe-117119.py
def indefiniteSieveOfEratosthenes():
    compositeDic = dict()   # Dictionary to hold composite numbers and their witness primes.
    currentNum = 2          # Starting prime.

    while True:
        if currentNum not in compositeDic:
            yield currentNum                                    # Not in compositeDic, so currentNum is prime.
            compositeDic[currentNum*currentNum] = [currentNum]  # Adding the first multiple of currentNum and setting the witness as currentNum.
        else:
            # currentNum is composite.
            for prime in compositeDic[currentNum]:
                compositeDic.setdefault(prime+currentNum,[]).append(prime)  # Moving each witness prime to it's next multiple.
            del compositeDic[currentNum]                                    # compositeNum[currentNum] is no longer needed.
        currentNum += 1

def main():
    print(sieveOfEratosthenes(100))

    # Needs KeyboardInterrupt to stop.
    for prime in indefiniteSieveOfEratosthenes():
        print(prime, end=" ")

if __name__ == "__main__":
    main()