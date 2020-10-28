# Addition Quiz
import random
number1 = random.randint(0,9)
number2 = random.randint(0,9)
number3 = random.randint(0,9)
answer = int(input(f"What is {number1} + {number2} + {number3}: "))
print(f"{number1} + {number2} + {number3} = {answer} is {number1 + number2 + number3 == answer} ")
if answer == number1 + number2 + number3:
    print("Good job!")
else:
    print("Boo!")