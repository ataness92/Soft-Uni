from collections import deque

cups_capacity = deque(map(int,input().split()))
bottles_capacity = [int(x) for x in input().split()]
waster_water = 0
my_cup = 0
while cups_capacity and bottles_capacity:
    my_bottle = bottles_capacity.pop()

    if my_cup == 0:
        my_cup = cups_capacity.popleft()
    if my_bottle >= my_cup:
        waster_water = waster_water + (my_bottle-my_cup)
        my_cup = 0
    else:
        my_cup = my_cup-my_bottle

if cups_capacity:
    if my_cup > 0:
        cups_capacity.appendleft(my_cup)
    print("Cups:", *cups_capacity)
else:
    print("Bottles:", *bottles_capacity)

print(f'Wasted litters of water: {waster_water}')