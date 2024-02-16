def rec_fact(num):
    if num == 1:
        return num
    else:
        return num*rec_fact(num-1)

num = int(input())
print(rec_fact(num))