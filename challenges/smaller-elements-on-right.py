"""
#165
Google

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1 

"""
import heapq

def smallerElementsOnRight(l):
    h = []
    resultList = []

    while len(l):
        currentElement = l.pop()
        heapq.heappush(h, currentElement)
        resultList = [h.index(currentElement)] + resultList
    
    return resultList

def main():
    print(smallerElementsOnRight([3, 4, 9, 6, 1]))

if __name__ == "__main__":
    main()