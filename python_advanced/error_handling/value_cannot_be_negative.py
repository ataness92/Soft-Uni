class ValueCannotBeNegativeError(Exception):
    """Raised when the input value is too small"""
    pass

for _ in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegativeError("Value Cannot Be Negative")
