number = int(input())
plant_dict = {}
rate_dict = {}
for _ in range(number):
    plant, rarity = input().split('<->')

    if plant not in plant_dict.keys():
        plant_dict[plant] = int(rarity)
    else:
        plant_dict[plant] += int(rarity)

def do_rate(my_plant, my_rate):
    if my_plant not in plant_dict.keys():
        print('error')
        return
    if my_plant not in rate_dict.keys():
        rate_dict[my_plant] = my_rate
    else:
        rate_dict[my_plant] += f",{my_rate}"

def update(my_plant, my_rarity):
    if my_plant not in plant_dict.keys():
        print('error')
        return
    else:
        plant_dict[my_plant] = int(my_rarity)

def reset(my_plant):
    if my_plant not in plant_dict.keys():
        print('error')
    else:
        rate_dict[my_plant] = '0'

command = input()

while command != 'Exhibition':
    command = command.split(': ')
    if command[0] == 'Rate':
        a_plant, rate = command[1].split(' - ')
        do_rate(a_plant, rate)
    elif command[0] == 'Update':
        my_plant, rarity = command[1].split(' - ')
        update(my_plant, rarity)
    elif command[0] == 'Reset':
        reset(command[1])

    command = input()

print('Plants for the exhibition:')
for key, value in plant_dict.items():
    if key in rate_dict.keys():
        avr = rate_dict[key].split(',')
        avr_list = [int(x) for x in avr]
        avr_sum = sum(avr_list)/len(avr_list)
    else:
        avr_sum = 0
    print(f'- {key}; Rarity: {value}; Rating: {avr_sum:.2f}')