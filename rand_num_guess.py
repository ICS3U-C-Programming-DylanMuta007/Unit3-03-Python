#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : March 2025
# This program makes the use guess randomly generated number 0 - 9
import random


def main():
    # creates a variable random_numb which creates a random number from 0 - 9
    random_numb = random.randint(0, 9)

    # asks the user to guess a number between 1 and 10
    user_guess = int(input("Guess a number between 0 and 9 : "))

    # checks if user guess is the same as the random number generated
    if user_guess == random_numb:
        print("good guess!!!")
    # if the user guess is not the same it prints
    else:
        print("sorry wrong guess the real number was {}".format(random_numb))


if __name__ == "__main__":
    main()  # runs the program
