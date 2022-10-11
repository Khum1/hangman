import random
from re import A

class Hangman:

    def __init__(self, word_list, num_lives):
        self.num_lives = num_lives
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
            self.display_image()
    
    def ask_for_input(self):
        guess = input('Enter a letter: ')

        while True:
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character.")
                break
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
                break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    def display_image(self):
        for item in hangman_image:
            for number in item:
                if number == 0:
                    print(' ', end='')
                elif number == 1 and self.num_lives <= 3:
                    print('O', end='')
                elif number == 2 and self.num_lives <= 2:
                    print('|', end='') 
                elif number == 3 and self.num_lives <= 1:
                    print('\\', end='')
                elif number == 4 and self.num_lives <= 0:
                    print('/', end='')
                elif number == 4 and self.num_lives > 0: # formatting 
                    print(' ', end='')
                elif number == 9 and self.num_lives <= 4:
                    print('_', end='')
                elif number == 8 and self.num_lives <= 4:
                    print('|', end='')
            print('')

    

def play_game():
    word_list = ['pineapple', 'strawberries', 'raspberries', 'peach', 'apple']
    game = Hangman(word_list, 5)
    print(game.word_guessed)
    while True:
        if game.num_lives > 0 and game.num_letters != 0:
            game.ask_for_input()
        elif game.num_lives == 0:
            print("You lose!")
            break
        else:
            print("Congrats, you won the game!")
            break


hangman_image = [
  [9,9,9,9,9],
  [8,0,0,1,0],
  [8,0,4,2,3],
  [8,0,4,0,3],
  [9,9,9,9,9]
    ]
    

play_game()
