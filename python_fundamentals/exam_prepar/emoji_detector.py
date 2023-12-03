import re

def calculate_coolness(my_emojie):
    sum = 0
    for ch in my_emojie:
        sum += ord(ch)

    if sum > cool_threshold:
        return True
    return False

my_string = input()

#pattern = r'([:*]{2})([A-Z][a-z][a-z]+)(\1)'
pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
emoji_matches = re.findall(pattern,my_string)

cool_matches = re.findall(r'\d',my_string)
cool_threshold = 1

for i in cool_matches:
    cool_threshold *= int(i)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emoji_matches)} emojis found in the text. The cool ones are:')
for match in emoji_matches:
    if calculate_coolness(match[1]):
        print(''.join(match))
