class Customer:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def can_be_sold_to(self):
        return True
    
class AgeRestrictedItem(Customer):
    def __init__(self, age):
        super().__init__(age)
    
    def can_be_sold_to(self):
        pass

class ShoppingList(Item):
    def __init__(self, owner):
        self.__owner = owner
        self.__items = []
        super().__init__()

    @property
    def owner(self):
        return self.__owner

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

    def add(self, item):
        if not item.can_be_sold_to(self.owner):
            raise ValueError()
        self.__items.append(item)