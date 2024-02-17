from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

my_dict = {
    'Patch' : 0,
    'Bandage': 0,
    'MedKit':0
}
while textiles and medicaments:
    element = textiles.popleft()
    medicament = medicaments.pop()


    if element+medicament == 30:
        my_dict['Patch'] += 1
    elif element+medicament == 40:
        my_dict['Bandage'] += 1
    elif element+medicament == 100:
        my_dict['MedKit'] += 1
    elif element+medicament > 100:
        my_dict['MedKit']+=1
        sum = element+medicament-100
        medicaments[-1] += sum
    else:
        medicament+=10
        medicaments.append(medicament)

if not textiles and not medicaments:
    print(f"Textiles and medicaments are both empty.")
else:
    if not textiles:
        print(f"Textiles are empty.")
    if not medicaments:
        print(f"Medicaments are empty.")

for element, value in sorted(my_dict.items(), key = lambda x: (-x[1], x[0])):
    if value > 0:
        print(f"{element} - {value}")

if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments[::-1]])}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")


