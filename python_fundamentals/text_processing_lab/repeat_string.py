text = input().split()
combined_string = ''
for ch in text:
    for _ in range(len(ch)):
        combined_string += ch

print(combined_string)