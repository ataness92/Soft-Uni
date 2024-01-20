from collections import deque
store = deque()
while True:
    command = input()

    if command == 'End':
        break
    elif command == 'Paid':
        while store:
            print(store.popleft())
    else:
        store.append(command)

print(f'{len(store)} people remaining.')