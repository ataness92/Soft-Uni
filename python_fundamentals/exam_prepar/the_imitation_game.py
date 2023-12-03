
encrypted_message = list(input())

def move(number):
    if number >= len(encrypted_message):
        number = len(encrypted_message)-1
    for _ in range(0):
        encrypted_message.append(encrypted_message.pop(0))

def insert(index,value):
    encrypted_message.insert(index,value)

def change_all(substring, replacement):
    for n in range(len(encrypted_message)):
        if encrypted_message[n] == substring:
            encrypted_message[n] = replacement


while True:
    command = input().split('|')

    if command[0] == 'Decode':
        break
    elif command[0] == 'ChangeAll':
        change_all(command[1], command[2])
    elif command[0] == 'Move':
        move(int(command[1]))
    elif command[0] == 'Insert':
        insert(int(command[1]), command[2])

print(f"The decrypted message is: {''.join(encrypted_message)}")

