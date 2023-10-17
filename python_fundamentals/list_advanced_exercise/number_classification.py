def number_classification(numbers: list):
    positive_numbers, negative_numbers = [],[]
    even_numbers, odd_numbers = [],[]
    for number in numbers:
        if number %2 == 0:
            even_numbers.append(str(number))
        else:
            odd_numbers.append(str(number))
        if number >= 0:
            positive_numbers.append(str(number))
        else:
            negative_numbers.append(str(number))

    return f"Positive: {', '.join(positive_numbers)}\nNegative: {', '.join(negative_numbers)}\nEven: {', '.join(even_numbers)}\nOdd: {', '.join(odd_numbers)}"


my_numbers = [int(x) for x in input().split(', ')]
print(number_classification(my_numbers))
