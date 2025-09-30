exampleMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
exampleRow = [2,4,6]

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
