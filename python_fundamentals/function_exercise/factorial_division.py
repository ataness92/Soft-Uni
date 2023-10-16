import math

first_number = int(input())
second_number = int(input())

def factorial(x,y):
    return f"{math.factorial(x)//math.factorial(y):.2f}"

def factorial_two(x,y):
    first_factorial = 1
    second_factorial = 1

    for i in range(1,first_number+1):
        first_factorial *= i
    for i in range(1,second_number+1):
        second_factorial *= i

    return f"{first_factorial//second_factorial:.2f}"

print(factorial_two(first_number,second_number))
#print(factorial(first_number,second_number))