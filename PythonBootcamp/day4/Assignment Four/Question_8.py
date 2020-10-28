import math

another_calculation = ("y" or "Y")
while (another_calculation == "y") or (another_calculation == "Y"):
    import math
    first_number = float(input("Enter a number: "))
    print(f"""
    Supported Operations
    +   - Addition
    -   - Subtraction
    *   - Multiplication
    /   - Division
    mod - Modulus
    ^   - Power
    log - Logarithm
            """)
    operation = str(input("Choose an operation: "))
    second_number = float(input("Enter a number: "))
    
    if operation == "+":
        result = first_number + second_number
        print(f"{first_number} {operation} {second_number} = {result}")
    
    elif operation == "-":
        result = first_number - second_number
        print(f"{first_number} {operation} {second_number} = {result}")
    
    elif operation == "*":
        result = first_number * second_number
        print(f"{first_number} {operation} {second_number} = {result}")
    
    elif operation == "/":
        result = first_number / second_number
        print(f"{first_number} {operation} {second_number} = {result}")
    
    elif operation == "mod":
        result = first_number % second_number
        print(f"{first_number} {operation} {second_number} = {result}")
    
    elif operation == "^":
        result = first_number ** second_number
        print(f"{first_number} {operation} {second_number} = {result}")
    
    elif operation == "log":
        if second_number == False:
            result = math.log(first_number)
            print(f"{operation} {first_number} = {result}")
        elif first_number == False:
            result = math.log(second_number)
            print(f"{operation} {second_number} = {result}")
    
    the_storage = []
    for x in the_storage:
        the_storage[x] = result


    user_continuation = str(input(f"Do you still want to perform another calculation (Y/N/H): "))
    another_calculation = user_continuation

    if (user_continuation == "n") or (user_continuation == "N"):
  #      print("Thank you for using mini calculator")
        print(the_storage)
    elif (user_continuation == "h") or (user_continuation == "H"):
        for x in the_storage.items():
            print(the_storage.items(x))
    