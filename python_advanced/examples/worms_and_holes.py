from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

matches = 0
not_match = 0

while worms and holes:
    worm, hole = worms.pop(), holes.popleft()

    if worm == hole:
        matches += 1
        continue
    else:
        worm -= 3
    if worm >= 1:
        worms.append(worm)
    else:
        not_match = 1

if matches >0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")
if worms:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")
elif not_match:
    print("Worms left: none")
else:
    print(f"Every worm found a suitable hole!")

if holes:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")
else:
    print(f"Holes left: none")
