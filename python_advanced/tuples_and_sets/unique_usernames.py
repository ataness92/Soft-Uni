usernames = set()
for _ in range(int(input())):
    usernames.add(input())

print(*usernames, sep="\n")

#print(*{input() for _ in range(int(input()))}, sep="\n")