product = input()
quantity = int(input())

def price(product, quantity):
    if product == 'coffee':
        return "{:.2f}".format(quantity*1.50)
    elif product == 'water':
        return "{:.2f}".format(quantity*1.00)
    elif product == 'coke':
        return "{:.2f}".format(quantity*1.4)
    elif product == 'snacks':
        return "{:.2f}".format(quantity*2.00)

print(price(product,quantity))