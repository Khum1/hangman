from hangman_model import play_game, Hangman
import random
import unittest

class HangmanTestCaase(unittest.TestCase):
    def setUp(self):
        self.word_list = ['cow', 'pig', 'hen']
        self.game = Hangman(self.word_list)

    def test_word_is_chosen(self):
        self.assertNotEqual(self.game.word, None)

    def test_num_letters(self):
        self.assertEqual(self.game.num_letters, 3)

    def test_guess_is_processed_correctly(self):
        guess_list = ['aa', '.', '1']
        for guess in guess_list:
            self.game.process_input(guess)
        self.assertEqual()