from hangman_model import play_game, Hangman
import unittest
from io import StringIO
from unittest.mock import patch

class HangmanTestCaase(unittest.TestCase):
    def setUp(self):
        self.word_list = ['cow', 'pig', 'hen']
        self.game = Hangman(self.word_list)
        

    def test_word_is_chosen(self):
        self.assertNotEqual(self.game.word, None)

    def test_num_letters(self):
        self.assertEqual(self.game.num_letters, 3)

    def test_guess_is_processed_correctly(self):
        guess = "A"
        self.assertEqual(self.game.process_input(guess),"a")

    @patch('sys.stdout', new_callable = StringIO) #replaces the standard output with a str object for this test
    def test_invalid_character(self, mock_stdout):
        guess = "."
        self.game.process_input(guess)
        self.assertEqual(mock_stdout.getvalue(), "Invalid letter. Please enter a single alphabetical character.\n")

    
        