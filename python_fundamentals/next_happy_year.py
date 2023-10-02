year = int(input()) + 1
while True:
    for n in str(year):
        if str(year).count(n) > 1:
            year += 1
            break
    else:
        print(year)
        break
