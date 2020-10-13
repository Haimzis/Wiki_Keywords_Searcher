from KeywordSearch.InputStreamPreprocess.simple_str_preprocess import DefaultStringPreprocess
from KeywordSearch.InputStreamPreprocess.abstract_preprocess import AbstractInputStreamPreprocess
from KeywordSearch.RegexPatternCreator.abstract_pattern_creator import AbstractRegexPatternCreator
from KeywordSearch.keywords_file_reader import KeywordsFileReader
from KeywordSearch.RegexPatternCreator.keywords_pattern_creator import KeywordsRegexPatternCreator
import re


class KeywordsSearcher:
    def __init__(self, keywords_file_path: str,
                 input_preprocessor: AbstractInputStreamPreprocess = DefaultStringPreprocess(),
                 re_pattern_creator: AbstractRegexPatternCreator = KeywordsRegexPatternCreator()):
        self._keywords_reader = KeywordsFileReader(keywords_file_path)
        self._input_preprocessor = input_preprocessor
        self._re_pattern_creator = re_pattern_creator

    def search_all(self, input_stream: str) -> list:
        """
        :param input_stream: an input in some type.
        :return: keywords instances in the input.
        """
        instance_list = []
        processed_input = self._input_preprocessor.preprocess(input_stream)
        for keyword in self._keywords_reader.get_all:
            if self._search_one(keyword, processed_input):
                instance_list.append(keyword)
        return instance_list

    def _search_one(self, keyword: str, processed_input: str) -> bool:
        keyword_pattern = self._re_pattern_creator.create_pattern(keyword)
        is_keyword_found = re.search(keyword_pattern, processed_input)
        return is_keyword_found is not None
