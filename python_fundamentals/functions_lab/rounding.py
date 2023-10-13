numbers = input().split()
print_list = list()
def rounder (numbers):
    for number in numbers:
        print_list.append(round(float(number)))
    return print_list

print(rounder(numbers))