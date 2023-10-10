n = int(input())
numbers = list()

for i in range(n):
    numbers.append(int(input()))

command = input()
new_list = numbers.copy()
for i in numbers:
    if command == 'even' and i%2 != 0:
        new_list.remove(i)
    elif command == 'odd' and i%2 == 0:
        new_list.remove(i)
    elif command == 'negative' and i >= 0:
        new_list.remove(i)
    elif command == 'positive' and i < 0:
        new_list.remove(i)
        
print(new_list)
