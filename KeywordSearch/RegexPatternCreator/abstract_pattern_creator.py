from abc import ABC, abstractmethod


class AbstractRegexPatternCreator(ABC):
    @abstractmethod
    def create_pattern(self, keyword: str) -> str:
        """
        :param keyword: desired keyword
        :return: regex pattern for finding it, under the specific task specification.
        """
        pass
