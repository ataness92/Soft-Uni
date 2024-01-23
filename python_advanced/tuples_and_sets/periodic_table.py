elements = set()
for _ in range(int(input())):
    element = set(input().split())
    elements = elements.union(element)
    # for element in input().split():
    #     elements.add(element)

print(*elements, sep="\n")

#print(*{el for _ in range(int(input())) for el in input().split()}, sep='\n')