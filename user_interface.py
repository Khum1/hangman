
class UserInterface():
    '''
    Creates user  interface for hangman game.

    Attributes
    ----------
    num_lives : int
        number of lives that the player has remaining

    Methods
    -------

    '''
    def __init__(self, num_lives):
        self.num_lives = num_lives

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

    def check_condition(self):
        '''
        Checks the conditions are met in the conditions matrix

        Parameters
        ----------
        None

        Returns
        -------
        False : bool
        '''
        if self.char in conditions:
            return conditions[self.char]()
        return False

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
            line = ''.join(char if self.check_condition() else ' ' for char in item)
            print(line)

num_lives = 5
ui = UserInterface(num_lives) 

conditions = {
' ': True,
'O': ui.num_lives <= 3,
'|': ui.num_lives <= 2,
'\\': ui.num_lives <= 1,
'/': ui.num_lives <= 0,
'_': ui.num_lives <= 4,
}

hangman_image = [ #Image matrix for displaying the evolving hangman
    ['_','_','_','_','_'],
    ['|',' ',' ','O',' '],
    ['|',' ','/','|','\\'],
    ['|',' ','/',' ','\\'],
    ['_','_','_','_','_']
    ]


