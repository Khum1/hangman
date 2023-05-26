import random
from user_interface import UserInterface, num_lives

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
        self.ui = UserInterface(5)

    def check_letter_in_board(self, letter, letters_guessed, unique_letters_set):
        '''
        Checks if the letter given is in the game_board or unique_letters_set.

        Parameters
        ----------
        letter : str
            guessed by the player
        letters_guessed : int 
            number of unique letters guessed by the player
        unique_letters_set : set 
            a set listing all of the letters that have been guessed by the player

        Returns
        -------
        letters_guessed : int
            number of unique letters guessed by the player


        '''
        if letter in self.word_board and letter not in unique_letters_set:
            letters_guessed += 1
        return letters_guessed

    def get_num_unique_letters(self):
        '''
        Gets the number of unique letters to be guessed.

        Parameters
        ----------
        None

        Returns
        -------
        len(unique_letters_set) - letters_guessed : int
            the number of the unique letters in the word - the number of correct letters guessed

        '''
        unique_letters_set = set()
        letters_guessed = 0
        for letter in self.word: 
            self.check_letter_in_board(letter, letters_guessed, unique_letters_set)
            unique_letters_set.add(letter)
        return len(unique_letters_set) - letters_guessed
    
    def successful_guess(self, guess):
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
        print (self.word_board)

    def unsuccessful_guess(self, guess):
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
        num_lives -= 1
        print(f'Sorry, {guess} is not in the word. Try again')
        print (f'You have {num_lives} lives left.')
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
        guess = guess.lower()
        if guess in self.word:
            self.successful_guess(guess)
            self.num_letters = self.get_num_unique_letters()
        else:
            self.unsuccessful_guess(guess)

    def win_lose_continue(self):
        while True:
            if num_lives > 0 and self.num_letters != 0:
                self.ui.ask_for_input()
            elif num_lives == 0:
                print(f"You lost the game! The word was {self.word}.")
                break
            else:
                print("Congrats, you won the game!")
                break

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

play_game()
