import random

while True:
    User_choice = input("Enter your choice from \n rock\n paper\n scissor \n")
    choice = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choice)
    print(f"You chose {User_choice} and computer chose {computer_choice}")

    if User_choice == computer_choice:
        print(f"Both players selected {User_choice}, so it's a tie!")
    elif User_choice == "rock":
        if computer_choice == "paper":
            print("Paper wraps rock, computer wins!!")
        else:
            print("Rock smashes scissors, you win!!")   
    elif User_choice == "paper":
        if computer_choice == "rock":
            print("Paper wraps rock, you win!!")
        else:
            print("Scissors cut paper, computer wins!!")
    elif User_choice == "scissor":
        if computer_choice == "rock":
            print("Rock smashes scissors, computer wins!!")
        else:
            print("Scissors cut paper, you win!!")      
    else:
        print("Invalid choice, please choose rock, paper, or scissor.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("bye bye")
