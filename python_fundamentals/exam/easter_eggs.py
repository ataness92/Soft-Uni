import re

my_string = input()

pattern = r'[@#]+([a-z]{3,})[@#]([^a-zA-Z\d]+)?\/(\d+)\/'

matches = re.findall(pattern, my_string)
for match in matches:
    print(f'You found {match[2]} {match[0]} eggs!')
