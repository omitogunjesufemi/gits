max_number = 0
count = 0
a = 0
while a <= 7:
    number = int(input("Enter a number (0; for end of input): "))
    count = 1
    if number > max_number:
        max_number = number
        count = 1
    
    a = a + 1
    numbers = []
    while a > 0:
        x = numbers()
        numbers.append(x)
            
        for num in numbers:
            print(num)
