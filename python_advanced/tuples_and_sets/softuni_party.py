vip = set()
regular = set()
for _ in range(int(input())):
    code = input()
    if code[0].isdigit():
        vip.add(code)
    else:
        regular.add(code)

while True:
    code = input()
    if code == 'END':
        break

    if code[0].isdigit():
        vip.remove(code)
    else:
        regular.remove(code)

print(len(vip | regular))
print('\n'.join(vip))
print('\n'.join(regular))
