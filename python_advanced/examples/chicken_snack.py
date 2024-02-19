from collections import deque

amount_of_money = [int(x) for x in input().split()]
prices_of_food = deque(int(x) for x in input().split())

difference = 0
eaten_food = 0
while amount_of_money and prices_of_food:
    change = amount_of_money.pop()
    price = prices_of_food.popleft()

    if change == price:
        eaten_food += 1
        continue
    elif change > price:
        eaten_food+=1
        difference = change - price
        if amount_of_money:
            amount_of_money[-1] += difference
    else:
        continue

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
if eaten_food == 1 :
    print(f"Henry ate: {eaten_food} food.")
if eaten_food == 0:
    print("Henry remained hungry. He will try next weekend again.")
if 1 < eaten_food < 4:
    print(f"Henry ate: {eaten_food} foods.")

