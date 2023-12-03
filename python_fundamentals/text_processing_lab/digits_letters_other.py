text = input()
digits = ''
letters = ''
characters = ''
for char in text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        characters +=char

print(f"{digits}\n{letters}\n{characters}")

name = 'Mario'
name = 'B' + name[1:]
print(name)