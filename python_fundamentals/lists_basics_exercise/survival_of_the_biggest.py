list_numbers = input().split()
list_numbers_int = [int(list_numbers[i]) for i in range(len(list_numbers))]
n = int(input())

for i in range(n):
    list_numbers_int.remove(min(list_numbers_int))

for i in range(len(list_numbers_int)):
    if i != len(list_numbers_int)-1:
        print(f'{list_numbers_int[i]}, ', end='')
    else:
        print(f'{list_numbers_int[i]}', end ='')
