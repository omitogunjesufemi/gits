user = ("scissors", "rock", "paper")
user_input = " "

while user_input == " ":
    from random import randint

    computer = ("scissors", "rock", "paper")
    computer_choice = computer[randint(0,2)]
    user_input = int(input("scissor (0), rock (1), paper (2) :"))
    if ((user_input > 2) or (user_input < 0)):
        print("Invalid Input")
        break
    
                 
    user_choice = user[user_input]
    user_win = 0
    if user_choice == computer_choice:
        print(f"The computer is {computer_choice}. You are {user_choice} too. It is a draw")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print(f"The computer is {computer_choice}. You are {user_choice}. You win")
            
        else:
            print(f"The computer is {computer_choice}. You are {user_choice}. You Lose")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print(f"The computer is {computer_choice}. You are {user_choice}. You win")
            
        else:
            print(f"The computer is {computer_choice}. You are {user_choice}. You Lose")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print(f"The computer is {computer_choice}. You are {user_choice}. You win")
            
        else:
            print(f"The computer is {computer_choice}. You are {user_choice}. You Lose")
    
    user_input = " "