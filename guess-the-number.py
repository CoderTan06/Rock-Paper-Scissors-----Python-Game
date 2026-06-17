#Guess the number program (1-100) - TS
import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:
        print("Correct! You guessed it!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
#End of program
