class Warehouse:

    """
    Manages the inventory of items available in the store.

    Attributes:
        inventory (dict): A dictionary where keys are item IDs and values are item objects.
    """

    def __init__(self):
        #Initializes an empty inventory.
        
        self.inventory = {}

    def add_stock(self, item):

        """
        Adds an item to the warehouse inventory.

        Args:
            item (InventoryItem): The item to add to the inventory.
        """

        self.inventory[item.item_id] = item

    def deduct_stock(self, item_id, quantity):

        """
        Deducts stock for an item based on the quantity/weight purchased.

        Args:
            item_id (int): The ID of the item to deduct stock from.
            quantity (float): The amount of stock to deduct.

        Raises:
            ValueError: If there is insufficient stock to fulfill the deduction.
        """

        if item_id in self.inventory and self.inventory[item_id].stock >= quantity:
            self.inventory[item_id].stock -= quantity
        else:
            raise ValueError("Insufficient stock.")

    def list_items(self):

        """
        Lists all items in the warehouse inventory, including their prices and stock levels.
        """

        print("Available Items:")
        for item in self.inventory.values():
            unit = "per kg" if getattr(item, "requires_weighing", False) else "each"
            print(f"{item.item_id}: {item.name} - £{item.price:.2f} {unit} (Stock: {item.stock})")
