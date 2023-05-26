
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
    def __init__(self):
        self.num_lives = 5
        self.conditions = {
            ' ': lambda: self.num_lives == 5,
            '|': lambda: self.num_lives <=4,
            'O': lambda: self.num_lives <= 3,
            '[]': lambda: self.num_lives <= 2,
            '\\': lambda: self.num_lives <= 1,
            '/': lambda: self.num_lives <= 0,
            '_': lambda: self.num_lives <= 4,
        }  

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
        return guess

    def __check_condition(self, char):
        '''
        Checks the conditions are met in the conditions matrix

        Parameters
        ----------
        None

        Returns
        -------
        False : bool
        '''
        if char in self.conditions:
            return self.conditions[char]()

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
            line = ''.join(char if self.__check_condition(char) else ' ' for char in item)
            print(line)
     

ui = UserInterface() 



hangman_image = [ #Image matrix for displaying the evolving hangman
    ['_','_','_','_','_'],
    ['|',' ',' ','O',' '],
    ['|','/','[]','\\'],
    ['|','/',' ','\\'],
    ['_','_','_','_','_']
    ]


