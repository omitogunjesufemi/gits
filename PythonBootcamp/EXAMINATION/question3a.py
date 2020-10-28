import random

computer = ["Scissors", "Rock", "Paper"]
computer_number = random.randint(0,2)
computer_choice = computer[computer_number]

user_number = int(input("Scissors(0), Rock(1), Paper(2): "))
user = ["Scissors", "Rock", "Paper"]
user_choice = user[user_number]

if computer_number == (user_number + 1) % 3:
    print (f"The computer is {computer_choice}, You are {user_choice}. You Lose!")

elif user_number == (computer_number + 1) % 3:
    print (f"The computer is {computer_choice}, You are {user_choice}. You Win!")

else:
    print (f"The computer is {computer_choice}, You are {user_choice}. Its a draw!")    




