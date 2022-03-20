# An explanation of the grid challenge.
# The actual function is found below this

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

grid = [list(row) for row in grid]  # convert string in grid to list
print(grid)

r = len(grid)  # length of the row of the grid
c = len(grid[0])  # length of column of grid

for i in range(r):  # along the row, perform these operations
    grid[i].sort()  # sort the rows

# the row is completely fixed, only the column elements are changing
# fixed elements are the outer loop while the dynamic elements are in the inner loop

# we have to compare the column elements
for j in range(c):  # start with a column
    for i in range(1, r):  # for every row in that column
        if not grid[i - 1][j] <= grid[i][j]:
            print('NO')
print('YES')


# The function
def grid_challenge(grid):
    # Write your code here

    # convert string in grid to list
    grid = [list(row) for row in grid]

    r = len(grid)  # length of the row of the grid
    c = len(grid[0])  # length of column of grid

    for row in range(r):  # along the row,
        grid[row] = sorted(grid[row])  # sort the row

    # we have to compare the column elements
    for j in range(c):  # start with a column
        for i in range(1, r):  # for row 1 to the end
            if not grid[i - 1][j] <= grid[i][j]:
                return 'NO'
    return 'YES'
