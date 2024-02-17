def accommodate_new_pets(capacity, weight_limit, *animals):
    animal_dict = {}
    left_capacity = capacity
    accomplished = 1
    message = ""

    for animal, weight in animals:
        if left_capacity == 0:
            accomplished = 0
            break
        if animal not in animal_dict and weight <= weight_limit:
            animal_dict[animal] = 1
            left_capacity -= 1
        else:
            if weight > weight_limit:
                continue
            animal_dict[animal] += 1
            left_capacity -= 1

    if accomplished:
        message += f"All pets are accommodated! Available capacity: {left_capacity}.\nAccommodated pets:"
    else:
        message += f"You did not manage to accommodate all pets!\nAccommodated pets:"

    return_dict = sorted(animal_dict.items(), key = lambda x: x[0])

    for animal, numbers in return_dict:
        message += f"\n"
        message += f"{animal}: {numbers}"

    return message

print(accommodate_new_pets(10,15.0,("cat", 5.8),("dog", 10.0),))
print(accommodate_new_pets(10,10.0,("cat", 5.8),("dog", 10.5), ("parrot", 0.8),("cat", 3.1),))
print(accommodate_new_pets(2,15.0,("dog", 10.0),("cat", 5.8),("cat", 2.7),))