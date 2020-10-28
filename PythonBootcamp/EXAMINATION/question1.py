def reverse(number):
    for x in reversed(number):
        print(x, end="")

def main():
    integar = str(input("Enter an integar: "))
    reverse(integar)

main()