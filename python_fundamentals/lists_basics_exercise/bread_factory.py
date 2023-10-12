initial_energy = 100
initial_coins = 100

day_events = input().split('|')
new_list = list()
finished_day = True

for event in day_events:
    new_list.append(event.split('-'))

for event in new_list:
    if 'rest' in event:
        current_energy = initial_energy
        initial_energy += int(event[1])
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy-current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {initial_energy}.')
    elif 'order' in event:
        if initial_energy - 30 >= 0:
            initial_coins += int(event[1])
            initial_energy -= 30
            print(f'You earned {event[1]} coins.')
        else:
            initial_energy += 50
            print('You had to rest!')
    else:
        if initial_coins - int(event[1])>=0:
            initial_coins -= int(event[1])
            print(f'You bought {event[0]}.')
        else:
            print(f'Closed! Cannot afford {event[0]}.')
            finished_day = False
            break

if finished_day:
    print(f"Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}")

