list_of_char = input().split(", ")

ascii_dict = {char: ord(char) for char in list_of_char}
print(ascii_dict)
