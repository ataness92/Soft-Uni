words = input().split()
palindrome = input()
found = 0
all_palindroms = [word for word in words if word == word[::-1]]
found = [found +1 for x in all_palindroms if palindrome==x]

print(f'{all_palindroms}\nFound palindrome {sum(found)} times')