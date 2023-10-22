number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
all_attendances = []
all_bonuses = []
for index in range(number_of_students):
    attendances = int(input())
    total_bonus = round(attendances/total_number_of_lectures*(5+additional_bonus))
    all_bonuses.append(total_bonus)
    all_attendances.append(attendances)

if len(all_bonuses) == 0:
    print(f'Max Bonus: 0.\n'
          f'The student has attended 0 lectures.')
else:
    print(f'Max Bonus: {max(all_bonuses)}.\n'
          f'The student has attended {all_attendances[all_bonuses.index(max(all_bonuses))]} lectures.')
