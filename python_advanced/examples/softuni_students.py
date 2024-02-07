def softuni_students(*args, **kwargs):
    my_list = []
    message = ""
    invalid_names = []
    for course_id, student_name in args:
        try:
            if kwargs[course_id]:
                my_list.append([student_name, kwargs[course_id]])
        except KeyError:
            invalid_names.append(student_name)

    for student, course in sorted(my_list):
        message += f"*** A student with the username {student} has successfully finished the course {course}!\n"
    if len(invalid_names) > 0:
        message += f"!!! Invalid course students: {', '.join([x for x in sorted(invalid_names)])}"

    return message


print(softuni_students(('id_1', 'Kaloyan9905'),id_1='Python Web Framework',))
print(softuni_students(('id_7', 'Silvester1'),('id_32', 'Katq21'),('id_7', 'The programmer'),id_76='Spring Fundamentals',id_7='Spring Advanced',))
print(softuni_students(('id_22', 'Programmingkitten'),('id_11', 'MitkoTheDark'),('id_321', 'Bobosa253'),('id_08', 'KrasimirAtanasov'),('id_32', 'DaniBG'),id_321='HTML & CSS',id_22='Machine Learning',id_08='JS Advanced',))
