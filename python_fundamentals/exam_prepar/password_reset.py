my_string = input()


def take_odd(string):
    new_string = ''
    for i in range(1, len(string), 2):
        new_string += string[i]
    return new_string


def cut(string, my_index, my_length):
    substring = string[my_index:(my_index+my_length)]
    string = string.replace(substring, '', 1)
    return string


def substitute(string, some_string, some_substitute):
    if some_string in string:
        string = string.replace(some_string,some_substitute)
        print(string)
    else:
        print("Nothing to replace!")
    return string


while True:
    command = input()

    if command == 'Done':
        break

    command = command.split()

    if command[0] == 'TakeOdd':
        my_string = take_odd(my_string)
        print(my_string)
    elif command[0] == 'Cut':
        my_string = cut(my_string, int(command[1]), int(command[2]))
        print(my_string)
    elif command[0] == 'Substitute':
        my_string = substitute(my_string,command[1],command[2])


print(f'Your password is: {my_string}')
