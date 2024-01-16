names_tuple = ([],)
number = int(input())

for _ in range(number):
    name = input()
    if name not in names_tuple[0]:
        names_tuple[0].append(name)

print('\n'.join(*names_tuple))

####Set ####
#names_set = set()
#for _ in range(int(input())):
#    names_set.add(input())
#print('\n'.join(names_set))

