n = int(input())
my_string = input()
my_list = list()
sorted_list = list()

for i in range(n):
    str = input()
    my_list.append(str)
    if my_string in str:
        sorted_list.append(str)

print(my_list)
print(sorted_list)
