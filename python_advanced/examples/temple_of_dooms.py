from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challanges = [int(x) for x in input().split()]

while True:
    tool = tools.popleft()
    substance = substances.pop()
    sum = tool*substance

    if sum in challanges:
        equal = challanges.index(sum)
        challanges.pop(equal)
    else:
        tool += 1
        substance -= 1
        tools.append(tool)
        if substance > 0:
            substances.append(substance)

    if (not substances or not tools) and challanges:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break

    if not challanges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if tools:
    print(f"Tools:", ', '.join([str(x) for x in tools]))
if challanges:
    print(f"Challenges:", ', '.join([str(x) for x in challanges]))
if substances:
    print(f"Substances:", ', '.join([str(x) for x in substances]))