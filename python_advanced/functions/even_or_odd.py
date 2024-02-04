# def even_odd(*args):
#     list = []
#     for x in range(len(args)-1):
#         if args[-1] == 'even' and args[x]%2 == 0:
#             list.append(args[x])
#         elif args[-1] == 'odd' and args[x]%2 != 0:
#             list.append(args[x])
#
#     return list

def even_odd(*args):
    command = args[-1]

    if command == "even":
        return [num for num in args[:-1] if num % 2 == 0]
    else:
        return [num for num in args[:-1] if num % 2 == 0]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))