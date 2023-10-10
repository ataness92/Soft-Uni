factor = int(input())
count  = int(input())
number = factor
my_list = list()
while count > 0:
    if number % factor == 0:
        my_list.append(number)
        count -= 1
    number += factor
    
print(my_list)  
