array_int = [int(x) for x in input().split()]

command = input().split()

while command[0] != 'end':
    if command[0] == 'swap':
        array_int[int(command[1])], array_int[int(command[2])] = array_int[int(command[2])], array_int[int(command[1])]
    elif command[0] == 'multiply':
        array_int[int(command[1])] = array_int[int(command[1])]*array_int[int(command[2])]
    elif command[0] == 'decrease':
        array_int = [x-1 for x in array_int]
    command = input().split()
print(f"{', '.join([str(x) for x in array_int])}")
