import unittest

from tinytext import char_count, word_count


class WordCountTest(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("one two  three"), 3)

    def test_empty(self):
        self.assertEqual(word_count(""), 0)


class CharCountTest(unittest.TestCase):
    def test_counts_characters_including_whitespace_by_default(self):
        self.assertEqual(char_count("a b\t\n!"), 6)

    def test_excludes_all_whitespace_when_requested(self):
        self.assertEqual(char_count("a b\t\n!", include_spaces=False), 3)

    def test_empty(self):
        self.assertEqual(char_count(""), 0)


if __name__ == "__main__":
    unittest.main()
