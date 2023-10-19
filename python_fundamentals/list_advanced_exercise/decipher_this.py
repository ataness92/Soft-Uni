message = input().split()
new_message = []
for word in message:
    digit = ''.join([x for x in word if x.isdigit()])
    new_word = list(chr(int(digit))+''.join([x for x in word if not x.isdigit()]))
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    print("".join(new_word), end=" ")