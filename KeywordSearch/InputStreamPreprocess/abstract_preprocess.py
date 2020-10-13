from abc import ABC, abstractmethod


class AbstractInputStreamPreprocess(ABC):
    @abstractmethod
    def preprocess(self, input_stream):
        """
        :param input_stream
        :return: input after a desired preprocess for a specific input source.
        """
        pass
