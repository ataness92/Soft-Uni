string_input = input().split('#')
water_amount = int(input())
fire_list = [elements.split(' = ') for elements in string_input]

valid_cell = True

total_fire = 0
total_efford = 0
print("Cells:")
for element in fire_list:
    type_of_fire, range_of_fire = element[0], element[1]
    if (type_of_fire == 'High' and 80<int(range_of_fire)<126)\
        or (type_of_fire == 'Medium' and 50<int(range_of_fire)<81)\
        or (type_of_fire == 'Low' and 0<int(range_of_fire)<51):
        if water_amount - int(range_of_fire) >=0:
            water_amount -= int(range_of_fire)
            total_fire +=int(range_of_fire)
            total_efford += 0.25*int(range_of_fire)
            print(f" - {range_of_fire}")

print(f'Effort: {total_efford:.2f}')
print(f'Total Fire: {total_fire}')



