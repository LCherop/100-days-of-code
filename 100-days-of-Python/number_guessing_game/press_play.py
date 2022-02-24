

#Number Guessing Game Objectives:
EASY_TURNS = 10
HARD_TURNS = 5
# Include an ASCII art logo.
from os import system
system("cls")
import random
from art import logo
print(logo)

print("Welcome to the number guessing game")
print("I'm guessing of a number between 1 and 100")

def set_level():
    level = int(input("Type 1 for the easy or 2 for the hard level "))
    if level == 1:
        print("You have 10 tries to try and guess the number")
        return EASY_TURNS
    elif level == 2:
        print("You have 5 tries to try and guess the number")
        return HARD_TURNS

number = random.randint(1,100)
turns =set_level()

guess = int(input("Please guess a number between 1 and 100 "))


def checker(num):
    global turns
    
    while not turns == 0 and num != number:
        if num < number:
            print("Too Low")
            turns -=1
            print(f"You have {turns} tries to try and guess the number")
            num = int(input("Guess again: "))
        if num > number:
            print("Too High")
            turns -=1
            print(f"You have {turns} tries to try and guess the number")
            num = int(input("Guess again: "))
    if num == number:
        print(f"You guessed right! The number is {number}")
        return 
        
    print("Whoops! You're out of tries.")
    return
   
checker(guess)
