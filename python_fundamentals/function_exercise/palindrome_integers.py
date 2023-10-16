list_of_numbers = input().split(', ')

def polindrome(my_list):
    for number in my_list:
        if number == number[::-1]:
            print("True")
        else:
            print("False")

polindrome(list_of_numbers)

