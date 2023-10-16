char1 = input()
char2 = input()

def ascii_range(char1, char2):
    for char in range(ord(char1)+1, ord(char2)):
        print(chr(char), end=' ')

ascii_range(char1,char2)