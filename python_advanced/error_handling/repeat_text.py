text = input()

try:
    repeat = int(input())
    print(repeat*text)
except ValueError:
    print("Variable must be integer")
