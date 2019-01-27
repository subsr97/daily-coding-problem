"""
#195
Google

Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]

And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.

"""

# Uncomment all print statements to see the valid upper and lower bound elements and their respective count
def countElements(matrix, upperBound, lowerBound):
    N = len(matrix)
    M = len(matrix[0])

    upperBoundCount = 0
    lowerBoundCount = 0

    # print("Upper bound elements: ", end = " ")
    for i in range(N):
        if matrix[i][0] >= upperBound:
            break
        else:
            # print(matrix[i][0], end = " ")
            upperBoundCount += 1
        
        for j in range(1, M):
            if matrix[i][j] >= upperBound:
                break
            # print(matrix[i][j], end = " ")
            upperBoundCount += 1

    # print("\nLower Bound Elements: ", end = " ")
    for i in range(N-1, -1, -1):
        if matrix[i][M-1] <= lowerBound:
            break
        else:
            # print(matrix[i][M-1], end = " ")
            lowerBoundCount += 1
        
        for j in range(M-2, -1, -1):
            if matrix[i][j] <= lowerBound:
                break
            # print(matrix[i][j], end = " ")
            lowerBoundCount += 1

    # print("\nUpper Bound Count:", upperBoundCount, "\nLower Bound Count:", lowerBoundCount)
    return upperBoundCount + lowerBoundCount
        

def main():
    matrix = [
        [1, 3, 7, 10, 15, 20],
        [2, 6, 9, 14, 22, 25],
        [3, 8, 10, 15, 25, 30],
        [10, 11, 12, 23, 30, 35],
        [20, 25, 30, 35, 40, 45]
    ]

    i1 = 1
    j1 = 1

    i2 = 3
    j2 = 3

    upperBound = matrix[i1][j1]
    lowerBound = matrix[i2][j2]

    print(countElements(matrix, upperBound, lowerBound))

if __name__ == "__main__":
    main()
