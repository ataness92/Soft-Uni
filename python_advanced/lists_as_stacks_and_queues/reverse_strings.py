my_word = list(input())
reverse_stack_word = []

for i in range(len(my_word)):
    reverse_stack_word.append(my_word.pop())

print("".join(reverse_stack_word))
