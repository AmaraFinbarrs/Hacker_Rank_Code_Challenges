# Write a program that takes a 2n x 2n matrix and reverses the rows and columns in the best possible way so that the sum of the elements in the matrix's upper left quadrant is maximal.

def flipping_matrix(matrix):
    # to flip the matrix vertically, y-axis of the matrix
    n_value = len(matrix[0]) // 2
    # print('n_value:', n_value)
    for count in range(n_value):
        y = []
        i = 0
        while i < 2 * n_value:
            y.append(matrix[i][n_value + count])
            i += 1
        max_y = max(y)
        # print('index:', y.index(max_y))
        if y.index(max_y) > n_value - 1:
            y = y[::-1]
            # print(y)
            for nos in range(2 * n_value):
                matrix[nos][n_value + count] = y[nos]
    # print(matrix)

    # to flip the matrix horizontally
    for count in range(n_value):
        x = []
        j = 0
        while j < 2 * n_value:
            x.append(matrix[count][j])
            # print(x)
            j += 1
        max_x = max(x)
        # print(max_y)
        # print('index:', x.index(max_x))
        if x.index(max_x) > n_value - 1:
            x = x[::-1]
            # print(x)
            for nos in range(2 * n_value):
                matrix[count][nos] = x[nos]
    # print(matrix)

    return sum_upper_left(matrix)


def sum_upper_left(matrix):
    n_value = len(matrix[0]) // 2  # print('n_value:', n_value)

    # create empty integers to store values
    result = 0  # to store the sum for the final result
    matrix_size = 2 * n_value  # size of one side of square matrix
    #  print('matrix_size:', matrix_size)

    for i in range(0, matrix_size // 2):
        j = 0  # counter for the vertical axis of the matrix.
        # print('i:', i, 'j:', j)
        while j < n_value:
            result += matrix[i][j]
            # print('result:', result)
            j += 1  # increment the counter
            # print('j:', j)

    return print(result)


matrix2_n1 = [[1, 2], [3, 4]]
matrix2_n2 = [[119, 114, 42, 112], [56, 125, 101, 49], [15, 78, 56, 43], [62, 98, 83, 108]]
matrix2_n3 = [
    [1, 2, 3, 4, 5, 6], [6, 6, 7, 8, 9, 10], [9, 10, 11, 12, 13, 14], [1, 2, 3, 4, 5, 6], [7, 8, 9, 1, 2, 3],
    [4, 5, 6, 7, 8, 9]]
# print(matrix2_n1)
# print(matrix2_n2)
#print(matrix2_n3)

# sum_upper_left(matrix2_n3)
flipping_matrix(matrix2_n2)
