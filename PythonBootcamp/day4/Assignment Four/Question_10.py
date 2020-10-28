store_name = input("Enter the store name: ")
if len(store_name) == 0:
    print("Name must not be empty")
    exit(1)

store_address = input("Enter the store address: ")
if len(store_address) == 0:
    print("Address must not be empty")
    exit(1)

no_of_items = int(input("How many items are in your inventory: "))
if no_of_items < 0:
    print("Number of items must be greater than or equal to 0")
    exit(1)

header = f"""Store:
    name: {store_name}
    address: {store_address}"""

inventory_body = header

serial_number = 1

if no_of_items >= 1:
    inventory_body += "\n    Items:"

while no_of_items >= serial_number:
    item_name = input(f"Enter the name of item {serial_number}: ")
    if len(item_name) == 0:
        print("Item name must not be empty")
        exit(1)
    item_sku = input(f"Enter the SKU of item {serial_number}: ")
    if len(item_sku) == 0:
        print("Item SKU must not be empty")
        exit(1)
    item_quantity = int(input(f"Enter the quantity of item {serial_number} in stock: "))
    if item_quantity < 0:
        print("Quantity must be greater than or equal to 0")
        exit(1)
    item_price = float(input(f"Enter the price of item {serial_number}: "))
    if item_price <= 0:
        print("Item price must be greater than 0")
        exit(1)
    item_body = f"""
        Item{serial_number}:
            Name: {item_name}
            SKU: {item_sku}
            Quantity: {item_quantity}
            Price: {item_price:.2f}"""
    
    if serial_number > 1:
        item_sku = []
        while range(1, serial_number):
            x = item_sku()
            item_sku.append(x)
            
        for item in item_sku:
                print(item)
    
    inventory_body += item_body
    serial_number += 1

print(inventory_body)