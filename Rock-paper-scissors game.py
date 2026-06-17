#Rock, paper, pencil and scissors game coding - TS
import random
user_choice_number=int(input("Enter the number corresponding to your choice (1/2/3/4) :"))

#Convert number to choice
if user_choice_number == 1:
    user_choice = 'Rock'
elif user_choice_number == 2:
    user_choice = 'Paper'
elif user_choice_number == 3:
    user_choice = 'Pencil'
elif user_choice_number == 4:
    user_choice = 'Scissors'
else:
    print("Invalid choice!")
    exit()

#Computer randomly selects a choice
choices = ['Rock','Paper','Pencil','Scissors']
computer_choice = random.choice(choices)
print(f"Computer chose : {computer_choice}")

#Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user == "rock" and computer in ["scissors", "pencil"]) or \
     (user == "paper" and computer in ["rock", "pencil"]) or \
     (user == "pencil" and computer == "paper") or \
     (user == "scissors" and computer in ["paper", "pencil"]):
    print("You win! Congrats!")
else:
    print("Computer wins! Try next time!")
#End of program
