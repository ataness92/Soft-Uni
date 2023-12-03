import re

pattern = r'[@][#]+([A-Z][A-Za-z0-9]*[A-Z])'

number = int(input())

for _ in range(number):
    barcode = input()
    match = re.findall(pattern,barcode)
    group = ''
    if len(match) > 0:
        for ch in match[0]:
            if ch.isdigit():
                group += ch

        if group == '':
            group = '00'
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")


