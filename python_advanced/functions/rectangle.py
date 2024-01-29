def rectangle(length, width):
    def area():
        return length*width

    def perimeter():
        return 2*(length + width)

    if isinstance(length, int) and isinstance(width, int):
        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    else:
        return "Enter valid values!"

print(rectangle(2,10)) 
