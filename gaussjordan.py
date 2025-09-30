rowExample = [1,2,3]
def row_multiplication(row,multiplier):
    builtRow = []
    for element in row:
        builtRow.append(element*multiplier)
    return builtRow

print(row_multiplication(rowExample,2))
