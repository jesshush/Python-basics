#otaining an element from matrix
matrix = [ [1,2,3,],
          [4,5,6],
          [7,8,9]]
print(matrix[2][1])


#transpose
transpose_matrix = [[matrix[j][i]
    for j in range(len(matrix))]
for i in range(len(matrix))]
print(transpose_matrix)


#append new row
new_row = [3,3,4]
matrix.append(new_row)
print(matrix)