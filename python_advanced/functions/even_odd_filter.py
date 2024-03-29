def even_odd_filter(**kwargs):
    dictionary = {}
    for command in kwargs.keys():
        if command == 'even':
            dictionary['even'] = [num for num in kwargs[command] if num % 2 == 0]
        else:
            dictionary['odd'] = [num for num in kwargs[command] if num % 2 != 0]

    return dict(sorted(dictionary.items(), key=lambda x:-len(x[1])))



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))