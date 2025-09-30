exampleMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

## Matrix Operations
def row_multiplication(row,multiplier):
    builtRow = []
    for element in row:
        builtRow.append(element*multiplier)
    return builtRow
def create_column(matrix, column_number):
    for rows in matrix:
        column = []
        column.append(rows[column_number-1])
        print(column)




print(create_column(exampleMatrix, 3))
