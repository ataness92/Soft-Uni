sequence_of_numbers = [int(x) for x in input().split(', ')]

max_value = max(sequence_of_numbers)
while True:
    for i in range(10, max_value+10, +10):
        list = [x for x in sequence_of_numbers if i-10<x<=i]
        print(f"Group of {i//10}0's: {list}")
    break
