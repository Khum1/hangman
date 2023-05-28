import random
from user_interface import UserInterface
from time import time


class Hangman:

    '''
    A class to start a game of Hangman
    ... 
    Attributes
    ----------
    word_list : list
        list of the possible words to guess
    word : str
        random word chosen from the word_list
    word_board : list
        representation of the word to be guessed with '_' to be replaced with the correct letters guessed
    num_letters: int
        number of unique letters in the word that have not been guessed yet
    list_of_guesses : list
        list of guesses that have already been tried

    Methods
    -------
    get_unique_letters():
        gets the number of unique letters to be guessed
    successful_guess(guess):
        on a successful guess, fills in the word_board with the correct letter in the correct place.
    unsuccessful_guess(guess):
        on an unsuccessful guess, removes a life and displays number of lives left and hangman image.
    check_guess(guess):
        checks whether the letter guessed is in the word chosen
    ask_for_input():
        asks the player for a letter to be guessed
    display_image():
        displays the image of the evolving hangman with each wrong guess

    '''

    def __init__(self, word_list):
        '''
        Constructs the necessary attributes for the Hangman object.

        Parameters
        ----------
        word_list : list
            list of the possible words to guess
        word : str
            random word chosen from the word_list
        word_board : list
            representation of the word to be guessed with '_' to be replaced with the correct letters guessed
        num_letters: int
            number of unique letters in the word that have not been guessed yet
        list_of_guesses : list
            list of guesses that have already been tried
        '''
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_board = self.word_board = len(self.word)*["_"]
        self.num_letters = self.get_num_unique_letters()
        self.list_of_guesses = []
        self.ui = UserInterface()
        self.start_time = time()

    def __check_letter_in_board(self, letter, unique_letters_set):
        '''
        Checks if the letter given is in the game_board or unique_letters_set.

        Parameters
        ----------
        letter : str
            guessed by the player
        unique_letters_set : set 
            a set listing all of the letters that have been guessed by the player

        Returns
        -------
        None


        '''
        if letter in self.word_board and letter not in unique_letters_set:
            self.letters_guessed += 1

    
    def process_input(self, guess):
        '''
        Converts the guess to lower case and checks it is a valid guess using the __check_valid_guess() method

        Parameters
        ----------
        guess : str
            input from the player to guess a letter in the word
        
        Returns
        -------
        guess
            input from the player to guess a letter in the word converted to a lower case letter

        '''
        guess = guess.lower()
        while True:
            message = self.__check_valid_guess(guess)
            print(message)
            return guess
    
    def __check_valid_guess(self, guess):
        '''
        Checks that the guess is a single letter of the alphabet

        Parameters
        ----------
        guess : str
            input from the player to guess a letter in the word

        Returns
        -------
        None
        '''
        if len(guess) != 1 or guess.isalpha() == False:
            message = "Invalid letter. Please enter a single alphabetical character."
        elif guess in self.list_of_guesses:
            message = "You already tried that letter!"
        else:
            message = "Thats a valid letter"
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
        return message

    def get_num_unique_letters(self):
        '''
        Gets the number of unique letters to be guessed.

        Parameters
        ----------
        None

        Returns
        -------
        len(unique_letters_set) - self.letters_guessed : int
            the number of the unique letters in the word - the number of correct letters guessed

        '''
        unique_letters_set = set()
        self.letters_guessed = 0
        for letter in self.word: 
            self.__check_letter_in_board(letter, unique_letters_set)
            unique_letters_set.add(letter)
        self.num_letters = int(len(unique_letters_set) - self.letters_guessed)
        return self.num_letters

    def __successful_guess(self, guess):
        '''
        On a successful guess, fills in the word_board with the correct letter in the correct place.
        
        Parameters
        ----------
        guess : str
            input from the player to guess a letter in the word

        Returns
        -------
        None
        '''
        print(f'Good guess! {guess} is in the word')
        for i in range(len(self.word)):
            if guess == self.word[i]:
                self.word_board[i] = guess
        self.num_letters -= 1
        return self.word_board

    def __unsuccessful_guess(self, guess):
        '''
        On an unsuccessful guess, removes a life and displays number of lives left and hangman image.

        Parameters
        ----------
        guess : str
            input from the player to gues a letter in the word
        
        Returns
        -------
        None
        '''
        self.ui.num_lives -= 1
        print(f'Sorry, {guess} is not in the word. Try again')
        print (f'You have {self.ui.num_lives} lives left.')
        self.ui.display_image()

    def check_guess(self, guess): 
        '''
        Checks whether the letter guessed is in the word chosen.

        Parameters
        ----------
        guess : str
            input from the player to gues a letter in the word

        Returns
        -------
        None
        '''
        if guess in self.word:
            self.__successful_guess(guess)
        else:
            self.__unsuccessful_guess(guess)
        print (self.word_board)

    def win_lose_continue(self):
        '''
        Checks num_letters is greater than 0 and self.ui.num_lives is greater than 0, if either proves True, tells you whether you won or lost. 

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        while True:  
            if self.ui.num_lives > 0 and self.num_letters > 0:
                guess = self.ui.ask_for_input()
                self.process_input(guess)
            elif self.ui.num_lives == 0:
                print(f"You lost the game! The word was {self.word}.")
                break
            else:
                self.end_time = time()
                self.elapsed_time = self.final_timer()
                print(f"Congrats, you won the game! You had {self.ui.num_lives} lives left and took {self.formatted_time} seconds to complete the word")
                break
    
    def final_timer(self):
        elapsed_time = self.end_time - self.start_time
        self.formatted_time = "{:.2f}".format(elapsed_time)
        return self.formatted_time

def play_game():
    '''
    Calls an instance of a game of Hangman.

    Parameters
    ----------
    None

    Returns
    -------
    None

    '''
    word_list = ['pineapple', 'strawberries', 'raspberries', 'peach', 'apple']
    game = Hangman(word_list)
    print(game.word_board)
    game.win_lose_continue()
        
if __name__ == "__main__":
    play_game()
