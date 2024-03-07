class Pizza:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def peperoni(cls):
        return cls(["tomato"])

    def print_me(self):
        print(self.ingredients)

my_pizza = Pizza.peperoni()
print(my_pizza.ingredients)
