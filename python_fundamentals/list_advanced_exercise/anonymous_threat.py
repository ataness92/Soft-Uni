def merge(coded_string: str, my_command: str):
    start_index = int(my_command.split()[1])
    end_index = int(my_command.split()[2])
    for i in range(start_index +1, end_index):
        coded_string[start_index] += coded_string[i]
    print(coded_string)

def divide(coded_string: str):
    print(coded_string)

input_line = input().split()
all_commands = list()
while True:
    command = input()
    if command == '3:1':
        break

    all_commands.append(command)

for do in all_commands:
    if do.startswith('merge'):
        merge(input_line, do)
    elif do.startswith('divide'):
        divide(input_line)
print(all_commands)

