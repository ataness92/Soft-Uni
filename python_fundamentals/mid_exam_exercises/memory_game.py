sequence_of_elements = input().split()

moves = 0
while True:
    command = input()

    if command == 'end':
        break
    else:
        my_numbers = [int(x) for x in command.split()]
        first_index, second_index = my_numbers[0], my_numbers[1]
    if len(sequence_of_elements) == 0:
        continue
    else:
        moves += 1

    if my_numbers[0] == my_numbers[1] or my_numbers[0] < 0 \
            or my_numbers[0] > len(sequence_of_elements) -1\
            or my_numbers[1] < 0 \
            or my_numbers[1] > len(sequence_of_elements) - 1:
        additional_element = '-'+str(moves)+'a'
        sequence_of_elements.insert(len(sequence_of_elements)//2, additional_element)
        sequence_of_elements.insert(len(sequence_of_elements)//2, additional_element)
        print("Invalid input! Adding additional elements to the board")
        continue

    if sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
        if second_index > first_index:
            sequence_of_elements.pop(second_index)
            sequence_of_elements.pop(first_index)
        else:
            sequence_of_elements.pop(first_index)
            sequence_of_elements.pop(second_index)
    else:
        print("Try again!")
        continue

        print(sequence_of_elements)

if len(sequence_of_elements) == 0:
    print(f'You have won in {moves} turns!')
else:
    print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")



