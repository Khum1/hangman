# Hangman

Creation of a game of hangman

## Milestone 1

I have built a word list and a simple guessing input. The input will tell you when a guess is one letter long, and displays text to say "good guess" and when it is not one letter will display "oops! That is not a valid guess."
Technologies used: python

"""
import random

word_list = ['pineapple', 'strawberries', 'raspberries', 'peach', 'apple']

print(word_list)

word = (random.choice(word_list))

print(word)

guess = input('Enter a letter')

if len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
    
"""
![](D:/Documents/Github/hangman/Screenshots/Capture.png)

## Milestone 2

I have used the word list and random word generator from milestone 1. For this I commented out the print functions and imported the file into milestone 2, making the word chooser a function. 

"""
from milestone_1 import word, word_list

guess = ''

def ask_for_imput(guess):
    guess = input('Enter a letter: ')

    while len(guess) != 1 or guess.isalpha() == False:
        print("Invalid letter. Please enter a single alphabetical character.")
        guess = input('Enter a letter: ')

secret_word = (word(word_list))

def check_guess(guess): 
    if guess in secret_word:
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')

ask_for_imput(guess)
"""

![](D:/Documents/Github?hangman/Screenshots/Capture_terminal.png)

