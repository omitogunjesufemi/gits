def main():
    max_number = int(input("Enter a number (0: for the end of input): "))
    count = 0
    user_input = ""
    while user_input != 0:
        user_input = int(input("Enter a number (0: for the end of input): "))
        if user_input == max_number:
            count = count + 1
        elif user_input > max_number:
            max_number = user_input
            count = 1
    
    print(f"""
The largest number is {max_number}
The occurence count of the largest number is {count}
    
    """)
    
main()