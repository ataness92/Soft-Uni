n = int(input())

for i in range (97, 97+n):
    for j in range(97, 97+n):
        for k in range(97, 97+n):
            print(f'{chr(i)}{chr(j)}{chr(k)}')

