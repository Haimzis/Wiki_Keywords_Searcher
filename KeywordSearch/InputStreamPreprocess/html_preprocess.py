from KeywordSearch.InputStreamPreprocess.abstract_preprocess import AbstractInputStreamPreprocess


class HtmlPagePreprocess(AbstractInputStreamPreprocess):
    def preprocess(self, html_body: str):
        str_input = html_body.lower()
        return str_input
