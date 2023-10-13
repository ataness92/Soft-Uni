def sum_numbers(num1, num2):
    return num1+num2

num1 = int(input())
num2 = int(input())
num3 = int(input())

def substract(num1, num2):
    return num1 - num2

def add_and_substract(num1, num2, num3):
    result = sum_numbers(num1,num2)
    print(substract(result,num3))

add_and_substract(num1,num2,num3)


