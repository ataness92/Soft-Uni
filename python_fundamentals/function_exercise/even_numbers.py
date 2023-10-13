numbers = list(map(int, input().split()))
my_list = []
def check_even(x):
    if x%2==0:
        return True

    return False


my_list = list(filter(check_even, numbers))
print(my_list)