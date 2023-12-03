text = input()
while text != 'end':
    reversed_string = ''
    for ch in reversed(text):
        reversed_string += ch
    print(f'{text} = {reversed_string}')
    text = input()