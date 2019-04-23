"""
#282
Netflix

Given an array of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.

"""

import random, math


def has_pythagorean_triplet(arr):
    arr.sort()
    squares = [num*num for num in arr]

    for ind in range(len(arr)-1, -1, -1):
        for i in range(ind):
            for j in range(i+1, ind):
                if squares[i]+squares[j] == squares[ind]:
                    print(int(math.sqrt(squares[i])), int(math.sqrt(squares[j])), int(math.sqrt(squares[ind])))
                    return True
        ind -= 1

    return False


def main():
    arr = [random.randint(1, 1000) for _ in range(1000)]
    print(has_pythagorean_triplet(arr))


if __name__ == "__main__":
    main()