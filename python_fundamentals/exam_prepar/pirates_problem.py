gold_dict = {}
people_dict = {}

def go_plunder(some_town, some_people, some_gold):
    found = 0
    destroyed = 0
    for key, value in gold_dict.items():
        if some_town == key:
            found = 1
            gold_dict[key] = value - int(some_gold)
            if gold_dict[key] <= 0:
                destroyed = 1
    for key, value in people_dict.items():
        if some_town == key:
            people_dict[key] = value - int(some_people)
            if people_dict[key] <= 0:
                destroyed = 1
    if destroyed == 1:
        del gold_dict[some_town]
        del people_dict[some_town]

    if found == 1:
        print(f"{some_town} plundered! {some_gold} gold stolen, {some_people} citizens killed.")
    if destroyed == 1:
        print(f"{some_town} has been wiped off the map!")

def go_prosper(some_town, some_gold):
    if some_town in gold_dict.keys():
        if int(some_gold) >= 0:
            gold_dict[some_town] += int(some_gold)
            print(f"{some_gold} gold added to the city treasury. {some_town} now has {gold_dict[some_town]} gold.")
        else:
            print(f"Gold added cannot be a negative number!")



def check_settlements(gld_dict,ppl_dict):
    if len(gld_dict) > 0:
        print(f"Ahoy, Captain! There are {len(gld_dict)} wealthy settlements to go to:")
        for key, value in people_dict.items():
            print(f"{key} -> Population: {value} citizens, Gold: {gold_dict[key]} kg")

while True:
    command = input()
    if command == 'Sail':
        break

    town, people, gold = command.split('||')
    if town not in gold_dict.keys():
        gold_dict[town] = int(gold)
        people_dict[town] = int(people)
    else:
        gold_dict[town] += int(gold)
        people_dict[town] += int(people)

while True:
    command = input()
    if command == 'End':
        break

    event = command.split("=>")[0]
    if event == 'Plunder':
        event, town, people, gold = command.split('=>')
        go_plunder(town,people,gold)
    elif event == 'Prosper':
        event, town, gold = command.split('=>')
        go_prosper(town, gold)

check_settlements(gold_dict, people_dict)