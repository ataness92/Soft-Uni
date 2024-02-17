rows, columns = [int(x) for x in input().split()]

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
matrix = []
my_position = []
for row in range(rows):
    matrix.append([x for x in input().split(' ')])
    if "B" in matrix[row]:
        my_position = row, matrix[row].index('B')

command = input()
touched_people = 0
moves = 0
while command != "Finish":
    row, col = my_position[0] + direction[command][0], my_position[1] + direction[command][1]

    if not (0 <= row < rows and 0<=col<columns):
        command = input()
        continue
    if matrix[row][col] == 'O':
        command = input()
        continue
    matrix[my_position[0]][my_position[1]] = '-'
    my_position = [row, col]

    if matrix[row][col] == 'P':
        touched_people+=1
        moves+=1
        matrix[row][col] = 'B'
    elif matrix[row][col] == '-':
        moves+=1

    if touched_people == 3:
        break

    command = input()

print("Game over!")
print(f"Touched opponents: {touched_people} Moves made: {moves}")