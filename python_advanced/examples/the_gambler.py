size = int(input())
board = []
position = []

money = 100
jackpot = False
direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for row in range(size):
    board.append([x for x in input()])
    if 'G' in board[row]:
        position = [row, board[row].index('G')]

command = input()

while command != 'end':

    row = position[0] + direction[command][0]
    col = position[1] + direction[command][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    if board[row][col] == '-':
        board[row][col] = 'G'
        board[position[0]][position[1]] = '-'
        position = [row, col]
    elif board[row][col] == 'W':
        money += 100
        board[row][col] = 'G'
        board[position[0]][position[1]] = '-'
        position = [row, col]
    elif board[row][col] == 'P':
        board[row][col] = 'G'
        board[position[0]][position[1]] = '-'
        position = [row, col]
        money -= 200
        if money <= 0:
            break
    elif board[row][col] == 'J':
        board[row][col] = 'G'
        board[position[0]][position[1]] = '-'
        position = [row, col]
        jackpot = True
        break

    command = input()

if jackpot:
    print(f"You win the Jackpot! End of game. Total amount {money+100000}$")
elif money > 0:
    print(f"End of the game. Total amount: {money}$")
    [print(''.join(row)) for row in board]
else:
    print("Game over! You lost everything!")

