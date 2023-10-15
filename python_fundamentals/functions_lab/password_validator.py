password = input()
password_valid = True
numbers_allowed = 0
chars_allowed = True
def check_password(password):
    global numbers_allowed
    global chars_allowed
    global password_valid

    if not 6 <= len(password) <= 10:
        print('Password must be between 6 and 10 characters')
        password_valid = False
    for i in password:
        if not (48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122):
            chars_allowed = False
            password_valid = False
        if 48 <= ord(i) <= 57:
            numbers_allowed = numbers_allowed +1

check_password(password)

if chars_allowed == False:
    print("Password must consist only of letters and digits")
if numbers_allowed <2:
    password_valid = False
    print("Password must have at least 2 digits")

if password_valid:
    print("Password is valid")

