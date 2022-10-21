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
    word_guessed : list
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
        word_guessed : list
            representation of the word to be guessed with '_' to be replaced with the correct letters guessed
        num_letters: int
            number of unique letters in the word that have not been guessed yet
        list_of_guesses : list
            list of guesses that have already been tried
        '''
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = self.word_guessed = len(self.word)*["_"]
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
            if letter in self.word_guessed and letter not in unique_letters_set:
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
                    self.word_guessed[i] = guess
            print (self.word_guessed)
            self.num_letters = self.get_num_unique_letters()
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again')
            print (f'You have {self.num_lives} lives left.')
            self.display_image()
    
    def ask_for_input(self):
        '''
        Asks the player for a letter to be guessed. 
        If the letter has already been guessed or the letter is non-alphabetical or more than one letter is 
        guessed, it will return a statement to try a different letter.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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
        '''
        Displays the image of the evolving hangman with each wrong guess.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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


hangman_image = [ #Image matrix for displaying the evolving hangman
  [9,9,9,9,9],
  [8,0,0,1,0],
  [8,0,4,2,3],
  [8,0,4,0,3],
  [9,9,9,9,9]
    ]
    

play_game()
