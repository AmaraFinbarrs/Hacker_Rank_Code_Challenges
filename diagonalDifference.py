# Given a square matrix, calculate the absolute difference between the sums of its diagonals.


def diagonalDifference(arr):
    # create zero integers to store sum
    primary_diag = secondary_diag = 0
    
    for i in range(n):
        # store sum of primary diagonal elements
        primary_diag += arr[i][i]

        # store sum of secondary diagonal elements
        secondary_diag += arr[i][n-1-i]

    # return an absolute difference between primary and secondary diagonal
    return abs(primary_diag - secondary_diag)
