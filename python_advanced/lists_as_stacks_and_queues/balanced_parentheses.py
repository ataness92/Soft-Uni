start = 1
my_string = list(input())
my_stack = []
for i in my_string:
    if ord(i) not in [40,91,123] and start:
        print("NO")
        break
    start = 0
    if ord(i) in [40,91,123]:
        my_stack.append(i)
    else:
        if my_stack:
            matching = my_stack.pop()
        else:
            print("NO")
            break
        if(ord(i) == 41 and ord(matching) == 40):
            continue
        elif(ord(i) == 93 and ord(matching) == 91):
            continue
        elif(ord(i) == 125 and ord(matching) == 123):
            continue
        else:
            print("NO")
            break
else:
    print("YES")
