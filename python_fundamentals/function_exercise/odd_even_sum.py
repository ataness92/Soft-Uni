number = int(input())

def sum_of_strings(number):
    odd_sum = 0
    even_sum = 0

    my_number = str(number)
    for char in my_number:
        if int(char) % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'




def sum_of_int(number):
    even_sum = 0
    odd_sum = 0
    while number > 0:
        if (number%10) % 2 == 0:
            even_sum += number%10
        else:
            odd_sum += number%10
        number //= 10

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'



#print(sum_of_strings(number))
print(sum_of_int(number))
