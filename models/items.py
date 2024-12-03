class InventoryItem:
    """
    Base class representing an inventory item in the warehouse.

    Attributes:
        item_id (int): Unique identifier for the item.
        name (str): Name of the item.
        price (float): Price of the item.
        stock (int): Quantity of the item in stock.
    """

    def __init__(self, item_id, name, price, stock=0):
    
        """
        Initializes an inventory item.

        Args:
            item_id (int): Unique ID for the item.
            name (str): Name of the item.
            price (float): Price of the item.
            stock (int): Initial stock quantity (default is 0).
        """
    
        self.item_id = item_id
        self.name = name
        self.price = price
        self.stock = stock

    def calculate_total_price(self, quantity):
        """
        Calculates the total price for a given quantity.

        Args:
            quantity (int or float): Number of units or weight in kg.

        Returns:
            float: Total price for the specified quantity.
        """
        return self.price * quantity


class GeneralItem(InventoryItem):
    
    """
    Represents a general (non-age-restricted) item.

    Attributes:
        requires_weighing (bool): Indicates if the item needs to be weighed (e.g., produce).
    """
    
    def __init__(self, item_id, name, price, stock=0, requires_weighing=False):
        """
        Initializes a general item.

        Args:
            item_id (int): Unique ID for the item.
            name (str): Name of the item.
            price (float): Price of the item.
            stock (int): Initial stock quantity (default is 0).
            requires_weighing (bool): Whether the item needs weighing (default is False).
        """
        super().__init__(item_id, name, price, stock)
        self.requires_weighing = requires_weighing


class AgeRestrictedItem(GeneralItem):
    
    """
    Represents an age-restricted item (e.g., alcohol, cigarettes).

    Attributes:
        age_limit (int): Minimum age required to purchase the item.
    """
    
    def __init__(self, item_id, name, price, stock=0, age_limit=18):
    
        """
        Initializes an age-restricted item.

        Args:
            item_id (int): Unique ID for the item.
            name (str): Name of the item.
            price (float): Price of the item.
            stock (int): Initial stock quantity (default is 0).
            age_limit (int): Minimum age required to purchase the item (default is 18).
        """
    
        super().__init__(item_id, name, price, stock)
        self.age_limit = age_limit
