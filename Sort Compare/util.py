import random
import time
import numpy
import pandas


def log(data: dict):
    print(f'''
    Data:
        Algoritmo: {data['algorithm']}
        Tipo: {data['type']}
        Quantidade: {data['size']}
        Média de trocas: {data['md_exchange']}
        Desvio padrão de trocas: {data['sd_exchange']}
        Média de comparações: {data['md_compare']}
        Desvio padrão de comparações: {data['sd_compare']}
        Média de tempo: {data['md_time']}
        Desvio padrão de tempo: {data['sd_time']}
        ''')


def show_data_frame(data: dict):
    df = pandas.DataFrame(data)
    cols = ['algorithm', 'type', 'size', 'md_exchange', 'sd_exchange', 'md_compare', 'sd_compare', 'md_time', 'sd_time']
    df = df[cols]

    print(df)


def generate_random_int_arr(length: int) -> list:  # generate a array with length value of items
    n = []

    for i in range(0, length):
        n.append(random.randrange(0, length * (10 ** 3)))

    return n


def get_average(arr: list) -> int:  # calculate the average of a int array
    return numpy.mean(arr)


def get_std(arr: list) -> int:
    return numpy.std(arr)


def get_time():
    return time.process_time()
