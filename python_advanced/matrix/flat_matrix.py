rows = int(input())
flat_matrix = []
for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    flat_matrix.extend(data)
print(flat_matrix)
