my_vehicles = input().split('>>')
total_tax = 0
for vehicle in my_vehicles:
    car_type = vehicle.split()[0]
    years = int(vehicle.split()[1])
    kilometers = int(vehicle.split()[2])

    if car_type == 'family':
        initial_tax = 50
        reduced_tax = 5*years
        tax = initial_tax-reduced_tax+12*(kilometers//3000)
    elif car_type == 'heavyDuty':
        initial_tax = 80
        reduced_tax = 8*years
        tax = initial_tax-reduced_tax+14*(kilometers//9000)
    elif car_type == 'sports':
        initial_tax = 100
        reduced_tax = 9*years
        tax = initial_tax-reduced_tax+18*(kilometers//2000)
    else:
        print("Invalid car type.")
        continue
    total_tax += tax
    print(f'A {car_type} car will pay {tax:.2f} euros in taxes.')
print(f'The National Revenue Agency will collect {total_tax:.2f} euros in taxes.')