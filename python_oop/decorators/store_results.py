def store_results(func):
    def wrapper(*args, **kwargs):
        with open("files/log.txt", "a") as log_file:
            log_file.write(f"Function {func.__name__} was called."
                           f" Result: {func(*args, **kwargs)}")

    return wrapper

class store_results:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        def wrapper(*args, **kwargs):
            with open("files/log.txt", "a") as log_file:
                log_file.write(f"Function {self.func.__name__} was called."
                               f" Result: {self.func(*args, **kwargs)}")


class store_results_in_file_name():
    _DIR = "files"

    def __init__(self, file_name):
        self.file_name = file_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with open(f"{self._DIR}/{self.file_name}", "a") as log_file:
                log_file.write(f"Function {func.__name__} was called."
                               f" Result: {func(*args, **kwargs)}")
        return wrapper

@store_results
def sum_numbers(a:int, b: int):
    return a+b

sum_numbers(65, 6)