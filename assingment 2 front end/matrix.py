# define the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
columns = len(matrix[0])

# visiting primary diagonal
for i in range(rows):
    print(matrix[i][i], end=" ")
print()

# visiting secondary diagonal
for i in range(rows):
    print(matrix[i][columns - 1 - i], end=" ")
print()

# calculate the sum of rows
for i in range(rows):
    total = 0
    for j in range(columns):
        total = total + matrix[i][j]
    print("sum of row", i, "=", total)

# sum of diagonals
sum_primary = 0
sum_secondary = 0

for i in range(rows):
    sum_primary = sum_primary + matrix[i][i]
    sum_secondary = sum_secondary + matrix[i][columns - 1 - i]

print("sum of primary diagonal:", sum_primary)
print("sum of secondary diagonal:", sum_secondary)
