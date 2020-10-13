import threading


def singleton(cls):
    instances = {}
    lock = threading.Lock()

    def get_instance(keywords_file_path):
        if cls not in instances:
            lock.acquire()
            if cls not in instances:
                instances[cls] = cls(keywords_file_path)
            lock.release()
        return instances[cls]
    return get_instance


@singleton
class KeywordsFileReader:
    def __init__(self, keywords_file_path):
        self._keywords_list = None
        self._read_keywords(keywords_file_path)

    def _read_keywords(self, keywords_file_path: str) -> None:
        """
        :param keywords_file_path
        :return: None, updates the keywords list once and for all.
        """
        with open(keywords_file_path, 'r') as keywords_file:
            self._keywords_list = keywords_file.read().splitlines()

    @property
    def get_all(self) -> list:
        return self._keywords_list
