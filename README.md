Self-Service Checkout System
============================

**Overview**
------------

This self-service checkout system simulates a supermarket checkout process. 

Customers can:

-   Scan or weigh items to add them to a cart
-   View their cart and total costs
-   Authorize age-restricted items with staff approval
-   Pay using card, cash, or mobile payment

The system updates inventry in realtime and handles payment retries for failed transactions.

* * * * *

**How to use**
--------------

### **1\. Starting the system**

1.  Open the terminal.

2.  Run the program with the command:

    `python3 main.py`

3.  Follow the menu prompts to perform actions such as scanning items, viewing the cart and/or checking out.

* * * * *

**Menu Options**
----------------

| Option | Description | Example |
| --- | --- | --- |
| **1** | List items for scanning (e.g. Milk, Bread). | View scannable items priced per unit and stock. |
| **2** | List items for weighing (e.g. Apples, Bananas). | View weighable items priced per kg and stock. |
| **3** | Scan an item to add it to the cart. | Enter item ID (e.g. 1 for Milk). |
| **4** | Weigh an item to add it to the cart. | Enter item ID (e.g. 11 for Apples) and weight (e.g., 2kg). |
| **5** | Display cart contents. | View items, quantities/weights, and total prices. |
| **6** | Checkout to pay and update stock. | Process payment and clear the cart. |
| **7** | Exit the program. | End the session. |

* * * * *

**Example Workflow**
--------------------

### **Step 1: List Items**

`Choose an action: 1
Available Items:
1: Milk - £1.55 each (Stock: 50 units)
2: Bread - £1.00 each (Stock: 30 units)
3: Eggs - £2.96 each (Stock: 40 units)`

### **Step 2: Scan an Item**

`Choose an action: 3
Enter item ID to scan: 1
Added Milk to the cart.`

### **Step 3: Weigh an Item**

`Choose an action: 4
Enter item ID to weigh: 11
Enter weight (in kg): 2
Added 2kg of Apples to the cart.`

### **Step 4: Display Cart**

`Choose an action: 5
Cart Items:
Milk - Qty: 1 - £1.55
Apples - Weight: 2kg - £5.00
Total: £6.55`

### **Step 5: Checkout**

`Choose an action: 6
Total amount to pay: £6.55
Select payment method: 1 (Credit/Debit Card)
Payment declined. 2 retries remaining. Please try again.
Payment of £6.55 processed successfully.
Warehouse stock updated. Checkout complete.`

* * * * *

**Payment Options**
-------------------

-   **Credit/Debit Card**: Total payment is processed.
-   **Cash**: Enter the cash amount and receive calculated change if overpaid. Part pyments are possible, and outstanding amount can be made by other methods.
-   **Mobile Payment**: Similar to card payments.

* * * * *

**Features**
------------

1.  **Item Management**:

    -   View scannable items (e.g., Bread, Milk) and weighable items (e.g., Apples, Bananas).

2.  **Cart Management**:

    -   Add scannable or weighable items to the cart.
    -   View cart contents and total cost.

3.  **Age Authorization**:

    -   Requires staff approval for items like Wine or Cigarettes.

4.  **Checkout**:

    -   Processes payments using card, cash, or mobile payment.
    -   Automatically updates stock levels.

5.  **Payment Failures**:

    -   Simulates failed payments with retries.
