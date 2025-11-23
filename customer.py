class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        def __str__(self):
            return f"Customer(name={self.name}, email={self.email})"
    pass