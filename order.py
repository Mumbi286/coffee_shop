class Order:
    # Validates the customer is an instance of Customer
    if not isinstance(customer, Customer):
        raise ValueError("Invalid customer information.")

    # checks that every item in the coffee_items list is an instance of Coffee
    for item in coffee_items:
        if not isinstance(item, Coffee):
            raise ValueError("Invalid coffee item in the order.")
            
            # If validations pass, initialize the order
    def __init__(self, customer, coffee_items):
        self.customer = customer
        self.coffee_items = coffee_items  # List of Coffee objects
        
    pass