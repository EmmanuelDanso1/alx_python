#!/usr/bin/python3
#square matrix
def square_matrix_simple(matrix=[]):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0]) if matrix else 0
    result_matrix = [[0 for _ in range(number_of_columns)] for _ in range(number_of_rows)]

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            result_matrix[i][j] = matrix[i][j] ** 2
    return result_matrix
