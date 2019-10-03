# coding=utf-8
import State


class SimpleHashTable:
    # Cria uma HashTable baseado no tamanho passado
    def __init__(self, size):
        self.size = size
        self.dictionary = [State.HashState.empty.value] * size
        self.data = [None] * size
        self.used = [False] * size

    def add(self, key, data):
        position = start_position = key % self.size

        if self.dictionary[position] == State.HashState.empty.value:  # se estiver vazio
            self.dictionary[position] = key  # coloca a chave
            self.data[position] = data  # associa dado
            self.used[position] = True
            return position
        else:  # se estiver ocupado, tenta achar lugar usando linear probing
            first_pass = True
            while position != start_position or first_pass:
                first_pass = False
                # incrementa posicão (mas fica dentro do intervalo do array de chaves)
                position = (position + 1) % self.size
                if self.dictionary[position] == State.HashState.empty.value:
                    self.dictionary[position] = key
                    self.data[position] = data
                    self.used[position] = True
                    return position

        if position == start_position:  # se posicao igual à inicial é porque fez a volta e não achou
            return State.HashState.empty.value  # informa que deu problema (está cheio)
        else:
            return position  # retorna posição onde colocou o dado

    def get(self, key):
        start_position = position = key % self.size
        first_pass = True

        # busca elemento usando linear probing:
        while self.dictionary[position] != key and self.used[position] and (start_position != position or first_pass):
            first_pass = False
            position = (position + 1) % self.size

        if self.dictionary[position] == key:
            return self.data[position]
        else:
            return None  # se chegou aqui é porque não existe a chave

    def remove(self, key):
        start_position = position = key % self.size
        first_pass = True

        # busca elemento usando linear probing:
        while self.dictionary[position] != key and self.used and (start_position != position or first_pass):
            first_pass = False
            position = (position + 1) % self.size

        if self.dictionary[position] == key:
            self.dictionary[position] = -1
            self.data[position] = None
            return position
        else:
            return None  # se chegou aqui é porque não existe a chave
        return State.HashState.empty.value

    # modifica tamanho da tabela criando nova tabela
    def resize_on_new(self, new_size):
        new_hash_table = SimpleHashTable(new_size)
        for position in range(0, self.size):
            if self.dictionary[position] != State.HashState.empty.value:
                new_hash_table.add(self.dictionary[position], self.data[position])

        return new_hash_table

    # modifica tamanho da tabela nela mesmo
    def resize_in_situ(self, new_size):
        #  Modificando o tamanho
        old_size = self.size
        self.size = new_size
        new_dictionary = [State.HashState.empty.value] * (new_size - old_size)
        new_data = [None] * (new_size - old_size)
        new_used = [False] * (new_size - old_size)
        self.dictionary = self.dictionary + new_dictionary
        self.data = self.data + new_data
        self.used = self.used + new_used

        for i in range(0, old_size):
            new_position = self.dictionary[i] % self.size
            if new_position != i:
                if self.dictionary[new_position] == State.HashState.empty.value:
                    #  Adiciona na nova posição
                    self.dictionary[new_position] = self.dictionary[i]
                    self.data[new_position] = self.data[i]
                    self.used[new_position] = True
                    #  Remove da antiga posição
                    self.dictionary[i] = State.HashState.empty.value
                    self.data[i] = None
                    self.used[i] = False
                elif new_position <= old_size:
                    process_finished = False
                    while(not process_finished):
                        #  Salvando dados do local antigo
                        temp_key = self.dictionary[new_position]
                        temp_data = self.data[new_position]
                        #  Reescrevendo
                        self.dictionary[new_position] = self.dictionary[i]
                        self.data[new_position] = self.data[i]
                        #  Calcula nova posição do item retirado
                        new_position = temp_key % self.size
                        if self.dictionary[new_position] == State.HashState.empty.value:
                            #  Adiciona na nova posição
                            self.dictionary[new_position] = temp_key
                            self.data[new_position] = temp_data
                            self.used[new_position] = True
                            process_finished = True
                        else:
                            continue_searching = True
                            while continue_searching:
                                # incrementa posicão (mas fica dentro do intervalo do array de chaves)
                                new_position = (new_position + 1) % self.size
                                if self.dictionary[new_position] == State.HashState.empty.value:
                                    self.dictionary[new_position] = temp_key
                                    self.data[new_position] = temp_data
                                    self.used[new_position] = True
                                    continue_searching = False
                else:
                    key = self.dictionary[i]
                    data = self.data[i]
                    self.dictionary[i] = State.HashState.empty.value
                    self.data[i] = None
                    self.used[i] = False
                    self.add(key, data)
        return -1

    def print_table(self):
        for i in range(0, self.size):
            print(f"({i:03d})[{self.dictionary[i]:03d}] = {str(self.data[i]):15s} ({self.used[i]})")
