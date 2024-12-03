from models.items import GeneralItem, AgeRestrictedItem
from services.warehouse import Warehouse

def populate_warehouse():
    """
    Populates the warehouse with a variety of items across multiple categories, including
    scannable, weighable, and age-restricted items.

    Returns:
        Warehouse: The warehouse object populated with items.
    """
    warehouse = Warehouse()

    # General Scannable Items
    warehouse.add_stock(GeneralItem(1, "Milk", 1.55, stock=50))
    warehouse.add_stock(GeneralItem(2, "Bread", 1.00, stock=30))
    warehouse.add_stock(GeneralItem(3, "Eggs", 2.96, stock=40))
    warehouse.add_stock(GeneralItem(4, "Butter", 2.20, stock=25))
    warehouse.add_stock(GeneralItem(5, "Cheese", 3.50, stock=20))
    warehouse.add_stock(GeneralItem(6, "Cereal", 2.80, stock=35))
    warehouse.add_stock(GeneralItem(7, "Orange Juice", 2.00, stock=15))
    warehouse.add_stock(GeneralItem(8, "Yogurt", 1.80, stock=40))
    warehouse.add_stock(GeneralItem(9, "Chips", 1.50, stock=50))
    warehouse.add_stock(GeneralItem(10, "Chocolate Bar", 0.85, stock=60))

    # Age-Restricted Items
    warehouse.add_stock(AgeRestrictedItem(11, "Wine", 6.00, stock=20, age_limit=18))
    warehouse.add_stock(AgeRestrictedItem(12, "Whiskey", 25.00, stock=10, age_limit=18))
    warehouse.add_stock(AgeRestrictedItem(13, "Vodka", 18.00, stock=15, age_limit=18))
    warehouse.add_stock(AgeRestrictedItem(14, "Beer", 1.80, stock=50, age_limit=18))
    warehouse.add_stock(AgeRestrictedItem(15, "Cigarettes", 12.00, stock=40, age_limit=18))
    warehouse.add_stock(AgeRestrictedItem(16, "Energy Drink", 1.50, stock=30, age_limit=16))

    # Weighable Items
    warehouse.add_stock(GeneralItem(17, "Apples", 2.50, stock=100, requires_weighing=True))
    warehouse.add_stock(GeneralItem(18, "Bananas", 1.80, stock=80, requires_weighing=True))
    warehouse.add_stock(GeneralItem(19, "Potatoes", 0.90, stock=150, requires_weighing=True))
    warehouse.add_stock(GeneralItem(20, "Tomatoes", 2.80, stock=70, requires_weighing=True))
    warehouse.add_stock(GeneralItem(21, "Carrots", 1.20, stock=120, requires_weighing=True))
    warehouse.add_stock(GeneralItem(22, "Onions", 1.00, stock=100, requires_weighing=True))
    warehouse.add_stock(GeneralItem(23, "Grapes", 3.50, stock=50, requires_weighing=True))
    warehouse.add_stock(GeneralItem(24, "Strawberries", 5.00, stock=40, requires_weighing=True))
    warehouse.add_stock(GeneralItem(25, "Blueberries", 6.00, stock=30, requires_weighing=True))
    warehouse.add_stock(GeneralItem(26, "Pears", 2.30, stock=90, requires_weighing=True))

    # Household Items
    warehouse.add_stock(GeneralItem(27, "Laundry Detergent", 6.50, stock=20))
    warehouse.add_stock(GeneralItem(28, "Dish Soap", 2.00, stock=35))
    warehouse.add_stock(GeneralItem(29, "Toilet Paper (4-pack)", 3.20, stock=50))
    warehouse.add_stock(GeneralItem(30, "Paper Towels", 2.50, stock=40))
    warehouse.add_stock(GeneralItem(31, "Hand Soap", 1.80, stock=25))

    return warehouse

if __name__ == "__main__":
    """
    Run this script to display the list of items in the populated warehouse.
    """
    warehouse = populate_warehouse()
    warehouse.list_items()
