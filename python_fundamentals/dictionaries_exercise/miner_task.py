mine_dict = {}

while True:
    input_sequence = input()
    if input_sequence == 'stop':
        break
    else:
        if input_sequence not in mine_dict.keys():
            mine_dict[input_sequence] = int(input())
        else:
            mine_dict[input_sequence] += int(input())

for x, y in mine_dict.items():
    print(f"{x} -> {y}")

