text = list(input())
replace_char = ''
for n in range(len(text)):
    if replace_char != text[n]:
        replace_char = text[n]
    else:
        text[n] = ''

print(''.join(text))