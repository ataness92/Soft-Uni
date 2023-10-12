TRAIN_TICKET = 150
CLOTHES_MAX_PRICE = 50.00
SHOES_MAX_PRICE = 35.00
ACCESSORIES_MAX_PRICE = 20.50

my_list = input().split('|')
budget = int(input())
profit = budget
list_prices = list()
for elements in my_list:
    item, price = elements.split('->')

    if ((item == 'Clothes' and float(price) <= CLOTHES_MAX_PRICE)\
            or (item == 'Shoes' and float(price) <= SHOES_MAX_PRICE)\
            or (item == 'Accessories' and float(price) <= ACCESSORIES_MAX_PRICE))\
            and (budget - float(price)) >= 0:
        budget -= float(price)
        list_prices.append(float(price)*1.4)
profit, budget = budget, profit
for prices in list_prices:
    print(f'{prices:.2f} ', end='')
    profit += prices
print(f'\nProfit: {profit-budget:.2f}')
if profit > TRAIN_TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")




