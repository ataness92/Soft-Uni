my_string = input()


def change(some_string, some_char, some_replacement):
    some_string = some_string.replace(some_char, some_replacement)
    print(some_string)
    return some_string


def includes(some_string, substring):
    if substring in some_string:
        print('True')
    else:
        print('False')
    return some_string


def end(some_string, substring):
    if some_string.endswith(substring):
        print('True')
    else:
        print('False')
    return some_string


def uppercase(some_string):
    some_string = some_string.upper()
    print(some_string)
    return some_string


def findindex(some_string, some_char):
    print(some_string.index(some_char))


def cut(some_string, some_index, count):
    print(some_string[some_index:(some_index+count)])
    return some_string


while True:
    command = input().split()
    if command[0] == 'Done':
        break

    if command[0] == 'Change':
        my_string = change(my_string, command[1], command[2])
    elif command[0] == 'Includes':
        my_string = includes(my_string, command[1])
    elif command[0] == 'End':
        my_string = end(my_string, command[1])
    elif command[0] == 'Uppercase':
        my_string = uppercase(my_string)
    elif command[0] == 'FindIndex':
        findindex(my_string, command[1])
    elif command[0] == 'Cut':
        my_string = cut(my_string, int(command[1]), int(command[2]))
