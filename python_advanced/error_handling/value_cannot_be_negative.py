class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass

amount_to_send = float(input())

if amount_to_send <= 0 < 1:
    raise ValueTooSmallError("Value is too low")

print("Pass")
