from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption = deque(int(x) for x in input().split())
necessary_amount_of_fuel = deque(int(x) for x in input().split())
message = ""
reached_top = 1
reached = 0
reached_list = []
while initial_fuel and additional_consumption:
    fuel = initial_fuel.pop()
    index = additional_consumption.popleft()
    needed_fuel = necessary_amount_of_fuel.popleft()

    if fuel-index >= needed_fuel:
        print(f"John has reached: Altitude {reached+1}")
        reached += 1
        reached_list.append(f"Altitude {reached}")
    else:
        print(f"John did not reach: Altitude {reached+1}")
        reached_top = 0
        break

if len(reached_list) == 0:
    print(f"John failed to reach the top.\nJohn didn't reach any altitude.")
elif not reached_top:
    print("John failed to reach the top.")
    print(f"Reached altitudes: ", end='')
    print(*reached_list, sep=', ')
else:
    print("John has reached all the altitudes and managed to reach the top!")
