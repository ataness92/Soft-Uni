string_numbers = input()
string_numbers = string_numbers.split(' ')
new_string = list()
#print(list(string_numbers.split(' ')))

for i in string_numbers:
    new_string.append(int(i)*(-1))

print(new_string)
