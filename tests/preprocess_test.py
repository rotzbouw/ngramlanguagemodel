from ngramlanguagemodel.preprocess import *
import unittest


class PreprocessingTests(unittest.TestCase):

    def test_normalisation(self):
        test_string = "text with numbers 09 348 and punctuation $#+ and it's great."
        actual = normalise(test_string)
        expected = "text with numbers   and punctuation  and it's great"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
