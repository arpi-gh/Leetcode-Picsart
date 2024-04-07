def setZeroes(matrix: list[list[int]]) -> None:
    row_zero = False
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                if i > 0:
                    matrix[i][0] = 0  # Marking the rows
                else:
                    row_zero = True
                matrix[0][j] = 0  # Marking the columns

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][0] == 0 or matrix[0][j] == 0:  # either the row or the column is zeroed out
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for i in range(rows):
            matrix[i][0] = 0  # set the first column to zero if it's flagged as zero

    if row_zero:
        for j in range(columns):
            matrix[0][j] = 0  # set the first row to zero if it's flagged as zero

