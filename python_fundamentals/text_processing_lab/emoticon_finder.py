text = list(input())

for n in range(len(text)):
    if text[n] == ':':
        print(f' {text[n]}{text[n+1]}')