
student_grades = {}       
number_of_students = int(input())
for _ in range(number_of_students):
    name, grade_as_string = input().split()
    if name not in student_grades:
        student_grades[name] = [float(grade_as_string)]
    else:
        student_grades[name].append(float(grade_as_string))

for name, grade in student_grades.items():
    print(name, end=' -> ')
    for index in range(len(grade)):
        print(f'{grade[index]:.2f} ', end='')
    print(f'(avg: {sum(grade)/len(grade):.2f})')
