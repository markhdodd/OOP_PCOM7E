class Cart:
    """
    Represents a shopping cart containing items selected by the customer.

    Attributes:
        items (dict): A dictionary where keys are item IDs and values are tuples of
                      (item object, quantity/weight, total price).
    """
    def __init__(self):
        """
        Initializes an empty cart.
        """
        self.items = {}

    def add_item(self, item, weight=None):
        """
        Adds an item to the cart or updates the quantity/weight if the item already exists.

        Args:
            item (InventoryItem): The item to add to the cart.
            weight (float, optional): Weight of the item if it's a weighable item.
        """
        if item.item_id in self.items:
            existing_item, current_qty_or_weight, _ = self.items[item.item_id]
            new_qty_or_weight = current_qty_or_weight + (weight or 1)
            total_price = item.calculate_total_price(new_qty_or_weight)
            self.items[item.item_id] = (existing_item, new_qty_or_weight, total_price)

        else:
            quantity_or_weight = weight if weight else 1
            total_price = item.calculate_total_price(quantity_or_weight)
            self.items[item.item_id] = (item, quantity_or_weight, total_price)

    def remove_item(self, item_id):
        """
        Removes an item from the cart by its id.

        Args:
            item_id (int): The ID of the item to remove.
        """
        if item_id in self.items:
            del self.items[item_id]

    def display_cart(self):
        """
        Displays all items in the cart, including their quantities/weights and total prices.
        """
        print("Cart Items:")
        for item_id, (item, qty_or_weight, total_price) in self.items.items():
            unit_label = "kg" if item.requires_weighing else "units"
            print(f"{item.name} - {qty_or_weight} {unit_label} - £{total_price:.2f}")

    def calculate_total(self):
        """
        calculates the total cost of all items in the cart.

        Returns:
            float: Total cost of the cart.
        """

        sumtotal = sum(total_price for _, _, total_price in self.items.values())

        return sumtotal