def length_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False

def characters_are_valid(username):
    for ch in username:
        if not (ch.isalnum() or ch == '-' or ch == '_'):
            return False
    return True

def no_redundant_symbols(username):
    if " " in username:
        return False
    return True

def username_is_valid(username):
    if length_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        return True
    return False

user_names = input().split(', ')
for name in user_names:
    if username_is_valid(name):
        print(name)
