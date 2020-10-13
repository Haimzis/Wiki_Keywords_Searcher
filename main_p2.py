from KeywordSearch.config import KEYWORDS_FILE_PATH
from RateLimiting.config import NUMBER_OF_WORKERS, KEYWORDS_FILE_PATH, REQUESTS_PER_SEC
from RateLimiting.wiki_keywords_searcher import WikipediaKeywordSearcher


def main():
    wiki_keywords_searcher = WikipediaKeywordSearcher(KEYWORDS_FILE_PATH, NUMBER_OF_WORKERS, REQUESTS_PER_SEC)
    wiki_keywords_searcher.start()


if __name__ == '__main__':
    main()

