first_students_per_hour = int(input())
second_students_per_hour = int(input())
third_students_per_hour = int(input())

number_of_students = int(input())
hours = 0
combined_hours = first_students_per_hour+second_students_per_hour+third_students_per_hour

while number_of_students > 0:
    if hours%4 == 0 and hours > 0:
        hours+=1
    hours += 1
    number_of_students -= combined_hours
    if hours%4 == 0 and hours > 0:
        hours+=1

print(f"Time needed: {hours}h.")

