# Store Inventory
name = str(input("Enter the store name: ").strip())

if len(name) != 0:
    address = str(input("Enter the store address: ").strip())
else:
    print("Invalid Input")
    exit(1)

if len(address) != 0:
    item_number = int(input("Enter the number of items you have: ").strip())
else:
    print("Invalid Input")
    exit(1)

# For Just One Quantity
if (item_number >= 0) and (item_number <= 1):
    
    item1_name = str(input("Enter the name of the First item: ").strip())
    
    if len(item1_name) != 0:
        item1_sku = input("Enter the SKU of the First item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item1_sku) != 0:
        item1_quantity = int(input("Enter the quantity of the First item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item1_quantity >= 0):
        item1_price = float(input("Enter the price of the First item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item1_price > 0):
        
        print(f"""Store:
        name: {name}
        address: {address}
        Items:
            Item1:
                Name: {item1_name}
                SKU: {item1_sku}
                Quantity: {item1_quantity}
                Price: {item1_price} """)
        exit(0)
    else:
        print("Invalid input")
        exit(1)

# For Two Quantities
if (item_number >= 0) and (item_number <= 2):        
    
    item1_name = str(input("Enter the name of the First item: ").strip())
    
    if len(item1_name) != 0:
        item1_sku = input("Enter the SKU of the First item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item1_sku) != 0:
        item1_quantity = int(input("Enter the quantity of the First item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item1_quantity >= 0):
        item1_price = float(input("Enter the price of the First item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item1_price > 0):
        
     item2_name = str(input("Enter the name of the Second item: ").strip())
    
    if len(item2_name) != 0:
        item2_sku = input("Enter the SKU of the Second item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item2_sku) != 0:
        item2_quantity = int(input("Enter the quantity of the Second item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item2_quantity >= 0):
        item2_price = float(input("Enter the price of the Second item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item2_price > 0):
        
        print(f"""Store:
        name: {name}
        address: {address}
        Items:
            Item1:
                Name: {item1_name}
                SKU: {item1_sku}
                Quantity: {item1_quantity}
                Price: {item1_price}
            
            Item2:
                Name: {item2_name}
                SKU: {item2_sku}
                Quantity: {item2_quantity}
                Price: {item2_price}   """)
        exit(0)
    else:
        print("Invalid input")
        exit(1)
       

#For Three Quantities 
if (item_number >= 0) and (item_number <= 3):     
    
    item1_name = str(input("Enter the name of the First item: ").strip())
    
    if len(item1_name) != 0:
        item1_sku = input("Enter the SKU of the First item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item1_sku) != 0:
        item1_quantity = int(input("Enter the quantity of the First item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item1_quantity >= 0):
        item1_price = float(input("Enter the price of the First item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item1_price > 0):
        
     item2_name = str(input("Enter the name of the Second item: ").strip())
    
    if len(item2_name) != 0:
        item2_sku = input("Enter the SKU of the Second item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item2_sku) != 0:
        item2_quantity = int(input("Enter the quantity of the Second item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item2_quantity >= 0):
        item2_price = float(input("Enter the price of the Second item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item2_price > 0):
        
        item3_name = str(input("Enter the name of the Third item: ").strip())
    
    if len(item3_name) != 0:
        item3_sku = input("Enter the SKU of the Third item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item3_sku) != 0:
        item3_quantity = int(input("Enter the quantity of the Third item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item3_quantity >= 0):
        item3_price = float(input("Enter the price of the Third item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item3_price > 0):

        print(f"""Store:
        name: {name}
        address: {address}
        Items:
            Item1:
                Name: {item1_name}
                SKU: {item1_sku}
                Quantity: {item1_quantity}
                Price: {item1_price}
            
            Item2:
                Name: {item2_name}
                SKU: {item2_sku}
                Quantity: {item2_quantity}
                Price: {item2_price} 
            
            Item3:
            Name: {item3_name}
            SKU: {item3_sku}
            Quantity: {item3_quantity}
            Price: {item3_price}         """)
        exit(0)
    else:
        print("Invalid input")
        exit(1)
       
# For Four Quantities
if (item_number >= 0) and (item_number <= 4):   
    
    item1_name = str(input("Enter the name of the First item: ").strip())
    
    if len(item1_name) != 0:
        item1_sku = input("Enter the SKU of the First item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item1_sku) != 0:
        item1_quantity = int(input("Enter the quantity of the First item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item1_quantity >= 0):
        item1_price = float(input("Enter the price of the First item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item1_price > 0):
        
     item2_name = str(input("Enter the name of the Second item: ").strip())
    
    if len(item2_name) != 0:
        item2_sku = input("Enter the SKU of the Second item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item2_sku) != 0:
        item2_quantity = int(input("Enter the quantity of the Second item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item2_quantity >= 0):
        item2_price = float(input("Enter the price of the Second item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item2_price > 0):
        
        item3_name = str(input("Enter the name of the Third item: ").strip())
    
    if len(item3_name) != 0:
        item3_sku = input("Enter the SKU of the Third item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item3_sku) != 0:
        item3_quantity = int(input("Enter the quantity of the Third item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item3_quantity >= 0):
        item3_price = float(input("Enter the price of the Third item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item3_price > 0):

        item4_name = str(input("Enter the name of the Fourth item: ").strip())
    
    if len(item4_name) != 0:
        item4_sku = input("Enter the SKU of the Fourth item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item4_sku) != 0:
        item4_quantity = int(input("Enter the quantity of the Fourth item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item4_quantity >= 0):
        item4_price = float(input("Enter the price of the Fourth item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item4_price > 0):

        print(f"""Store:
        name: {name}
        address: {address}
        Items:
            Item1:
                Name: {item1_name}
                SKU: {item1_sku}
                Quantity: {item1_quantity}
                Price: {item1_price}
            
            Item2:
                Name: {item2_name}
                SKU: {item2_sku}
                Quantity: {item2_quantity}
                Price: {item2_price} 
            
            Item3:
                Name: {item3_name}
                SKU: {item3_sku}
                Quantity: {item3_quantity}
                Price: {item3_price}        
            
            Item4:
                Name: {item4_name}
                SKU: {item4_sku}
                Quantity: {item4_quantity}
                Price: {item4_price}  """)

        exit(0)
    else:
        print("Invalid input")
        exit(1)
       
# For Five Quantities
if (item_number >= 0) and (item_number <= 5):   
    item1_name = str(input("Enter the name of the First item: ").strip())
    
    if len(item1_name) != 0:
        item1_sku = input("Enter the SKU of the First item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item1_sku) != 0:
        item1_quantity = int(input("Enter the quantity of the First item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item1_quantity >= 0):
        item1_price = float(input("Enter the price of the First item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item1_price > 0):
        
     item2_name = str(input("Enter the name of the Second item: ").strip())
    
    if len(item2_name) != 0:
        item2_sku = input("Enter the SKU of the Second item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item2_sku) != 0:
        item2_quantity = int(input("Enter the quantity of the Second item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item2_quantity >= 0):
        item2_price = float(input("Enter the price of the Second item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item2_price > 0):
        
        item3_name = str(input("Enter the name of the Third item: ").strip())
    
    if len(item3_name) != 0:
        item3_sku = input("Enter the SKU of the Third item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item3_sku) != 0:
        item3_quantity = int(input("Enter the quantity of the Third item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item3_quantity >= 0):
        item3_price = float(input("Enter the price of the Third item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item3_price > 0):

        item4_name = str(input("Enter the name of the Fourth item: ").strip())
    
    if len(item4_name) != 0:
        item4_sku = input("Enter the SKU of the Fourth item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item4_sku) != 0:
        item4_quantity = int(input("Enter the quantity of the Fourth item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item4_quantity >= 0):
        item4_price = float(input("Enter the price of the Fourth item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item4_price > 0):

        item5_name = str(input("Enter the name of the Fifth item: ").strip())
    
    if len(item5_name) != 0:
        item5_sku = input("Enter the SKU of the Fifth item: ").strip()
    else:
        print("Invalid Input")
        exit(1)
    
    if len(item5_sku) != 0:
        item5_quantity = int(input("Enter the quantity of the Fifth item in stock: ").strip())
    else:
        print("Invalid Input")
        exit(1)
    
    if (item5_quantity >= 0):
        item5_price = float(input("Enter the price of the Fifth item: "))
    else:
        print("Invalid Input")
        exit(1)
    
    if (item5_price > 0):

        print(f"""Store:
        name: {name}
        address: {address}
        Items:
            Item1:
                Name: {item1_name}
                SKU: {item1_sku}
                Quantity: {item1_quantity}
                Price: {item1_price}
            
            Item2:
                Name: {item2_name}
                SKU: {item2_sku}
                Quantity: {item2_quantity}
                Price: {item2_price} 
            
            Item3:
                Name: {item3_name}
                SKU: {item3_sku}
                Quantity: {item3_quantity}
                Price: {item3_price}        
            
            Item4:
                Name: {item4_name}
                SKU: {item4_sku}
                Quantity: {item4_quantity}
                Price: {item4_price}  
            Item5:
                Name: {item5_name}
                SKU: {item5_sku}
                Quantity: {item5_quantity}
                Price: {item5_price}   """)
        exit(0)
    else:
        print("Invalid input")
        exit(1)
        