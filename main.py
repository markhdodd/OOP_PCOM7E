from models.cart import Cart
from test_data import populate_warehouse

# Initialize warehouse
warehouse = populate_warehouse()

# Initialize customer cart
cart = Cart()

# Predefined staff authorization code
STAFF_AUTHORIZATION_CODE = "1234"

# Menu for user actions
def display_menu():
    print("\nChoose an action:")
    print("1: List items for scanning")
    print("2: List items for weighing")
    print("3: Scan an item")
    print("4: Weigh an item")
    print("5: Display cart")
    print("6: Checkout")
    print("7: Exit")

# Function to list items based on their type
def list_items(warehouse, requires_weighing):

    print("Available Items:")

    for item in warehouse.inventory.values():
        if hasattr(item, "requires_weighing") and item.requires_weighing == requires_weighing:
            unit = "per kg" if requires_weighing else "each"
            stock_unit = "kg" if requires_weighing else "units"
            print(f"{item.item_id}: {item.name} - £{item.price:.2f} {unit} (Stock: {item.stock} {stock_unit})")

# Function to authorize age-restricted items
def authorize_age_restricted_items(cart):

    for item_id, (item, _, _) in list(cart.items.items()):  # Use a copy of items for safe removal

        if hasattr(item, "age_limit") and item.age_limit > 0:
            code = input(f"Staff authorization required for {item.name}. Enter code: ")

            if code == STAFF_AUTHORIZATION_CODE:
                print(f"Authorization successful for {item.name}.")
            else:
                print(f"Authorization failed for {item.name}. Item removed from the cart.")
                cart.remove_item(item_id)

# Function to handle payment at checkout
def process_payment(total):
    print("\nSelect a payment method:")
    print("1: Credit/Debit Card")
    print("2: Cash")
    print("3: Mobile Payment (e.g., Apple Pay, Google Pay)")

    while True:
        try:
            payment_method = int(input("Enter the number corresponding to yor payment method: "))
            if payment_method == 1:
                print(f"Payment of £{total:.2f} processed successfully via Credit/Debit Card.")
                return True
            elif payment_method == 2:
                cash = float(input(f"Enter cash amount: £"))
                if cash >= total:
                    change = cash - total
                    print(f"Payment of £{total:.2f} accepted. Change: £{change:.2f}")
                    return True
                else:
                    print(f"Insufficient cash. You need £{total - cash:.2f} more.")
            
            elif payment_method == 3:
                print(f"Payment of £{total:.2f} processed successfully via Mobile Payment.")
                return True
            
            else:
                print("Invalid option. Please select a valid payment method.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to update warehouse stock after checkout

def update_warehouse_stock(cart, warehouse):
    for item_id, (item, quantity_or_weight, _) in cart.items.items():
        warehouse.deduct_stock(item_id, quantity_or_weight)
    print("Warehouse stock updated.")

# Simulate actions

while True:
    display_menu()
    try:
        action = int(input("Enter the number corresponding to your action: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        continue

    if action == 1:  # List items for scanning
        list_items(warehouse, requires_weighing=False)

    elif action == 2:  # List items for weighing
        list_items(warehouse, requires_weighing=True)

    elif action == 3:  # Scan an item
        try:
            item_id = int(input("Enter item ID to scan: "))
            if item_id in warehouse.inventory:
                item = warehouse.inventory[item_id]
                if not getattr(item, "requires_weighing", False):
                    cart.add_item(item)
                    print(f"Added {item.name} to the cart.")
                else:
                    print(f"{item.name} must be weighed instead of scanned.")
            else:
                print("Invalid item ID.")
        except ValueError:
            print("Invalid input. Please enter a valid item ID.")
        cart.display_cart()  # Display cart after addition

    elif action == 4:  # Weigh an item
        try:
            item_id = int(input("Enter item ID to weigh: "))
            if item_id in warehouse.inventory:
                item = warehouse.inventory[item_id]
                if getattr(item, "requires_weighing", False):
                    weight = float(input("Enter weight (in kg): "))
                    cart.add_item(item, weight)
                    print(f"Added {weight}kg of {item.name} to the cart.")
                else:
                    print(f"{item.name} does not require weighing.")
            else:
                print("Invalid item ID.")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

        cart.display_cart()  # Display cart after addition

    elif action == 5:  # Display cart
        cart.display_cart()

    elif action == 6:  # Checkout
        if not cart.items:
            print("Your cart is empty. Add items before proceeding to checkout.")
            continue

        total = cart.calculate_total()
        print(f"Total amount to pay: £{total:.2f}")
        authorize_age_restricted_items(cart)  # Authorize age-restricted items

        if process_payment(total):
            update_warehouse_stock(cart, warehouse)  # Update stock after successful payment
            cart.items.clear()  # Empty the cart after checkout
            print("Checkout complete. You can continue shopping.")

    elif action == 7:  # Exit

        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid action. Please select a number between 1 and 7.")
