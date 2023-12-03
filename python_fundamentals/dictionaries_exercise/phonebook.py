phonebook = {}

while True:

    contacts = input().split('-')

    if len(contacts) > 1:
        phonebook[contacts[0]] = contacts[1]
    else:
        number = int(contacts[0])
        break

for i in range(number):
    target_name = input()
    if target_name in phonebook.keys():
        print(f"{target_name} -> {phonebook[target_name]}")
    else:
        print(f"Contact {target_name} does not exist.")