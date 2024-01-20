from collections import deque
quantity = int(input())
people = deque()

command = input()

while command != 'Start':
    people.append(command)
    command = input()
command = input()
while command != 'End':
    data = command.split()

    if len(data) == 1:
        liters_requested = int(data[0])
        person = people.popleft()
        if quantity >= liters_requested:
            print(f'{person} got water')
            quantity-=liters_requested
        else:
            print(f'{person} must wait')
    elif len(data) == 2:
        liters_to_add = int(data[1])
        quantity+=liters_to_add

    command = input()

print(f'{quantity} liters left')


