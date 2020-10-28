# Sum of digits in an integar
integer = int(input("Enter a number between 0 and 1000: "))
if integer in range(0, 1000):
    digit3 = integer % 10
    num3 = integer // 10
    digit2 = num3 % 10
    num2 = num3 // 10
    digit1 = num2 % 10
    num1 = num2 // 10
    addition = digit1 + digit2 + digit3
    print ("The sum of the digits is " +str(addition))
else:
    print ("Invalid number")