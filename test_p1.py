import unittest
from KeywordSearch.config import KEYWORDS_FILE_PATH, TEST_EXAMPLES
from KeywordSearch.keywords_searcher import KeywordsSearcher


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.keywords_searcher = KeywordsSearcher(keywords_file_path=KEYWORDS_FILE_PATH)

    def test_results(self):
        for test_example in TEST_EXAMPLES:
            with self.subTest(line=test_example):
                self.assertEqual(set(self.keywords_searcher.search_all(test_example['input'])), test_example['result'])


unittest.main()
