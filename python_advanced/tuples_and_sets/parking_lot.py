parking_lot = set()

for _ in range(int(input())):
    direction, number = input().split(', ')
    if direction == 'IN':
        parking_lot.add(number)
    else:
        parking_lot.remove(number)

if parking_lot:
    print('\n'.join(parking_lot))
else:
    print("Parking Lot is Empty")
