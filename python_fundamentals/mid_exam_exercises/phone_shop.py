list_of_phones = input().split(', ')

while True:
    command = input().split(' - ')

    if command[0] == 'End':
        break

    phone = command[1]

    if command[0] == 'Add':
        if not phone in list_of_phones:
            list_of_phones.append(phone)
    elif command[0] == 'Remove':
        if phone in list_of_phones:
            list_of_phones.remove(phone)
    elif command[0] == 'Bonus phone':
        phone, next_phone = command[1].split(":")[0], command[1].split(":")[1]
        if phone in list_of_phones:
            index = list_of_phones.index(phone)
            list_of_phones.insert(index+1, next_phone)
    elif command[0] == 'Last':
        if phone in list_of_phones:
            list_of_phones.remove(phone)
            list_of_phones.append(phone)

print(', '.join(list_of_phones))
