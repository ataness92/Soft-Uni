all_prices = list()
total_price_list = list()
discount = False
taxes = 0
while True:
    command = input()

    if command in ['special','regular']:
        if command == 'special':
            discount = True
        break

    no_taxed_price = float(command)
    if no_taxed_price < 0:
        print ("Invalid price!")
        continue
    taxes += no_taxed_price*0.2
    total_price_list.append(no_taxed_price)
    total_price = no_taxed_price*1.2
    all_prices.append(total_price)

message = f"Congratulations you've just bought a new computer!\nPrice without taxes: {sum(total_price_list):.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: "

if sum(all_prices)>0:
    if discount == True:
        print(f"{message}{0.9*sum(all_prices):.2f}$")
    else:
        print(f"{message}{sum(all_prices):.2f}$")
else:
    print("Invalid order!") 
