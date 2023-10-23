
class Inventory:

    items = []
    __capacity = 0
    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        Inventory.__capacity = __capacity
        self.students = []
        self.grades = []
        
    def add_item(self, item: str):
        if self.__capacity > 0:
            self.__capacity -= 1
            Inventory.items.append(item)
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return Inventory.__capacity

    def __repr__(self):
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {self.__capacity}"
        


inventory = Inventory(1)
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
