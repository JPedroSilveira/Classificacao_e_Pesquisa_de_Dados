import SimpleHashTable
import StringHashTable
import AnyTypeHashTable
import string
import random

def main():
    #Resize on new
    print('Teste On New')
    test_hash_table_new = SimpleHashTable.SimpleHashTable(20)
    for i in range(10, 30):
        if test_hash_table_new.add(i, f"valor {i}") == -1:
            print(f"ERRO ao inserir valor {i}")

    #Elementos irão se deslocar para as casas de 10 a 30 com o novo tamanho
    test_hash_table_new_resized = test_hash_table_new.resize_on_new(30)
    test_hash_table_new_resized.print_table()

    #Resize in situ
    print('Teste In Situ')
    test_hash_table = SimpleHashTable.SimpleHashTable(20)
    for i in range(30, 50):
        if test_hash_table.add(i, f"valor {i}") == -1:
            print(f"ERRO ao inserir valor {i}")

    # Elementos irão se deslocar para as casas de 30 a 50 com o novo tamanho
    test_hash_table.resize_in_situ(50)
    test_hash_table.print_table()

    #String Hash Table
    print('Teste String Hash Table')
    string_hash_table = StringHashTable.StringHashTable(20)
    alpha = list(string.ascii_letters)

    for i in range(0, 15):
        word_size = random.randint(1, 50)
        word = ''
        for i in range(0,word_size):
            random_position = random.randint(0, 51)
            word = word + alpha[random_position]

        if string_hash_table.add(word, "valor " + word) == -1:
            print(f"ERRO ao inserir valor " + word)

    string_hash_table.print_table()

    #Any type Hash Table
    print('Any Type Hash Table')
    any_type_hash_table = AnyTypeHashTable.AnyTypeHashTable(40)

    #Inserindo Strings

    for i in range(0, 15):
        word_size = random.randint(1, 50)
        word = ''
        for i in range(0,word_size):
            random_position = random.randint(0, 51)
            word = word + alpha[random_position]

        if any_type_hash_table.add(word, "valor "+word) == -1:
            print(f"ERRO ao inserir valor " + word)

    #Inserindo números
    for i in range(15, 30):
        if any_type_hash_table.add(i, f"valor {i}") == -1:
            print(f"ERRO ao inserir valor {i}")

    any_type_hash_table.print_table()


if __name__ == '__main__':
    main()