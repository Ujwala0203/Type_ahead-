import unittest

from auto_suggest import auto_suggest  # type: ignore


class TestAutoSuggest(unittest.TestCase):
    def test_exact_subword_match(self):
        words = ['take', 'make', 'check', 'ack', 'rake']
        subword = 'ke'
        expected_result = ['take', 'make', 'rake']
        self.assertEqual(auto_suggest(words, subword), expected_result) # type: ignore

    def test_wildcard_match(self):
        words = ['take', 'make', 'check', 'ack', 'rake']
        subword = '*k'
        expected_result = ['check', 'ack']
        self.assertEqual(auto_suggest(words, subword), expected_result) # type: ignore

    def test_no_match(self):
        words = ['take', 'make', 'check', 'ack', 'rake']
        subword = 'xyz'
        expected_result = []
        self.assertEqual(auto_suggest(words, subword), expected_result) # type: ignore

    def test_case_insensitive_match(self):
        words = ['Take', 'Make', 'check', 'aCk', 'RaKe']
        subword = 'tA'
        expected_result = ['Take']
        self.assertEqual(auto_suggest(words, subword), expected_result) # type: ignore

    def test_empty_input(self):
        words = []
        subword = '*k'
        expected_result = []
        self.assertEqual(auto_suggest(words, subword), expected_result) # type: ignore

# Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
