
class Order:
    #Represents an order placed by a customer.
    
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.cart = customer.cart
        self.status = "Pending"

    def finalize_order(self):
    
        #Marks the order as completed.
        self.status = "Completed"

    def __str__(self):
    
        #Displays the order details
        total = self.cart.calculate_total()
        return f"Order {self.order_id} | Total: ${total:.2f} | Status: {self.status}"
