size = int(input())

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
start_position = []
matrix = []
armor_left = 300
enemy = 4
for row in range(size):
    matrix.append([x for x in input()])
    if 'J' in matrix[row]:
        start_position = [row, matrix[row].index('J')]

while True:
    command = input()

    row, col = start_position[0] + direction[command][0], start_position[1] + direction[command][1]

    if matrix[row][col] == '-':
        matrix[start_position[0]][start_position[1]] = '-'
        matrix[row][col] = 'J'
        start_position = [row, col]
    elif matrix[row][col] == 'E':
        matrix[start_position[0]][start_position[1]] = '-'
        matrix[row][col] = 'J'
        start_position = [row, col]
        enemy-=1
        if enemy == 0:
            print(f"Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor_left -= 100
    elif matrix[row][col] == "R":
        matrix[start_position[0]][start_position[1]] = '-'
        matrix[row][col] = 'J'
        start_position = [row, col]
        armor_left = 300


    if armor_left == 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
        break


[print(''.join(x)) for x in matrix]
