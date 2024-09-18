import unittest
from textutils.text_analysis import word_count, sentence_count

class TestTextAnalysis(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_sentence_count(self):
        self.assertEqual(sentence_count("Hello. How are you?"), 2)

if __name__ == '__main__':
    unittest.main()
