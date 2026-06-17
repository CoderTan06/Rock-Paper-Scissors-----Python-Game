#Dice rolling simulation - TS
import random

print("Welcome to the Dice Rolling Simulator!")

while True:
  #Asking the user to roll the dice or quit
  user_input = input("Enter 'r' to roll the dice or 'q' to quit :").lower()
  
  if user_input == 'r':
    #Generate a random number between 1 and 6 to simulate a dice roll
    result = random.randint(1,6)
    print(f"You rolled a {result}!")
  elif user_input == 'q':
    #If the user presses 'q', exit the program
    print("Thanks for playing! Goodbye.")
    break
  else:
    #Print for invalid input
    print("Invalid input. Please enter 'r' to roll or 'q' to quit.")
    #End of program
