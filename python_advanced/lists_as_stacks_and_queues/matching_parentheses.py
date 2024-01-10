expression = input()
result = []

for i in range(len(expression)):
    if expression[i] == '(':
        result.append(i)
    elif expression[i] == ')':
        print(expression[result.pop():i+1])
