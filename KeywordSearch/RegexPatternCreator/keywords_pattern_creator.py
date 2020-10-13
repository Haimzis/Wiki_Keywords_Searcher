from KeywordSearch.config import KEYWORDS_DELIMITERS_REG_EXPRESSION, INPUT_DELIMITERS_REG_EXPRESSION
from KeywordSearch.RegexPatternCreator.abstract_pattern_creator import AbstractRegexPatternCreator
import re


class KeywordsRegexPatternCreator(AbstractRegexPatternCreator):
    def __init__(self):
        self._keywords_delimiters_reg_expression = KEYWORDS_DELIMITERS_REG_EXPRESSION
        self._input_delimiters_reg_expression = INPUT_DELIMITERS_REG_EXPRESSION

    def create_pattern(self, keyword: str) -> str:
        """
        :param keyword.
        :return: re pattern for finding it.
        """
        lower_keyword = keyword.lower()
        lower_keywords_without_delimiters = re.split(pattern=self._keywords_delimiters_reg_expression, string=lower_keyword)
        re_pattern = self._input_delimiters_reg_expression.join(lower_keywords_without_delimiters)
        return re_pattern
