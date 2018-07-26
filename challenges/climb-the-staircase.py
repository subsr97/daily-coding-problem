"""
#12
Amazon

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, 
you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

"""

ways = 0

def climb(remainingSteps):
    global ways
    
    if remainingSteps == 0:
        ways += 1
        return
    
    climb(remainingSteps-1)

    if remainingSteps >= 2:
        climb(remainingSteps - 2)

def climbCustom(remainingSteps, possibleSteps):
    global ways

    if remainingSteps == 0:
        ways += 1
        return
    
    for step in possibleSteps:
        if remainingSteps >= step:
            climbCustom(remainingSteps - step, possibleSteps)


if __name__ == "__main__":
    noOfSteps = 10
    possibleSteps = [1, 3, 5]
    
    climb(noOfSteps)
    print(ways)

    ways = 0

    climbCustom(noOfSteps, possibleSteps)
    print(ways)