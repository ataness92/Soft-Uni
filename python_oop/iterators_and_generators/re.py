def reverse_text(string: str):
    idx = len(string)
    while idx > 0:
        yield string[idx-1]
        idx -= 1


for char in reverse_text()("step"):
    print(char, end='')