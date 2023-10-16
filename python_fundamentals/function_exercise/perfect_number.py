my_number = int(input())

def perfect_number(my_number):
    check_list = []
    for number in range(1, my_number):
        if my_number%number == 0:
            check_list.append(number)

    if sum(check_list) == my_number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

perfect_number(my_number)