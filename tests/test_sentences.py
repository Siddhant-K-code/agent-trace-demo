import unittest

from tinytext import sentence_count


class SentenceCountTest(unittest.TestCase):
    def test_counts_sentences(self):
        self.assertEqual(sentence_count("One. Two! Three?"), 3)

    def test_no_terminator(self):
        self.assertEqual(sentence_count("Hello world"), 1)

    def test_trailing_text(self):
        self.assertEqual(sentence_count("Hi. There"), 2)

    def test_repeated_punctuation(self):
        self.assertEqual(sentence_count("Wait... what?!"), 2)

    def test_empty_and_blank(self):
        self.assertEqual(sentence_count(""), 0)
        self.assertEqual(sentence_count("  \n "), 0)
        self.assertEqual(sentence_count("..."), 0)


if __name__ == "__main__":
    unittest.main()
