my_list = [x for x in input() if x != ' ']
my_dict = {}
count = 0
for symbol in my_list:
    if symbol not in my_dict.keys():
        my_dict[symbol] = 1
    else:
        my_dict[symbol] += 1

for key,value in my_dict.items():
    print(f'{key} -> {value}')
