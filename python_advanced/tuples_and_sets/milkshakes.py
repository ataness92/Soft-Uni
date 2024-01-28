from collections import deque

chocolate = [int(x) for x in input().split(',')]
cups = deque([int(x) for x in input().split(',')])

milkshake = 0

while chocolate and cups and milkshake < 5:
    el = chocolate.pop()
    cup = cups.popleft()

    if el <= 0 and cup <=0:
        continue
    elif el <= 0:
        cups.appendleft(cup)
        continue
    elif cup <= 0:
        chocolate.append(el)
        continue

    if el == cup:
        milkshake += 1
    else:
        cups.append(cup)
        chocolate.append(el-5)

if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolate) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups) or 'empty'}")