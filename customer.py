class Customer:
    def __init__(self, name, email):
        self.name = name 
        self.email = email

    @property #The name property getter method, allows accessing the customer name 
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # Lets validate 
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(new_name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")

    # if the validation passes ,store the value in the attribute
    self._name = new_name

        def __str__(self):
            return f"Customer(name={self.name}, email={self.email})"
    pass