#Guessing secret number program- the user can play guess(x) if they want to guess a number the computer picks or they can play computer_guess(x) if they want the computer to guess a number that the user picks.

import random

def guess(x):
    random_number = random.randint(1,x) #giving computer a random number
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again, your guess was too low.")
        elif guess > random_number:
            print("Sorry, guess again, your guess was too high.")

    print(f"Yay! Congrats, you have guessed the number {random_number} correctly.")

#computer guessing user's number. User has to pick a number in their head, and based off that number, indicate if the computer's guess is too high, too low, or correct. The computer will keep guessing until it gets the number right, not guessing the same incorrect number more than once
def computer_guess(x): #x is the range from 0 to x of the user's guess
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low == guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly!")

guess(100)
