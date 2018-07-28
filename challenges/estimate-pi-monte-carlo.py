"""
#14
Google

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

"""

import random, math

def isInsideCircle(x, y):
    return x*x + y*y <= 0.5*0.5

if __name__ == "__main__":
    NO_OF_POINTS = 10000000

    insideTheCircleCount = 0

    for _ in range(NO_OF_POINTS):
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        if isInsideCircle(x,y):
            insideTheCircleCount += 1
        

    pi = 4 * insideTheCircleCount/ NO_OF_POINTS
    print("%.3f" %pi)