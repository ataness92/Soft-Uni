my_version = list(map(int, input().split('.')))

def set_next_version(current_version):
    carrier = 0
    new_version = []
    for number in range(len(current_version)-1, -1, -1):
        if carrier == 1 and current_version[number] == 9:
            current_version[number] = 0
        elif carrier == 1:
            current_version[number] += 1
            carrier = 0
        elif current_version[number] == 9:
            current_version[number] = 0
            carrier = 1
        else:
            current_version[number] += 1
        if carrier == 0 :
            new_version = list(map(str, current_version))
            break
    print('.'.join(new_version))

set_next_version(my_version)