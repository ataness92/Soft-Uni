rows, columns = [int(x) for x in input().split()]
matrix = []
direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
starting_boy_position = []
current_boy_position = []
for row in range(rows):
    matrix.append([x for x in input()])
    if 'B' in matrix[row]:
        current_boy_position = [row, matrix[row].index('B')]
starting_boy_position = current_boy_position
while True:
    command = input()

    row, col = current_boy_position[0] + direction[command][0], current_boy_position[1] + direction[command][1]

    if not (0 <= row < rows and 0 <= col < columns):
        matrix[starting_boy_position[0]][starting_boy_position[1]] = ' '
        print("The delivery is late. Order is canceled.")
        break

    if matrix[row][col] == '*':
        continue

    current_boy_position = row, col

    if matrix[row][col] == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[row][col] = 'R'
    if matrix[row][col] == 'A':
        print("Pizza is delivered on time! Next order...")
        matrix[row][col] = 'P'
        break

    if matrix[row][col] == '-':
        matrix[row][col] = '.'

for row in range(rows):
    print(''.join(str(x) for x in matrix[row]))


