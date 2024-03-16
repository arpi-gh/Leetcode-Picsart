def rotate(matrix):
    n = len(matrix)
    for j in range(n):
        for i in range(j, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[j].reverse()


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(mat)
print(mat)