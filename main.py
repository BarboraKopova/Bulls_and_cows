"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Barbora Kopová
email: barbarakopova20@seznam.cz
"""

import random
import time
import sys

#Function for generating secret number
def generate_secret_number():
    digits = list("123456789")
    first_digit = random.choice(digits)
    digits.remove(first_digit)
    remaining_digits = random.sample([d for d in "0123456789" if d != first_digit], 3)
    return first_digit + "".join(remaining_digits)

#Function for validating guessed number
def is_valid_guess(guess):
    if not guess.isdigit():
        print("Please enter only digits.")
        return False
    if len(guess) != 4:
        print("The number must be exactly 4 digits long.")
        return False
    if guess[0] == "0":
        print("The number must not start with 0.")
        return False
    if len(set(guess)) != 4:
        print("Digits must be unique.")
        return False
    return True

# Function for returning count of bulls and cows
def count_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

# Main programme
print("Hi there!")
print("-" * 50)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-" * 50)

secret_number = generate_secret_number()
attempts = 0
start_time = time.time()

while True:
    guess = input("Enter a number:\n>>> ").strip()
    print("-" * 50)

    if not is_valid_guess(guess):
        continue

    attempts += 1
    bulls, cows = count_bulls_and_cows(secret_number, guess)

    if bulls == 4:
        duration = round(time.time() - start_time)
        print(f"Correct, you've guessed the right number {secret_number} in {attempts} guesses and {duration} seconds.")
        print("-" * 50)
        print("That's amazing!")
        sys.exit()
    else:
        bull_word = "bull" if bulls == 1 else "bulls"
        cow_word = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull_word}, {cows} {cow_word}")


