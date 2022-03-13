import logging
from concurrent.futures import ThreadPoolExecutor

from utils import io_bound_function, cpu_bound_function


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(cpu_bound_function, range(3))
