def main():
    integar_input = input("Enter any integar: ")
    length = len(integar_input)
    sum_of_integars(integar_input, length)

def sum_of_integars(integar_inputs, lengths):
    integars = int(integar_inputs)
    store_digit = []
    zero = int(0)

    while lengths > 1:
        digit = integars % 10
        extracted = integars // 10
        store_digit.append(digit)
        sumofDigit = digit + zero
        zero = sumofDigit
        
        integars = extracted
        newInt = str(integars)
        lengths = len(newInt)
        
        if lengths == 1:
            store_digit.append(integars)
            result = sumofDigit + integars

    print(store_digit)
    print(result)

main()
    
