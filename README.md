# Hangman

Creation of a game of hangman

## Milestone 1

I have built a word list and a simple guessing input. The input will tell you when a guess is one letter long, and displays text to say "good guess" and when it is not one letter will display "oops! That is not a valid guess."
Technologies used: python

```python
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
    
```
![](Screenshots/Capture.png)

## Milestone 2

I have used the word list and random word generator from milestone 1. For this I commented out the print functions and imported the file into milestone 2, making the word chooser a function. 

```python
from milestone_1 import word, word_list

guess = ''

def ask_for_imput(guess):
    guess = input('Enter a letter: ')

    while len(guess) != 1 or guess.isalpha() == False:
        print("Invalid letter. Please enter a single alphabetical character.")
        guess = input('Enter a letter: ')

secret_word = (word(word_list))

def check_guess(guess): 
    guess.lower()
    if guess in secret_word:
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')

ask_for_imput(guess)
```

![](Screenshots/Capture_terminal.png)


## Milestone 3

I have used the definitions created in milestone 2 as a basis for the code in the main game, creating the class hangman. To this I have added functions to initialise the attributes of the game. I created functions to populate the word to be guessed first with '_' and then, following a correct input, with the correct letter at the appropriate index. If an incorrect value is guessed, the player will lose a life and display a message stating the guess is incorrect. 

```python
import random
from re import A

class Hangman:

    def __init__(self, word_list, num_lives):
        self.num_lives = 5
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = []
        self.populate_word_guessed()
        self.num_letters = self.get_num_unique_letters()
        self.list_of_guesses = []

    def populate_word_guessed(self):
        for letters in self.word:
            self.word_guessed.append('_')
        
    def get_num_unique_letters(self):
        word_set = set({})
        letters_guessed = 0
        for letter in self.word:
            if letter in self.word_guessed and letter not in word_set:
                letters_guessed += 1
            word_set.add(letter)
        unique_letters = len(word_set)
        return unique_letters - letters_guessed

    def check_guess(self, guess): 
        guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
            self.num_letters = self.get_num_unique_letters()
            print (self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again')
            print (f'You have {self.num_lives} lives left.')
    
    def ask_for_input(self):
        guess = input('Enter a letter: ')

        while True:
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character.")
                guess = input('Enter a letter: ')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
                guess = input('Enter a letter: ')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                guess = input('Enter a letter: ')

word_list = ['pineapple', 'strawberries', 'raspberries', 'peach', 'apple']

h = Hangman(word_list, 5)

print(h.word_guessed)

h.ask_for_input()
```

![](Screenshots/Milestone_3.PNG)
