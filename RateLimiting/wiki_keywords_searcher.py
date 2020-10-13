import signal
import sys
import threading
from queue import Queue
from time import sleep

from RateLimiting.producer import WikiPagesProducer
from RateLimiting.worker import KeywordSearcherWorkerThread


class WikipediaKeywordSearcher:
    def __init__(self, keywords_file_path: str, number_of_workers: int, requests_per_second: int):
        queue_is_empty_event = threading.Event()
        self.stop_event = threading.Event()
        self._message_queue = Queue(maxsize=requests_per_second)
        self._workers = [KeywordSearcherWorkerThread(keywords_file_path, self._message_queue, queue_is_empty_event, self.stop_event, worker_number) for
                         worker_number in range(1, number_of_workers + 1)]
        self._pages_producer = WikiPagesProducer(self._message_queue, queue_is_empty_event, self.stop_event)

    def start(self) -> None:
        self._pages_producer.start()
        for worker in self._workers:
            worker.start()
        signal.signal(signal.SIGINT, self.stop)
        self.stop_event.wait()
        # waits for producer, workers finish
        self._pages_producer.join()
        for worker in self._workers:
            worker.join()


    def stop(self, signal, frame):
        # throws stop event for all the threads.
        self.stop_event.set()
        print('\n#### KEYBOARD INTERRUPTION EVENT - SHUTTING THE PROGRAM ####\n')
