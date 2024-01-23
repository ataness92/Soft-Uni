n, m = map(int, input().split())
set1 = set()
set2 = set()
for i in range(n+m):
    if i < n :
        set1.add(input())
    else:
        set2.add(input())

print(*set1.intersection(set2), sep="\n")

