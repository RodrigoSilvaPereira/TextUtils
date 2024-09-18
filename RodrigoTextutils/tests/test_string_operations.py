import unittest
from textutils.string_operations import reverse_string, capitalize_words

class TestStringOperations(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")

if __name__ == '__main__':
    unittest.main()
