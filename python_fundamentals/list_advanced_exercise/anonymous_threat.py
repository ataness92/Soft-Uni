def merge(coded_string: str, my_command: str):

    if not int(my_command.split()[1]) >=len(coded_string)-1 : 
        if int(my_command.split()[1]) < 0:
            start_index = 0
        else:
            start_index = int(my_command.split()[1])
        if int(my_command.split()[2]) <= len(coded_string)-1 :
            end_index = int(my_command.split()[2])
        else :
            end_index = len(coded_string)-1
        combined_string = ''.join(map(lambda x: x, coded_string[start_index:end_index+1]))
        coded_string[start_index:end_index+1] = [combined_string]

    return coded_string

def divide(coded_string: str, my_command: str):
    index = int(my_command.split()[1])
    partitions = int(my_command.split()[2])
    element = coded_string[index]
    partition_length = len(element) // partitions
    divided_partition = []
    for current_element_index in range(partitions):
        if current_element_index != partitions -1 :
            divided_partition.append(element[current_element_index*partition_length: (current_element_index+1)*partition_length])
        else:
            divided_partition.append(element[current_element_index*partition_length:])
    coded_string[index:index+1] = divided_partition
        
    return coded_string

input_line = input().split()
all_commands = list()

while True:
    command = input()
    if command == '3:1':
        break

    all_commands.append(command)

for do in all_commands:
    if do.startswith('merge'):
        input_line = merge(input_line, do)
    elif do.startswith('divide'):
        divide(input_line, do)

print(' '.join(input_line))
