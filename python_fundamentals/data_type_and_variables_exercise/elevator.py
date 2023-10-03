number_of_people = int(input())
capacity_of_elevator = int(input())

full_courses = number_of_people//capacity_of_elevator
half_courses = number_of_people%capacity_of_elevator

if full_courses > 0 and half_courses != 0:
    print(full_courses+1)
elif half_courses != 0:
    print(1)
else:
    print(full_courses)
