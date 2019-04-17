"""
#273
Apple

A fixed point in an array is an element whose value is equal to its index.

Given a sorted array of distinct elements, return a fixed point, if one exists.
Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.

"""


def find_fixed_point_linear_search(arr):
    for ind in range(len(arr)):
        if arr[ind] == ind:
            return ind
        elif arr[ind] > ind:
            return False
    
    return False


def find_fixed_point_binary_search(arr):
    left = 0
    right = len(arr)
    mid = right // 2

    while True:
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            return False
    
    return False


def main():
    print(find_fixed_point_linear_search([-6, 0, 2, 40]))      # 2
    print(find_fixed_point_linear_search([1, 5, 7, 8]))        # False
    print()
    print(find_fixed_point_binary_search([-6, 0, 2, 40]))      # 2
    print(find_fixed_point_binary_search([1, 5, 7, 8]))        # False


if __name__ == "__main__":
    main()