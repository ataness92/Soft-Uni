from collections import deque

names = deque(input().split())
toss = int(input())

while len(names) > 1:
    for i in range(toss-1):
        names.append(names.popleft())

    print(f'Removed {names.popleft()}')

print(f'Last is {names.popleft()}')