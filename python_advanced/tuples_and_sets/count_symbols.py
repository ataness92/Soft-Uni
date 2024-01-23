#my_dict = {}
#
#for i in input():
#    my_dict[i] = my_dict.get(i,0)+ 1
#
#for char, times in sorted(my_dict.items()):
#    print(f'{char}: {times} time/s')

text = input()

for symbol in sorted(set(text)):
    print(f'{symbol}: {text.count(symbol)} time/s')