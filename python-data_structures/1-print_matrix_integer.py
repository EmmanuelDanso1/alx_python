#!/usr/bin/python3
#printing matrix cols and rows 
def print_matrix_integer(matrix=[[]]):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0]) if number_of_rows > 0 else 0

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            print("{:d}".format(matrix[i][j]), end="")
            if j < number_of_columns - 1:
                print(" ", end="")
        print()



