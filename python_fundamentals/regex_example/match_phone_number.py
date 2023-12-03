import re
phone_number = input()
valid_phone_numbers = []
regex = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
matches = re.findall(regex, phone_number)
print(', '.join(matches))