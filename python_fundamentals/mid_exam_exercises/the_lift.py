def find_space(space: list, people: int):
    number_of_wagons = len(space)
    
    for wagon in range(number_of_wagons):
        while space[wagon] < 4 and people > 0:
            space[wagon] += 1
            people -= 1
    if space.count(4) < number_of_wagons:
        print(f"The lift has empty spots!")
        print(*space, sep=" ")
    elif people > 0:
        print(f"There isn't enough space! {people} people in a queue!")
        print(*space, sep=" ")
    else:
        print(*space, sep=" ")
        

people_waiting = int(input())
lift_space = list(map(int, input().split()))

find_space(lift_space, people_waiting)
