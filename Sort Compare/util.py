import random
import time
import numpy
import datetime


def generate_random_int_arr(length: int) -> list:  # generate a array with length value of items
    n = []

    for i in range(0, length):
        n.append(random.randrange(0, length * 10))

    return n


def get_average(arr: list) -> int:  # calculate the average of a int array
    return numpy.mean(arr)


def get_std(arr: list) -> int:
    return numpy.std(arr)


def get_time():
    return time.process_time()


def get_datatime():
    return datetime.datetime.now()