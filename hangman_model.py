import random

class Hangman:

    '''
    A class to start a game of Hangman
    ...
    Attributes
    ----------
    num_lives : int
        number of lives that the player has remaining
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
    check_guess(guess):
        checks whether the letter guessed is in the word chosen
    ask_for_input():
        asks the player for a letter to be guessed
    display_image():
        displays the image of the evolving hangman with each wrong guess

    '''

    def __init__(self, word_list, num_lives):
        '''
        Constructs the necessary attributes for the Hangman object.

        Parameters
        ----------
        num_lives : int
            number of lives that the player has remaining
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
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_board = self.word_board = len(self.word)*["_"]
        self.num_letters = self.get_num_unique_letters()
        self.list_of_guesses = []

        
    def get_num_unique_letters(self):
        '''
        Gets the number of unique letters to be guessed.

        Parameters
        ----------
        None

        Returns
        -------
        len(unique_letters_set) - letters_guessed (int): the number of the unique letters in the word - the number of correct letters guessed

        '''
        unique_letters_set = set()
        letters_guessed = 0
        for letter in self.word: 
            if letter in self.word_board and letter not in unique_letters_set:
                letters_guessed += 1
            unique_letters_set.add(letter)
        return len(unique_letters_set) - letters_guessed 

    def check_guess(self, guess): 
        '''
        Checks whether the letter guessed is in the word chosen.

        Parameters
        ----------
        guess (str) : input from the player to guess a letter in the word

        Returns
        -------
        None
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_board[i] = guess
            print (self.word_board)
            self.num_letters = self.get_num_unique_letters()
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again')
            print (f'You have {self.num_lives} lives left.')
            self.display_image()
    
    


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
    game = Hangman(word_list, 5)
    print(game.word_board)
    while True:
        if game.num_lives > 0 and game.num_letters != 0:
            game.ask_for_input()
        elif game.num_lives == 0:
            print(f"You lost the game! The word was {game.word}.")
            break
        else:
            print("Congrats, you won the game!")
            break
    

play_game()
