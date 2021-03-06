matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def rotateMatrix(matrix):
    """
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    >>> rotateMatrix(matrix)
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])//2):
            matrix[i][j], matrix[i][len(matrix[0]) - 1 - j] = \
                matrix[i][len(matrix[0]) - 1 - j], matrix[i][j]
    return matrix


[print(row) for row in rotateMatrix(matrix)]
