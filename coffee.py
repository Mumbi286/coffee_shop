class Coffee:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price
    
    def __str__(self):
        return f"Coffee:(name={self.name}, Size: {self.size}, Price: {self.price})"
    pass