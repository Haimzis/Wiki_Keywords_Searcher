from KeywordSearch.InputStreamPreprocess.abstract_preprocess import AbstractInputStreamPreprocess


class DefaultStringPreprocess(AbstractInputStreamPreprocess):
    def preprocess(self, text: str):
        return text.lower()
