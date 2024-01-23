result_odd = set()
result_even = set()
for row in range(1,int(input())+1):
    result = sum(ord(x) for x in input())//row

    if result % 2 == 0:
        result_even.add(result)
    else:
        result_odd.add(result)

if sum(result_even) == sum(result_odd):
    print(*result_odd.union(result_even), sep=', ')
elif sum(result_odd) > sum(result_even):
    print(*result_odd.difference(result_even), sep=', ')
else:
    print(*result_odd.symmetric_difference(result_even), sep=', ')