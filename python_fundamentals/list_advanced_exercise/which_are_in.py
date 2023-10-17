first_string = input().split(', ')
second_string = input().split(', ')

def find_match(some_string : list, other_string: list) -> list:
    new_string = []
    for element in first_string:
        for second_element in second_string:
            if element not in new_string and element in second_element:
                new_string.append(element)

    return new_string

print(find_match(first_string, second_string))