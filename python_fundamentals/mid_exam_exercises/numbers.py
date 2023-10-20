sequence_of_numbers = [int(x) for x in input().split()]
sequence_of_numbers = list(sorted(sequence_of_numbers, key = lambda x: -x))
average = sum(sequence_of_numbers)//len(sequence_of_numbers)
length = len(sequence_of_numbers)
flag = False
if length > 5:
    length = 5
for x in range(length):
    if sequence_of_numbers[x] > average:
        print(sequence_of_numbers[x], end=' ')
        flag = True
else :
    if flag == False:
        print('No')