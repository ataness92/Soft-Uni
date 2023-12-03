
student_dict = {}

while True:

    students_info = input()
    if len(students_info.split(":")) > 1:
        name, id, course = students_info.split(":")
        student_dict[name] = [id,course]
    else:
        course = students_info.replace('_', ' ')
        break

for key in student_dict.keys():
    if course.startswith(f'{student_dict[key][1]}'):
        print(f"{key} - {student_dict[key][0]}")

