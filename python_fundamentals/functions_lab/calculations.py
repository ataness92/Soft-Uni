operator = input()
first_number = int(input())
second_number = int(input())

def calculate(operator, number_one, number_two):
    if operator == 'multiply':
        return number_one*number_two
    elif operator == 'divide':
        return number_one//number_two
    elif operator == 'add':
        return number_one+number_two
    elif operator == 'subtract':
        return number_one-number_two

print(calculate(operator,first_number,second_number))