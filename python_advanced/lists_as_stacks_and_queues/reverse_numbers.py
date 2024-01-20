numbers = input().split()
numbers_second = numbers.copy()
while numbers:
    print(numbers.pop(), end=' ')
numbers_second.reverse()
print()
print(*numbers_second)