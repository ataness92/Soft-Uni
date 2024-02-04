from string import punctuation

with open("file_1.txt", 'r') as file:
    list_of_lines = file.readlines()

with open("output.txt", 'w') as file:
    for idx in range(len(list_of_lines)):
        letter, symbol = 0, 0
        for char in list_of_lines[idx]:
            if char.isalpha():
                letter += 1
            elif char in punctuation:
                symbol += 1
        file.writelines(f"Line {idx+1}: {''.join(list_of_lines[idx][:-1])} ({letter})({symbol})\n")