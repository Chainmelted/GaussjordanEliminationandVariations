gauss_jordan_matrix_input = [
        [1, -1, 0],
        [-2, 2, -1],
        [0, 1, -2]
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
def copy_matrix(M):
    new_M = []
    for row in M:
        new_row = []
        for val in row:
            new_row.append(val)
        new_M.append(new_row)
    return new_M


########################################################################################

def gauss_jordan(matrix):
    n = len(matrix)
    num_cols = len(matrix[0])

    # finding the largest magnitude in a column
    for pivot_index in range(n):
        pivot_row = pivot_index
        for candidate_row in range(pivot_index, n):
            if abs(matrix[candidate_row][pivot_index]) > abs(matrix[pivot_row][pivot_index]):
                pivot_row = candidate_row
        if pivot_row != pivot_index:
            swap_rows(matrix, pivot_index, pivot_row)

        # normalize pivot row
        pivot_value = matrix[pivot_index][pivot_index]
        for col in range(num_cols):
            matrix[pivot_index][col] = matrix[pivot_index][col] / pivot_value

        # eliminate other rows
        for other_row in range(n):
            if other_row != pivot_index:
                factor = matrix[other_row][pivot_index]
                for col in range(num_cols):
                    matrix[other_row][col] -= factor * matrix[pivot_index][col]

    return matrix

def inverse_matrix(matrix):
    n = len(matrix)

    partitioned = []
    for row_number in range(n):
        row = []
        # left side: original matrix
        for col_number in range(n):
            row.append(matrix[row_number][col_number])
        # right side: identity
        for col_number in range(n):
            if row_number == col_number:
                row.append(1.0)
            else:
                row.append(0.0)
        partitioned.append(row)

    # calling GJ elimination on the identity section
    reduced = gauss_jordan(partitioned)

    # extract right side as inverse
    inverse = []
    for row_number in range(n):
        row = []
        for col_number in range(n, 2*n):
            row.append(reduced[row_number][col_number])
        inverse.append(row)

    return inverse


##
if __name__ == "__main__":
    A_for_GJE = copy_matrix(gauss_jordan_matrix_input)
    GJE_result = gauss_jordan(A_for_GJE)

    A_for_inverse = copy_matrix(gauss_jordan_matrix_input)
    GJE_inverse_result = inverse_matrix(A_for_inverse)

    print("Matrix w/ Gauss-Jordan:")
    format_matrix(GJE_result)
    print("\nInverse matrix:")
    format_matrix(GJE_inverse_result)