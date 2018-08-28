"""
#42
Google

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

"""

ansSubArr = None

def findSubArrRecursively(arr, subArr, targetSum, index):
    global ansSubArr

    # Set answer and return
    if sum(subArr) == targetSum:
        ansSubArr = subArr
        return
    
    # Return if answer has been found or if sum has exceeded the target sum.
    if ansSubArr or sum(subArr)>targetSum:
        return
    
    # If there are any more elements left, make two recursive calls. 
    #   -> One call including the next element
    #   -> Once call without the next element
    if index < len(arr):
        findSubArrRecursively(arr, subArr+[arr[index]], targetSum, index+1)
        findSubArrRecursively(arr, subArr, targetSum, index+1)
    

def findSubArrWithSum(arr, targetSum):
    findSubArrRecursively(arr, [], targetSum, 0)
    return ansSubArr

def main():
    arr = [12, 1, 61, 5, 9, 2]
    targetSum = 24
    print(findSubArrWithSum(arr,targetSum))

if __name__ == "__main__":
    main()
