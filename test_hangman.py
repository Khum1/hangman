from hangman_model import play_game, Hangman
import random
import unittest

class HangmanTestCaase(unittest.TestCase):
    def setUp(self):
        self.word_list = ['cow', 'pig', 'hen']
        self.game = Hangman(self.word_list)

    def test_word_is_chosen(self):
        self.assertNotEqual(self.game.word, None)

    