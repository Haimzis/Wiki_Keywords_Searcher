import socket
import threading
import time
from queue import Queue
from urllib import request
from urllib.error import URLError, HTTPError
from timeit import default_timer as timer
from RateLimiting.config import REQUESTS_PER_SEC, RANDOM_WIKI_PAGE_URL, HTTP_REQUEST_TIMEOUT, RATE_LIMIT_INTERVAL


class WikiPagesProducer(threading.Thread):
    def __init__(self, message_queue: Queue, queue_empty_event: threading.Event, stop_event: threading.Event):
        super(WikiPagesProducer, self).__init__()
        self.stop_event = stop_event
        self._queue_empty_event = queue_empty_event
        self._wiki_pages_mq = message_queue

    def run(self) -> None:
        """
        puts random wiki html pages, with their url - with rate limiting of REQUESTS_PER_SEC
        waits when queue is empty.
        """
        while not self.stop_event.isSet():
            self._queue_empty_event.wait()
            start = timer()
            timers_threads = []
            for _ in range(REQUESTS_PER_SEC):
                timer_thread = threading.Thread(target=self._produce_wiki_page)
                timer_thread.start()
                timers_threads.append(timer_thread)

            for timer_thread in timers_threads:
                timer_thread.join()
            end = timer()

            if end - start < RATE_LIMIT_INTERVAL:
                time.sleep(RATE_LIMIT_INTERVAL - (end - start))
            self._queue_empty_event.clear()

    def _produce_wiki_page(self) -> None:
        # gets wiki page, and put it in the message queue
        try:
            with request.urlopen(RANDOM_WIKI_PAGE_URL, timeout=HTTP_REQUEST_TIMEOUT) as response:
                response_content = response.read().decode('utf-8')
                message = {"url": response.url, "body": response_content}
                self._wiki_pages_mq.put(message)
        except (HTTPError, URLError, socket.timeout):
            print('request timeout limit is over\n-----------------------------')
