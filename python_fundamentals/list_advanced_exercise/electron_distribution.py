number_of_electrons = int(input())
list_of_shells = []
start = 1
while True:
    needed_electrons = 2*(start**2)
    if needed_electrons < number_of_electrons:
        number_of_electrons -= needed_electrons
        list_of_shells.append(needed_electrons)
        start += 1
    else:
        list_of_shells.append(number_of_electrons)
        break


print(list_of_shells)