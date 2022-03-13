import logging
from utils import thread_function

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    result = map(thread_function, range(3))
    result = list(result)
