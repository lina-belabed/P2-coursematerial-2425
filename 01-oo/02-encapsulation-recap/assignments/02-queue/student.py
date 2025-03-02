class Queue:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        if isinstance(item, str):
            self.items.append(item)
        else:
            return ValueError("Item has to be type string.")

    def next(self):
        return self.items.pop(0)
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False