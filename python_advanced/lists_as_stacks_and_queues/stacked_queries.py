empty = []

for _ in range(int(input())):
    empty_data = [int(x) for x in input().split()]
    command = empty_data[0]
    if command == 1:
        empty.append(empty_data[1])
    elif not empty:
        pass
    elif command == 2:
        empty.pop()
    elif command == 3:
        print(max(empty))
    elif command == 4:
        print(min(empty))
if empty:
    empty.reverse()
    print(', '.join(map(str,empty)))

#print(*empty, sep=', ')
