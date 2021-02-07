import unittest
import lib

class TestWordCount(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(lib.count_word("Hello World"), 2)