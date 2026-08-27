# Product inventory system for a small store

# Dictionary of products
inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "notebook": {"price": 4.99, "quantity": 80},
    "printer": {"price": 125.79, "quantity": 10},
    "monitor": {"price": 89.99, "quantity": 24}
}

# Display inventory, look up/update a product, and check low stock
def display_inventory():
    print("=" * 40)
    print("Store Inventory".center(40))
    print("=" * 40)

    print(f"\n{'Product':<15} {'Price':<15} {'QTY'}")
    print("-" * 40)
    if not inventory:
        print("No inventory yet.")
        return

    for key, info in inventory.items():
        print(f"{key:<15} ${info['price']:<15.2f} {info['quantity']}")

    print(f"\nTotal Type of Products in Inventory: {len(inventory)}")
    print("*" * 40)

    print(f"\n{'Product':<15} {'Inventory Value per Product'}")
    print("-" * 40)
    inventory_value = 0
    for key, info in inventory.items():
        product_value = info['price'] * info['quantity']
        inventory_value = inventory_value + product_value
        print(f"{key:<15} ${product_value:.2f}")
    print(f"\n* Store Inventory Total Value: ${inventory_value:,.2f} *")

    # Look up a specific product
    search = input("\nLook up a product (enter product): ").lower()
    product = inventory.get(search)

    if product:
        print(f"\nIn Inventory: \nProduct: {search.title()}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Qty: {product['quantity']}")
    
        # Update the quantity of a product
        print(f"\nUpdate Product ({search.title()}) Quantity")
        print("Would you like to update by SALE(1) or RESTOCK(2)")
    
        try:
            choice = int(input("\nChoice: "))
            if choice == 1:
                qty_sold = int(input(f"How many were sold: "))
                if qty_sold > product['quantity']:
                    print(f"Not enough stock. Only {product['quantity']} {search} available.")
                else:
                    new_qty = product['quantity'] - qty_sold
                    product['quantity'] = new_qty
                    print(f"Updated {search} quantity: {product['quantity']}")
            elif choice == 2:
                qty_restock = int(input(f"How many are being restocked: "))
                new_qty = product['quantity'] + qty_restock
                product['quantity'] = new_qty
                print(f"Updated {search} quantity: {product['quantity']}")
            else:
                print("No changes made")
        except (ValueError, IndexError):
            print("Enter a valid number")
    else:
        print(f"No product found for '{search}'.")
    # Track low-stock products
    low_stock = set()
    for key, info in inventory.items():
        if info['quantity'] < 10:
            low_stock.add(key)
    print(f"\nProducts in Low Stock:")
    if low_stock:
        for item in low_stock:
            print(f" {item.title()} ({inventory[item]['quantity']} in stock)")
    else:
        print("All products are well stocked")
display_inventory()