numbers = input().split()
list_out = list()

for number in numbers:
    list_out.append(abs(float(number)))

print(list_out)