string_of_integers = input().split(', ')
beggars = int(input())

money_list = []

for index in string_of_integers:
    money_list.append(int(index))

final_sums = []
start_index = 0

while start_index < beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_list), beggars):
        current_beggar_sum += money_list[current_index]

    final_sums.append(current_beggar_sum)
    start_index += 1

print(final_sums)


