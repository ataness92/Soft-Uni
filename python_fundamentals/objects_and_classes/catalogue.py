#!/usr/bin/env /tools/bin/python

class Catalogue:

    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        new_list = []
        for product in Catalogue.products:
            if product.startswith(first_letter):
                new_list.append(product)

        return new_list
                
    def __repr__(self):
        Catalogue.products.sort()
        message = f"Items in the {self.name} catalogue:"
        for name in Catalogue.products:
            message += f"\n{name}"

        return message


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
