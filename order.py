class Order:
    def __init__(self, customer, coffee_items):

        # validates the customer is an instance of Cusotomer
        if not isinstance(customer, Customer):
            raise ValueError("customer must be an instance of Customer class")

        # Checks that every item in coffee_items is an instance of Coffee
        for item in coffee_items:
            if not isinstance(item, Coffee):
                raise ValueError("All items in coffee_items must be instances of Coffee class")
        self.customer = customer
        self.coffee_items = coffee_items #list of Coffe objects

        # Calculates total price of the order
        def total_price(self):
            return sum(item.price for item in self.coffee_items)
        
    pass