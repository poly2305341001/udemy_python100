#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from d012_module import logo

print(logo)

def playgame():
    level = int(input("Which level will you play? (0 ~ 9)"))
    chances = 20 - level*2
    print(f"You start with {chances} chances")

    number = random.randint(1, 100)

    while 1:
        guessing = int(input("Guess the number between 1 and 100:) \n "))
        if guessing == number:
            print(f"You are right! The number was {number}.")
            break
        elif guessing > number:
            print("Down")
        else:
            print("Up")
        chances -= 1
        if chances == 1:
            print("You lose a chance. Now you have the LAST chance.")
        elif chances == 0:
            print("GAME OVER")
            break
        else:
            print(f"You lose a chance. Now you have {chances} chances.")

    print(f"The number was {number}.")
    again = input("Would you try again?(y/n) ")
    if again == 'y':
        playgame()
    
playgame()