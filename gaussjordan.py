gauss_jordan_matrix_input = [
        [1, -1, 0, 2],
        [-2, 2, -1, -1],
        [0, 1, -2, 6]
    ]
## Matrix Operations
def row_multiplication(row,multiplier):
    builtRow = []
    for element in row:
        builtRow.append(element*multiplier)
    return builtRow

def row_division(row,divider):
    builtRow = []
    for element in row:
        builtRow.append(element / divider)
    return builtRow

def row_addition(row1, row2):
    builtRow = []
    for i in range(len(row1)):
        builtRow.append(row1[i] + row2[i])
    return builtRow

def create_column(matrix, column_number):
    column = []
    for rows in matrix:
        column.append(rows[column_number-1])
    return column

def swap_rows(matrix, i, j):
    temp = matrix[i]
    matrix[i] = matrix[j]
    matrix[j] = temp

def format_matrix(matrix):
    for row in matrix:
        print(row)

########################################################################################

def gauss_jordan(matrix):
    n = len(matrix)

    # finding the largest magnitude in a column
    for pivot_index in range(n):
        pivot_row = pivot_index
        for candidate_row in range(pivot_index, n):
            if abs(matrix[candidate_row][pivot_index]) > abs(matrix[pivot_row][pivot_index]):
                pivot_row = candidate_row
        if pivot_row != pivot_index:
            swap_rows(matrix, pivot_index, pivot_row)

        pivot_value = matrix[pivot_index][pivot_index]
        matrix[pivot_index] = row_division(matrix[pivot_index], pivot_value)

        for other_row in range(n):
            if other_row != pivot_index:
                factor = -matrix[other_row][pivot_index]
                scaled_pivot = row_multiplication(matrix[pivot_index], factor)
                matrix[other_row] = row_addition(matrix[other_row], scaled_pivot)

    return matrix


##
if __name__ == "__main__":

    result = gauss_jordan(gauss_jordan_matrix_input)

    print("Matrix w/ Gauss-Jordan:")
    format_matrix(result)

    solution = []
    for row in result:
        solution.append(row[-1])
    print("Solution:", solution)