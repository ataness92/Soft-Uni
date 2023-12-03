import re

my_string = input()
pattern = r'([=]{1}|[\/]{1})([A-Z][A-Za-z][A-Za-z]+)(\1)'

matches = re.findall(pattern,my_string)

travel_points = 0
message = 'Destinations: '
for match in matches:
    travel_points += len(match[1])
    message += f'{match[1]}, '
if len(matches) > 0:
    print(message[:-2])
else:
    print(message)
print(f'Travel Points: {travel_points}')