def type_check(some_type):

    def decorator(func):

        def wrapper(*args, **kwargs):

            if not all(isinstance(x, some_type) for x in args):
                return 'Bad Type'

            return func(*args)
        return wrapper

    return decorator

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter("Hello World"))

