employees_happiness = list(map(int, input().split()))
improvement = int(input())

overall_happines = list(map(lambda x: x*3, employees_happiness))

happy = [x for x in overall_happines if sum(overall_happines)/len(overall_happines) < x]

if len(happy) >= len(employees_happiness)//2:
    print(f'Score: {len(happy)}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy)}/{len(employees_happiness)}. Employees are not happy!')

