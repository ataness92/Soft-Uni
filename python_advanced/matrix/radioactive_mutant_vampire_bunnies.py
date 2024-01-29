from collections import deque

rows, cols = [int(x) for x in input().split()]

lair = [[x for x in input()] for _ in range(rows)]

player_pos = deque([row, col] for row in range(rows) for col in range(cols) if lair[row][col] == 'P')
bunny_pos = [[row, col] for row in range(rows) for col in range(cols) if lair[row][col] == 'B']
move = {
    "L" : [0,-1],
    "R" : [0, 1],
    "U" : [-1, 0],
    "D" : [1, 0],
}

command = [x for x in input()]

def spread_rabbit():
    for position in bunny_pos:

        if(position[1] < cols-1):
            lair[position[0]][position[1] + 1] = 'B'  # right
        if(position[0]>0):
            lair[position[0]-1][position[1]] = 'B' # up
        if(position[0]< rows-1):
            lair[position[0]+1][position[1]] = 'B' # down
        if(position[1] > 0):
            lair[position[0]][position[1]-1] = 'B' # left

won = 0
for c in command:
    player_pos.append([player_pos[0][0] + move[c][0], player_pos[0][1] + move[c][1]])
    if player_pos[-1][0] < 0 or player_pos[-1][1] < 0 or player_pos[-1][0] >= rows or player_pos[-1][1] >= cols:
        won = 1
        lair[player_pos[0][0]][player_pos[0][1]] = '.'
        spread_rabbit()
        break
    else:
        lair[player_pos[0][0]][player_pos[0][1]] = '.'
        player_pos.popleft()
        if lair[player_pos[0][0]][player_pos[0][1]] == 'B':
            won = 0
            spread_rabbit()
            break
        else:
            lair[player_pos[0][0]][player_pos[0][1]] = 'P'
        spread_rabbit()

    bunny_pos = [[row, col] for row in range(rows) for col in range(cols) if lair[row][col] == 'B']

print(*[''.join(x) for x in lair], sep='\n')
if won:
    print("won:", *player_pos[0])
else:
    print("dead:", *player_pos[0])
