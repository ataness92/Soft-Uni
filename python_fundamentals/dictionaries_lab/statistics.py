stock_dict = {}
while True:

    command = input().split(': ')

    if command[0] == 'statistics':
        break
    else:
        key = command[0]
        value = int(command[1])
        if key not in stock_dict:
            stock_dict[key] = 0
        stock_dict[key] += value

print("Products in stock:")

for (product, quantity) in stock_dict.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock_dict.keys())}")
print(f"Total Quantity: {sum(stock_dict.values())}")
