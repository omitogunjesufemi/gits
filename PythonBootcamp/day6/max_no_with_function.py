def max_of_two(num1, num2):
    if num1 > num2 :
        return num1
    else:
        return num2
def max_of_three(num1, num2, num3):
    return max_of_two(num1, max_of_two(num2, num3))
    

def main():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))
    max_of_three(number1, number2, number3)
    print(f"The maximum number is {max_of_three(number1, number2, number3)}")
        
main()