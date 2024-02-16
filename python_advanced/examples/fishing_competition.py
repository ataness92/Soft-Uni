size = int(input())
area = []

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    area.append([x for x in input()])

    if "S" in area[row]:
        captain_position = [row, area[row].index('S')]

command = input()
amount = 0

while command != 'collect the nets':

    row, col = captain_position[0] + direction[command][0], captain_position[1] + direction[command][1]

    if not (0 <= row < size and 0 <= col < size):
        row, col = captain_position[0] - direction[command][0], captain_position[1] - direction[command][1]

    if area[row][col] == '-':
        area[row][col] == 'G'
        area[captain_position[0]][captain_position[1]] = '-'
        captain_position = [row, col]
    print(area[row][col])

    command = input()

print(captain_position)
print(area)