number_of_balls = int(input())
print_result = 0
print_weight = 0
print_time = 0
print_quality = 0
result = 0
for i in range (number_of_balls):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    result = (weight/time_needed)**quality
    if print_result <= result:
        print_result = int(result)
        print_time = time_needed
        print_weight = weight
        print_quality = quality


print(f'{print_weight} : {print_time} = {print_result} ({print_quality})')


