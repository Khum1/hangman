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
