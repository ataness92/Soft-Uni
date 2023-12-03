number_of_words = int(input())
my_dict = {}
for _ in range(number_of_words):
    word = input()
    synonym = input()
    if word not in my_dict.keys():
        my_dict[word] = [synonym]
    else:
        my_dict[word].append(synonym)
for word in my_dict:
    print(f"{word} - {', '.join(my_dict[word])}")
