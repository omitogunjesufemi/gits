def factorial_of_number(number):
    total = 1
    for x in range(1, number+1):
        total = total * x
    print (total)

def main():
    num = int(input("Please enter the number for the factorial: "))
    factorial_of_number(num)

main()
