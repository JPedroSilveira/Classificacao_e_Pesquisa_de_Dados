# coding=utf-8
import State


class AnyTypeHashTable:
    # Cria uma HashTable baseado no tamanho passado
    def __init__(self, size):
        self.size = size
        self.dictionary = [None] * size
        self.data = [None] * size
        self.used = [False] * size

    def position_calculator(self, key):
        str_key = str(key)
        size = len(str_key)
        position = 0
        for i in (0, size - 1):
            position = i * (ord(str_key[i]) + position)

        return position % self.size

    def add(self, key, data):
        position = start_position = self.position_calculator(key)

        if self.dictionary[position] is None:  # se estiver vazio
            self.dictionary[position] = key  # coloca a chave
            self.data[position] = data  # associa dado
            self.used[position] = True
            return position
        else:  # se estiver ocupado, tenta achar lugar usando linear probing
            first_pass = True
            while position != start_position or first_pass:
                first_pass = False
                # incrementa posicão (mas fica dentro do intervalo do array de chaves)
                position = position + 1
                if self.dictionary[position] is None:
                    self.dictionary[position] = key
                    self.data[position] = data
                    self.used[position] = True
                    return position

        if position == start_position:  # se posicao igual à inicial é porque fez a volta e não achou
            return State.HashState.empty.value  # informa que deu problema (está cheio)
        else:
            return position  # retorna posição onde colocou o dado

    def get(self, key):
        position = start_position = self.position_calculator(key)
        first_pass = True

        # busca elemento usando linear probing:
        while self.dictionary[position] != key and self.used[position] and (start_position != position or first_pass):
            first_pass = False
            position = position + 1

        if self.dictionary[position] == key:
            return self.data[position]
        else:
            return None  # se chegou aqui é porque não existe a chave

    def remove(self, key):
        position = start_position = self.position_calculator(key)
        first_pass = True

        # busca elemento usando linear probing:
        while self.dictionary[position] != key and self.used and (start_position != position or first_pass):
            first_pass = False
            position = position + 1

        if self.dictionary[position] == key:
            self.dictionary[position] = None
            self.data[position] = None
            return position
        else:
            return None  # se chegou aqui é porque não existe a chave
        return None

    def print_table(self):
        for i in range(0, self.size):
            print(f"({i:03d})[{str(self.dictionary[i]):64s}] = {str(self.data[i]):20s} ({self.used[i]})")
