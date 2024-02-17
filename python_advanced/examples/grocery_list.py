def shop_from_grocery_list(budget, grocery_list, *products):
    my_budget = budget

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {my_budget:.2f}."

    for name, money in products:
        if name not in grocery_list:
            continue
        if my_budget >= money:
            grocery_list.remove(name)
            my_budget -= money
        else:
            break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {my_budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))