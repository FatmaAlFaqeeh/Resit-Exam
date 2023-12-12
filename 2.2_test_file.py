import unittest
from pangram_checker import is_pangram

class TestIsPangram(unittest.TestCase):

    def test_pangram_sentence(self):
#I chose this case because it's a famous pangram
        result = is_pangram("The quick brown fox jumps over the lazy dog")
        self.assertTrue(result)

    def test_another_pangram(self):
#Testing with another famous pangram
        result = is_pangram("The five boxing wizards jump quickly")
        self.assertTrue(result)

    def test_pangram_with_symbols(self):
#Testing a pangram that contains punctuation
        result = is_pangram("Sphinx of black quartz, judge my vow")
        self.assertTrue(result)

    def test_not_a_pangram(self):
#Testing with a sentence which isn't a pangram
        result = is_pangram("This is not a pangram")
        self.assertFalse(result)

    def test_incomplete_pangram(self):
        # I chose to test a sentence which is nearly a pangram but is missing sone letters
        result = is_pangram("The quick brown fox")
        self.assertFalse(result)

    def test_empty_string(self):
        # Testing the pangram with an empty string
        result = is_pangram("")
        self.assertFalse(result)

    def test_all_letters_case_insensitive(self):
        # Testing with a pangram that is fully uppercase
        result = is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
        self.assertTrue(result)

    def test_numbers_and_special_characters(self):
        # Testing with a sentence that contains numbers and special characters
        result = is_pangram("Pack my box with five dozen liquor jugs!!!")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

