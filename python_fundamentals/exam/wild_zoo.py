animal_dict = {}


def add(animal_name, needed_food, some_area):
    if animal_name not in animal_dict.keys():
        animal_dict[animal_name] = [needed_food, some_area]
    else:
        animal_dict[animal_name][0] += needed_food

def feed(animal_name, some_food):
    if animal_name in animal_dict:
        animal_dict[animal_name][0] -= some_food
        if animal_dict[animal_name][0] <= 0:
            del animal_dict[animal_name]
            print(f'{animal_name} was successfully fed')


while True:
    command = input()
    if command == 'EndDay':
        break

    command = command.split(': ')
    if command[0] == 'Add':
        name, quantity, area = command[1].split('-')
        add(name, int(quantity), area)
    elif command[0] == 'Feed':
        name, food = command[1].split('-')
        feed(name, int(food))

area_dict = {}
count = 0
print('Animals:')
for key, value in animal_dict.items():
    print(f' {key} -> {value[0]}g')
    if value[1] in area_dict.keys():
        area_dict[value[1]] += 1
    else:
        area_dict[value[1]] = 1

print('Areas with hungry animals:')
for key, value in area_dict.items():
    print(f' {key}: {value}')