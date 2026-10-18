import unittest

from number_words_lib import int_to_words
from number_words_lib.core import _two_digits


class TestIntToWords(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(int_to_words(0), "zero")

    def test_negative_one(self):
        self.assertEqual(int_to_words(-1), "negative one")

    def test_single_digits(self):
        self.assertEqual(int_to_words(7), "seven")

    def test_teens(self):
        self.assertEqual(int_to_words(13), "thirteen")
        self.assertEqual(int_to_words(15), "fifteen")
        self.assertEqual(int_to_words(18), "eighteen")

    def test_round_tens(self):
        self.assertEqual(int_to_words(20), "twenty")
        self.assertEqual(int_to_words(40), "forty")
        self.assertEqual(int_to_words(90), "ninety")

    def test_hyphenated_tens(self):
        self.assertEqual(int_to_words(21), "twenty-one")
        self.assertEqual(int_to_words(99), "ninety-nine")

    def test_exact_hundred(self):
        self.assertEqual(int_to_words(100), "one hundred")
        self.assertEqual(int_to_words(500), "five hundred")

    def test_hundred_and_something(self):
        self.assertEqual(int_to_words(101), "one hundred one")
        self.assertEqual(int_to_words(115), "one hundred fifteen")
        self.assertEqual(int_to_words(123), "one hundred twenty-three")

    def test_thousands(self):
        self.assertEqual(int_to_words(1000), "one thousand")
        self.assertEqual(int_to_words(1001), "one thousand one")
        self.assertEqual(int_to_words(1234), "one thousand two hundred thirty-four")

    def test_millions(self):
        self.assertEqual(int_to_words(1000000), "one million")
        self.assertEqual(
            int_to_words(1234567),
            "one million two hundred thirty-four thousand five hundred sixty-seven",
        )

    def test_max_value(self):
        self.assertEqual(
            int_to_words(999999999),
            "nine hundred ninety-nine million nine hundred ninety-nine thousand "
            "nine hundred ninety-nine",
        )

    def test_negative_max(self):
        self.assertEqual(
            int_to_words(-999999999),
            "negative nine hundred ninety-nine million nine hundred ninety-nine "
            "thousand nine hundred ninety-nine",
        )

    def test_chunk_with_zero_tens(self):
        self.assertEqual(int_to_words(1000001), "one million one")
        self.assertEqual(int_to_words(1000100), "one million one hundred")

    def test_out_of_range_raises(self):
        with self.assertRaises(ValueError):
            int_to_words(1000000000)
        with self.assertRaises(ValueError):
            int_to_words(-1000000000)

    def test_bool_rejected(self):
        with self.assertRaises(TypeError):
            int_to_words(True)

    def test_two_digits_helper(self):
        self.assertEqual(_two_digits(0), "zero")
        self.assertEqual(_two_digits(10), "ten")
        self.assertEqual(_two_digits(12), "twelve")
        self.assertEqual(_two_digits(30), "thirty")
        self.assertEqual(_two_digits(45), "forty-five")


if __name__ == "__main__":
    unittest.main()
