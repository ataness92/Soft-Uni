my_tuple = tuple([float(x) for x in input().split()])
same_values = {}
for num in my_tuple:
    if num not in same_values:
        same_values[num] = my_tuple.count(num)

for key, value in same_values.items():
    print(f'{key} - {value} times')
        
