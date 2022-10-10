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
            print (self.word_guessed)
            self.num_letters = self.get_num_unique_letters()
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

