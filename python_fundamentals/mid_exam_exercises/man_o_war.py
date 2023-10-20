pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
capacity = int(input())

def fire(lcommand: str, ship: list):
    index = int(lcommand.split()[1])
    damage = int(lcommand.split()[2])

    if 0 <= index < len(warship):
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()
        
def defend(lcommand: str, ship: list):
    startIndex = int(lcommand.split()[1])
    endIndex = int(lcommand.split()[2])
    damage = int(lcommand.split()[3])
    if  0 <= startIndex < len(pirate_ship)\
        and 0 <= endIndex < len(pirate_ship):
        for i in range(startIndex, endIndex+1):
            pirate_ship[i] = pirate_ship[i] - damage
            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()

def repair(lcommand: str, ship: list):
    index = int(lcommand.split()[1])
    health = int(lcommand.split()[2])

    if 0 <= index < len(pirate_ship):
        pirate_ship[index] += health
        if pirate_ship[index] > capacity:
            pirate_ship[index] = capacity   

def status(ship: list):
    count = 0
    for i in ship:
        if i < 0.2*capacity:
            count += 1
    print(f"{count} sections need repair.")
            
    

while True:
    command = input()
    if command == 'Retire':
        print(f"Pirate ship status: {sum(pirate_ship)}\n Warship status: {sum(warship)}")
        break
    elif command.startswith('Fire'):
        fire(command, warship)
    elif command.startswith('Defend'):
        defend(command, pirate_ship)
    elif command.startswith('Repair'):
        repair(command, pirate_ship)
    elif command.startswith('Status'):
        status(pirate_ship)
