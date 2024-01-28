rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append([char for char in input()])

symbol = input()

result = next(((row, column) for row in range(rows) for column in range(rows) if matrix[row][column] == symbol), None)
if result:
    print(result)
else:
    print(f"{symbol} does not occur in the matrix")
