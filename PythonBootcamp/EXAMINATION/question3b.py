user_win = 0
computer_win = 0

while user_win < 3 or computer_win < 3:
    user_number = int(input("Scissors(0), Rock(1), Paper(2): "))
    user = ["Scissors", "Rock", "Paper"]
    user_choice = user[user_number]

    import random

    computer = ["Scissors", "Rock", "Paper"]
    computer_number = random.randint(0,2)
    computer_choice = computer[computer_number]

    
    if computer_number == (user_number + 1) % 3:
        computer_win = computer_win + 1
        print (f"The computer is {computer_choice}, You are {user_choice}. You Lose!")

    elif user_number == (computer_number + 1) % 3:
        user_win = user_win + 1
        print (f"The computer is {computer_choice}, You are {user_choice}. You Win!")

    else:
        print (f"The computer is {computer_choice}, You are {user_choice}. Its a draw!")    

    if user_win > 2:
        print("The game ends. You win.")
        break
    elif computer_win > 2:
        print("The game ends. You lose.")
        break


    