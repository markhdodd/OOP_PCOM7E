class User:

    #Base class for users of the system.

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Customer(User):

    #Customer who interacts with the checkout system.

    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.cart = None

    def add_to_cart(self, item):

        #Adds an item to the customer's cart.
        self.cart.add_item(item)

    def remove_from_cart(self, item_id):

        #Removes an item from the customer's cart.
        self.cart.remove_item(item_id)


class Staff(User):

    #Staff who manage approvals and overrides.

    def __init__(self, user_id, name, role):
        super().__init__(user_id, name)
        self.role = role

    def approve_age_restricted_item(self, order_id, item_name):

        #Approves an age-restricted item.
        return f"Approval granted for order {order_id}, item: {item_name}"
