from math import floor

group_size = int(input())
days = int(input())

money_earned = 0
spent_money = 0
for i in range(1, days+1):
    if i % 10 == 0:
        group_size = group_size -2
    if i % 15 == 0:
        group_size = group_size +5
    money_earned += 50
    spent_money += 2*group_size
    if i % 3 == 0:
        spent_money += 3*group_size
    if i % 5 == 0:
        money_earned += 20*group_size
        if i % 3 == 0:
            spent_money += 2*group_size
money_earned = money_earned - spent_money
print(f'{group_size} companions received {floor(money_earned/group_size)} coins each.')



