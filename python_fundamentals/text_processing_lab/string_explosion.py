text = list(input())
left_strength = 0
for n in range(len(text)):
    if text[n] == '>' and n < len(text):
        strength = int(text[n+1]) + left_strength
        if left_strength > 0:
            left_strength = 0
        if n+1+strength > len(text):
            strength = len(text)
        else:
            strength = n + 1 + strength
        for i in range(n+1, strength,1):
            if text[i] == '>':
                left_strength = n+1+strength - i
                break
            text[i] = ''

print(''.join(text))
