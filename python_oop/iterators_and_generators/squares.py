def squares(n: int):
    idx = 1
    while idx <= n:
        yield idx*idx
        idx += 1

print(list(squares(5)))