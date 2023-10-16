vowels = ['a','o','u','e','i']
my_text = [x for x in input() if x.lower() not in vowels]
print(''.join(my_text))