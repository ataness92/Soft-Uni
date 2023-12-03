sequence = input().split()
total_sum = 0
fletter_is_upper = 0
bletter_is_upper = 0
front_letter, back_letter = '',''

for word in sequence:
    sum = 0
    word = list(word)
    front_letter = word[0].upper()
    back_letter = word[-1].upper()
    fletter_is_upper, bletter_is_upper = word[0].isupper(), word[-1].isupper()
    word[0], word[-1] = '', ''
    number = int(''.join(word))

    if fletter_is_upper:
        sum += number/(ord(front_letter)-64)
    else:
        sum += number*(ord(front_letter)-64)
    if bletter_is_upper:
        sum -= (ord(back_letter)-64)
    else:
        sum += (ord(back_letter)-64)

    total_sum += sum

print(f'{total_sum:.2f}')

