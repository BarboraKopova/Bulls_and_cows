"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Barbora Kopová
email: barbarakopova20@seznam.cz
"""

import random
import time
import sys


def generate_secret_number() -> str:
    """
    Generates a 4-digit secret number with unique digits.
    The first digit is not allowed to be zero.
    """
    digits = list("123456789")
    first_digit = random.choice(digits)
    digits.remove(first_digit)
    remaining_digits = random.sample([d for d in "0123456789" if d != first_digit], 3)
    return first_digit + "".join(remaining_digits)


def is_valid_guess(guess: str) -> bool:
    """
    Checks whether the user's input is a valid 4-digit number:
    - must be digits only
    - must be 4 characters long
    - must not start with zero
    - must not contain repeated digits
    """
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


def count_bulls_and_cows(secret: str, guess: str) -> tuple[int, int]:
    """
    Compares the guess with the secret number.
    Returns:
    - bulls: correct digits in correct position
    - cows: correct digits in wrong position
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows


def print_intro() -> None:
    """
    Prints the introduction and instructions for the game.
    """
    print("Hi there!")
    print("-" * 50)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 50)


def play_game() -> None:
    """
    Main game loop where the user tries to guess the number.
    """
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
            break
        else:
            bull_word = "bull" if bulls == 1 else "bulls"
            cow_word = "cow" if cows == 1 else "cows"
            print(f"{bulls} {bull_word}, {cows} {cow_word}")


if __name__ == "__main__":
    print_intro()
    play_game()
