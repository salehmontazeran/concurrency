import time
import logging


def io_bound_function(name):
    logging.info("Task %s: starting", name)
    time.sleep(3)
    logging.info("Task %s: finishing", name)


def cpu_bound_function(name):
    logging.info("Task %s: starting", name)
    list(range(179999999 + name))
    logging.info("Task %s: finishing", name)
    return "sisil"
