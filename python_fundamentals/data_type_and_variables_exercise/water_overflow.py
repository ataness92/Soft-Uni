number_of_lines = int(input())
capacity = 255
total_liters = 0
for i in range(number_of_lines):
    liters_of_waters = int(input())
    if total_liters + liters_of_waters > 255:
        print("Insufficient capacity!")
    else:
        total_liters += liters_of_waters

print(total_liters)

        


