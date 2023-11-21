# A Boolean Matrix Question
# Given a boolean matrix mat[M][N] of size M X N,
# Modify it such that if a matrix cell mat[i][j] is 1 (or true) then make all the cells of ith row and jth column as 1.
import numpy as np

arr = np.array([[1, 0, 2, 1],
                [3, 1, 5, 2],
                [0, 3, 0, 5]])
rows, cols = arr.shape
# print(rows,cols)


# Approach1: Using brute force
def mask_cells(arr2d, row_idx, col_idx):
    # set entire column to -1
    for c in range(cols):
        if arr2d[row_idx][c] != 1:
            arr2d[row_idx][c] = -1
    for r in range(rows):
        if arr2d[r][col_idx] != 1:
            arr2d[r][col_idx] = -1


for row in range(rows):
    for col in range(cols):
        if arr[row][col] == 1:
            mask_cells(arr, row, col)

for row in range(rows):
    for col in range(cols):
        if arr[row][col] == -1:
            arr[row][col] = 1

print(arr)


# Another Approach:
print("Another Approach")
arr = np.array([[1, 0, 2, 1],
                [3, 4, 1, 2],
                [0, 3, 0, 5]])
arr_2d = np.zeros(arr.shape, dtype=int)

for i in range(rows):
    for j in range(cols):
        if arr[i][j] == 1:
            arr_2d[i] = 1
            arr_2d[:, j] = 1
for i in range(rows):
    for j in range(cols):
        if arr_2d[i][j] == 0:
            arr_2d[i][j] = arr[i][j]
print(arr_2d)