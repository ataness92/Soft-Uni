from collections import deque

armor_of_monsters = deque(int(x) for x in input().split(','))
striking_impact = [int(x) for x in input().split(',')]
monsters_killed = 0

while armor_of_monsters and striking_impact:
    monster = armor_of_monsters.popleft()
    strike = striking_impact.pop()

    if strike >= monster:
        strike -= monster
        monsters_killed += 1
        if strike > 0:
            if len(striking_impact)==0:
                striking_impact.append(strike)
            else:
                striking_impact[-1] += strike
    else:
        monster -= strike
        armor_of_monsters.append(monster)

if not armor_of_monsters:
    print("All monsters have been killed!")
if not striking_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")

#20,15,10
#5,15,10,25