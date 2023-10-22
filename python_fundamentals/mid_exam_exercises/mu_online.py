def potion(initial_health, heal: int):
    if initial_health + heal > 100:
        print(f'You healed for {100 - initial_health} hp.\n'
              f'Current health: {100} hp.')
        initial_health = 100
    else:
        initial_health += heal
        print(f'You healed for {heal} hp.\n'
              f'Current health: {initial_health} hp.')
    return initial_health

def chest(coin:int):
    print(f"You found {coin} bitcoins.")
    return coin

def monster(initial_health, room, my_monster: str, monster_attack: int):
    initial_health -= monster_attack
    if initial_health > 0:
        print(f"You slayed {my_monster}.")
    else:
        print(f"You died! Killed by {my_monster}.\n"
              f"Best room: {room}")
        exit()
    return initial_health

def main():
    dungeons_rooms = input().split("|")
    initial_health = 100
    room = 1
    all_bitcoins = 0

    for i in range(len(dungeons_rooms)):

        command = dungeons_rooms[i].split()[0]

        if command == 'potion':
            heal = int(dungeons_rooms[i].split()[1])
            initial_health = potion(initial_health,heal)
        elif command == 'chest':
            bitcoins = int(dungeons_rooms[i].split()[1])
            all_bitcoins +=chest(bitcoins)
        else:
            attack = int(dungeons_rooms[i].split()[1])
            initial_health = monster(initial_health, room, command, attack)

        room += 1

    if initial_health > 0:
        print(f"You've made it!\n"
              f"Bitcoins: {all_bitcoins}\n"
              f"Health: {initial_health}")

main()