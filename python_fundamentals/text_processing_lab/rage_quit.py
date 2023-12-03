text = list(input())
rage_dict = {}
char_list = []
my_char, my_digit, message = '', '', ''

for ch in text:
    if not ch.isdigit():
        if my_digit != '':
            message += my_char*int(my_digit)
            my_digit, my_char = '', ''

        my_char += ch.upper()
        if ch.upper() not in char_list:
            char_list.append(ch.upper())
    else:
        my_digit += ch
if my_digit != '':
    message += my_char*int(my_digit)
    my_digit, my_char = '', ''
print(f"Unique symbols used: {len(char_list)}")
print(message)



