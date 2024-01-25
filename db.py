import tinydb

class GroceryDB:
    def __init__(self):
        self.db = tinydb.TinyDB('db.json')
        self.table = self.db.table('grocery')
        self.query = tinydb.Query()

    def grocery_add(self, fruit: dict):
        self.table.insert(fruit)
    
    def grocery_all(self):
        return self.table.all()
    
    def get_by_type(self, type: str)->list:
        return self.table.search(self.query.type == type)

    def get_by_name(self, name: str)->list:
        return self.table.search(self.query.name == name)
    
    def get_by_price(self, price: float)->list:
        return self.table.search(self.query.price==price)
    
    def get_by_quantity(self, quantity: int)->list:
        return self.table.search(self.query.quantity == quantity)
