import _queue
import threading
from queue import Queue
from KeywordSearch.InputStreamPreprocess.html_preprocess import HtmlPagePreprocess
from KeywordSearch.keywords_searcher import KeywordsSearcher
from RateLimiting.config import RATE_LIMIT_INTERVAL


class KeywordSearcherWorkerThread(threading.Thread):
    def __init__(self, keywords_file_path: str, message_queue: Queue, queue_is_empty_event: threading.Event,
                 stop_event: threading.Event, worker_id: int):
        super(KeywordSearcherWorkerThread, self).__init__()
        self.stop_event = stop_event
        self._queue_is_empty_event = queue_is_empty_event
        self._worker_id = worker_id
        self._keywords_searcher = KeywordsSearcher(keywords_file_path=keywords_file_path, input_preprocessor=HtmlPagePreprocess())
        self._wiki_pages_mq = message_queue

    def run(self) -> None:
        while not self.stop_event.isSet():
            try:
                if self._wiki_pages_mq.empty():
                    self._queue_is_empty_event.set()
                wiki_message = self._wiki_pages_mq.get(timeout=RATE_LIMIT_INTERVAL)
                wiki_url, wiki_body = wiki_message['url'], wiki_message['body']
                matches = self._keywords_searcher.search_all(wiki_body)
                if not self.stop_event.isSet():
                    print(f'Worker: {self._worker_id}\nRandom URL: {wiki_url}\nMatches: {matches}\n-----------------------------')
            except _queue.Empty:
                self._queue_is_empty_event.set()




