def rec_draw(n):
    if n == 0:
        return
    print("*"*n)
    rec_draw(n-1)
    print('#'*n)

num = int(input())
rec_draw(num)