number = int(input())

def loading_bar(number):

    print(f'{number}% ', end='')
    if number % 100 == 0:
        print(f"Complete!\n[{number//10*'%'}]")
    else:
        print(f"[{(number%100)//10*'%'}{((100-number)%100)//10*'.'}]\nStill loading...")


loading_bar(number)