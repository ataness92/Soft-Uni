def number_classification(number: int):
    positive_numbers, negative_numbers = []
    even_numbers, odd_numbers = []
    if number %2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

    return f"positive_numbers, negative_numbers, even_numbers, odd_numbers"
my_numbers = list(map(int, (input().split(', '))))
print(my_numbers)
print([number_classification(x) for x in my_numbers])

