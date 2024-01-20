box_of_clothes = [int(x) for x in input().split()]
capacity = int(input())
used_capacity = 0
number_of_racks = 1

while box_of_clothes:
    new_cloth = box_of_clothes.pop()
    if used_capacity+new_cloth > capacity:
        number_of_racks+=1
        used_capacity = 0+new_cloth
    else:
        used_capacity+=new_cloth

print(number_of_racks)

