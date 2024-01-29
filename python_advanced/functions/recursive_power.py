def recursive_power(number, power):
    if power > 1:
        number = number*recursive_power(number,power-1)
        
    return number
