"""
#150
LinkedIn

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.
For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""

from heapq import heappush, heappop

def distanceSquare(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def kNearestPointsUsingHeap(points, centralPoint, k):
    h = []

    for point in points:
        heappush(h,(distanceSquare(point,centralPoint),point))
    
    return [heappop(h)[1] for _ in range(k)]


def main():
    points = [(0,0), (5,4), (3,1)]
    centralPoint = (1,2)
    k = 2

    print(kNearestPointsUsingHeap(points, centralPoint, k))


if __name__ == "__main__":
    main()