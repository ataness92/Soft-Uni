string1, string2 = input().split()
total_sum = 0
string1, string2 = list(string1), list(string2)

while len(string1) > 0 and len(string2) > 0:
    total_sum += ord(string1[0]) * ord(string2[0])
    string1.pop(0)
    string2.pop(0)

new_string = ''.join(string1) + ''.join(string2)
for ch in new_string:
    total_sum += int(ord(ch))

print(total_sum)