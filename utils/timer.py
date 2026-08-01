import time


class Timer:

    def __enter__(self):

        self.start = time.perf_counter()

        return self

    def __exit__(self, *args):

        self.end = time.perf_counter()

        self.elapsed = round(
            self.end - self.start,
            2
        )