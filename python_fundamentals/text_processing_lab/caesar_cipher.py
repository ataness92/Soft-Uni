encrypted_text = [chr(ord(char)+3) for char in list(input())]
print(''.join(encrypted_text))