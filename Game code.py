#Rock, paper and scissors game coding - Tanya Singh
import random
user_choice_number=int(input("Enter the number corresponding to your choice (1/2/3) :"))

#Convert number to choice
if user_choice_number == 1:
    user_choice = 'Rock'
elif user_choice_number == 2:
    user_choice = 'Paper'
elif user_choice_number == 3:
    user_choice = 'Scissors'
else:
    print("Invalid choice!")
    exit()

#Computer randomly selects a choice
choices = ['Rock','Paper','Scissors']
computer_choice = random.choice(choices)
print(f"Computer chose : {computer_choice}")

#Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
     (user_choice == 'Paper' and computer_choice == 'Rock') or \
     (user_choice == 'Scissors' and computer_choice == 'Paper'):
    print("You win! Congrats!")
else:
    print("Computer wins! Try next time!")
