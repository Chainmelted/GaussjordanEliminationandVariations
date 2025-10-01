gauss_jordan_matrix_input = [
        [1, -1, 0],
        [-2, 2, -1],
        [0, 1, -2]
    ]
## test algorithm 3
system = [
    [1, 0, 2, 1],
    [2, -1, 3, -1],
    [4, 1, 8, 2]
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

def row_subtraction(row1, row2):
    builtRow = []
    for i in range(len(row1)):
        builtRow.append(row1[i] - row2[i])
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

def gaussian_elimination(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for pivot_row_index in range(num_rows):
        # Step 1: partial pivoting
        max_row_index = pivot_row_index
        for candidate_row_index in range(pivot_row_index, num_rows):
            if abs(matrix[candidate_row_index][pivot_row_index]) > abs(matrix[max_row_index][pivot_row_index]):
                max_row_index = candidate_row_index
        if max_row_index != pivot_row_index:
            swap_rows(matrix, pivot_row_index, max_row_index)

        # Step 2: divide through pivot row
        pivot_value = matrix[pivot_row_index][pivot_row_index]
        matrix[pivot_row_index] = row_division(matrix[pivot_row_index], pivot_value)

        # Step 3: eliminate rows below pivot
        for lower_row_index in range(pivot_row_index+1, num_rows):
            factor = matrix[lower_row_index][pivot_row_index]
            scaled_pivot_row = row_multiplication(matrix[pivot_row_index], factor)
            matrix[lower_row_index] = row_subtraction(matrix[lower_row_index], scaled_pivot_row)

    #substitution
    solution = []
    for variable_index in range(num_rows):
        solution.append(0)

    for row_index in range(num_rows-1, -1, -1):
        right_partition = matrix[row_index][num_cols-1]
        for col_index in range(row_index+1, num_rows):
            right_partition -= matrix[row_index][col_index] * solution[col_index]
        solution[row_index] = right_partition / matrix[row_index][row_index]

    return solution

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
        # eliminate other rows (in gauss_jordan)
        for other_row in range(n):
            if other_row != pivot_index:
                factor = matrix[other_row][pivot_index]
                scaled_pivot = row_multiplication(matrix[pivot_index], factor)
                matrix[other_row] = row_subtraction(matrix[other_row], scaled_pivot)

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
    gaussian_result = gaussian_elimination(copy_matrix(system))

    A_for_inverse = copy_matrix(gauss_jordan_matrix_input)
    GJE_inverse_result = inverse_matrix(A_for_inverse)

    print("Matrix w/ Gauss-Jordan:")
    format_matrix(GJE_result)
    print("\nInverse matrix:")
    format_matrix(GJE_inverse_result)
    print("\nGaussian Elimination solution:")
    print("x =", gaussian_result[0])
    print("y =", gaussian_result[1])
    print("z =", gaussian_result[2])