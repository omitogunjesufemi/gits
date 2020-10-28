user = ("scissors", "rock", "paper")
user_input = " "
user_win = 0
computer_win = 0
while (user_input == " ") and (user_win < 3) and (computer_win < 3):
    
    from random import randint
    computer = ("scissors", "rock", "paper")
    computer_choice = computer[randint(0,2)]
    
    user_input = int(input("scissor (0), rock (1), paper (2) :"))
    if ((user_input > 2) or (user_input < 0)):
        print("Invalid Input")
        break
    
                 
    user_choice = user[user_input]
    
    if user_choice == computer_choice:    
        print(f"The computer is {computer_choice}. You are {user_choice} too. It is a draw")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            user_win = user_win + 1
            print(f"The computer is {computer_choice}. You are {user_choice}. You win")
            
        else:
            computer_win = computer_win + 1
            print(f"The computer is {computer_choice}. You are {user_choice}. You Lose")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            user_win = user_win + 1
            print(f"The computer is {computer_choice}. You are {user_choice}. You win")
            
        else:
            computer_win = computer_win + 1
            print(f"The computer is {computer_choice}. You are {user_choice}. You Lose")
    elif user_choice == "paper":
        if computer_choice == "rock":
            user_win = user_win + 1
            print(f"The computer is {computer_choice}. You are {user_choice}. You win")
            
        else:
            computer_win = computer_win + 1
            print(f"The computer is {computer_choice}. You are {user_choice}. You Lose")


    if user_win > 2:
        print("The Game Ends, You Win!")

    if computer_win > 2:
        print("The Game Ends, You Lose!")

    user_input = " "

    computer_win = computer_win + 0
    user_win = user_win + 0
