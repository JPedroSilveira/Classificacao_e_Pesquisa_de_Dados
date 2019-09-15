import math
from typing import Any
from pandas.compat.numpy import function


# All these sorts have the same return value for generic proposes
#  Return: list (the ordered array); int (the number of compares); int (the number of exchanges)


def get_sorts(ids: list) -> list:
    sort_list = []

    for sort_id in ids:
        sort_list.append({'function': get_sort_function(sort_id),
                          'name': get_sort_name(sort_id)})

    return sort_list


def get_sort_name(sort_id: str) -> str:
    dic = {'shell_sort': 'Shell Sort', 'selection_sort': 'Selection Sort',
           'insertion_sort': 'Insertion Sort', 'binary_insertion_sort': 'Binary Search Sort',
           'merge_sort': 'Merge Sort', 'quick_sort': 'Quick Sort', 'bubble_sort': 'Bubble Sort',
           'comb_sort': 'Comb Sort', 'shake_sort': 'Shake Sort', 'improved_quick_sort': 'Improved Quick Sort',
           'heap_sort': 'Heap Sort', 'merge_insertion_sort': 'Merge Insetion Sort'}
    return dic[sort_id]


def get_sort_function(sort_id: str) -> function:
    dic = {'shell_sort': shell_sort, 'selection_sort': selection_sort,
           'insertion_sort': insertion_sort, 'binary_insertion_sort': binary_insertion_sort,
           'merge_sort': merge_sort, 'quick_sort': quick_sort, 'bubble_sort': bubble_sort,
           'comb_sort': comb_sort, 'shake_sort': shake_sort, 'improved_quick_sort': improved_quick_sort,
           'heap_sort': heap_sort, 'merge_insertion_sort': merge_insertion_sort}
    return dic[sort_id]


def bubble_sort(arr: list) -> (list, int, int):
    exchanges = compares = before_exchange = 0
    length = len(arr) - 1
    should_exchange = True

    while should_exchange:
        should_exchange = False
        for i in range(0, length):
            compares += + 1
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
                should_exchange = True
                before_exchange = i
                exchanges += 1
        length = before_exchange

    return arr, compares, exchanges


def shake_sort(arr: list) -> (list, int, int):
    exchanges = compares = 0
    swapped = True
    start = 0
    end = len(arr) - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                exchange(arr, i, i + 1)
                exchanges += 1
                swapped = True
            compares += 1

        if not swapped:
            return arr, compares, exchanges

        swapped = False

        end -= 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                exchange(arr, i, i + 1)
                exchanges += 1
                swapped = True
            compares += 1

        start += 1

    return arr, compares, exchanges


def comb_sort(arr: list) -> (list, int, int):
    length = len(arr)
    exchanges = compares = 0
    gap = length
    shrink = 1.3
    arr_sorted = False

    while not arr_sorted:
        gap = math.floor(gap / shrink)

        if gap <= 1:
            gap = 1
            arr_sorted = True

        i = 0
        while (i + gap) < length:
            if arr[i] > arr[i + gap]:
                exchange(arr, i, i + gap)
                exchanges += 1
                arr_sorted = False
            compares += 1
            i += 1

    return arr, compares, exchanges


def selection_sort(arr: list) -> (list, int, int):
    # count the number of exchanges and compares
    compares = 0
    exchanges = 0

    for i in range(len(arr)):
        m = i  # save the smallest value as the current value
        j = i + 1  # used to search all elements in the right of the current value

        while j < len(arr):  # search all right sub-array
            if arr[j] < arr[m]:  # when find a smaller value
                m = j  # save in the m
            compares += 1  # sum the compare
            j += 1

        exchanges += 1  # sum the exchange
        exchange(arr, i, m)  # exchange the selected array position with the minor value found

    return arr, compares, exchanges


def insertion_sort(arr: list) -> (list, int, int):
    # count the number of exchanges and compares
    compares = 0
    exchanges = 0

    # sort arr in increasing order
    for i in range(len(arr)):

        j = i

        # exchange i element with the predecessor until find a smaller one
        while j > 0 and arr[j] < arr[j - 1]:
            compares += 1  # sum compare
            exchanges += 1
            exchange(arr, j, j - 1)
            j -= 1

    return arr, compares, exchanges


def binary_insertion_sort(arr: list) -> (list, int, int):
    # count the number of exchanges and compares
    compares = 0
    exchanges = 0

    for i in range(1, len(arr)):  # starts in the second item
        val = arr[i]  # gets current value
        j, compares = binary_search(arr, val, 0, i - 1, compares)  # do the binary search
        exchanges += 1
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]  # re-order the list by the binary search result

    return arr, compares, exchanges


def binary_search(arr: list, val: int, start: int, end: int, compares: int) -> (int, int):
    if start == end:
        if arr[start] > val:
            return start, compares
        else:
            return start + 1, compares

    if start > end:
        return start, compares

    mid = int((start + end) / 2)
    if arr[mid] < val:
        compares += 1
        return binary_search(arr, val, mid + 1, end, compares)
    elif arr[mid] > val:
        compares += 1
        return binary_search(arr, val, start, mid - 1, compares)
    else:
        return mid, compares


def shell_sort(arr: list) -> (list, int, int):
    # count the number of exchanges and compares
    compares = 0
    exchanges = 0

    n = len(arr)  # save the length of the array
    h = 1  # starts h

    while h < (n / 3):
        h = 3 * h + 1  # 1, 4, 13, 40, 121, ... Set the h value by the array length

    while h >= 1:  # h-sort the array
        i = h  # start i with h value
        while i < n:  # insert arr[i] among a[i-h], a[i-2*h], a[i-3*h], ...
            j = i  # start j with i value
            while j >= h and arr[j] < arr[j - h]:
                exchanges += 1  # increase the exchange count value
                compares += 1  # increase the compare count value
                exchange(arr, j, j - h)
                j -= h
            i += 1
        h = int(h / 3)

    return arr, compares, exchanges


def merge_sort(arr: list) -> (list, int, int):
    compares = 0
    exchanges = 0
    aux = [0] * len(arr)
    compares, exchanges = aux_merge_sort(arr, 0, len(arr) - 1, aux, compares, exchanges)

    return arr, compares, exchanges


def aux_merge_sort(arr: list, lo: int, hi: int, aux: list, compares: int, exchanges: int) -> (int, int):
    if hi <= lo:
        return compares, exchanges

    mid = int(lo + (hi - lo) / 2)
    compares, exchanges = aux_merge_sort(arr, lo, mid, aux, compares, exchanges)
    compares, exchanges = aux_merge_sort(arr, mid + 1, hi, aux, compares, exchanges)
    compares, exchanges = merge(arr, lo, mid, hi, aux, compares, exchanges)

    return compares, exchanges


def merge(arr: list, lo: int, mid: int, hi: int, aux: list, compares: int, exchanges: int) -> (int, int):
    i = lo
    j = mid + 1

    k = lo
    while k <= hi:
        aux[k] = arr[k]
        exchanges += 1
        k += 1

    k = lo
    while k <= hi:
        if i > mid:
            exchanges += 1
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            exchanges += 1
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            exchanges += 1
            compares += 1
            arr[k] = aux[j]
            j += 1
        else:
            exchanges += 1
            arr[k] = aux[i]
            i += 1
        k += 1

    return compares, exchanges


def quick_sort(arr: list) -> (list, int, int):
    compares = 0
    exchanges = 0
    compares, exchanges = aux_quick_sort(arr, 0, len(arr) - 1, compares, exchanges)

    return arr, compares, exchanges


def aux_quick_sort(arr: list, lo: int, hi: int, compares: int, exchanges: int) -> (int, int):
    if hi <= lo:
        return compares, exchanges

    j, compares, exchanges = partition(arr, lo, hi, compares, exchanges)

    compares, exchanges = aux_quick_sort(arr, lo, j - 1, compares, exchanges)
    compares, exchanges = aux_quick_sort(arr, j + 1, hi, compares, exchanges)

    return compares, exchanges


def partition(arr: list, lo: int, hi: int, compares: int, exchanges: int) -> (int, int, int):
    i = lo
    j = hi + 1
    v = arr[lo]

    while True:
        i += 1
        while arr[i] < v:
            compares += 1
            if i == hi:
                break
            i += 1

        j -= 1
        while v < arr[j]:
            compares += 1
            if j == lo:
                break
            j -= 1

        if i >= j:
            break

        exchange(arr, i, j)
        exchanges += 1

    exchange(arr, lo, j)
    exchanges += 1

    return j, compares, exchanges


def improved_quick_sort(arr: list) -> (int, int, int):
    compares = exchanges = 0  # Start counters

    stack = [0, len(arr) - 1]  # Start stack with the first and last value

    while len(stack) > 0:
        # Get the top of the stack in order of last and first element
        last = get_from_stack(stack)
        first = get_from_stack(stack)

        # Order partially the partition
        middle, middle_range, compares, exchanges = improved_quick_partition(arr, first, last, compares, exchanges)

        # Verify it has a new partition of left side to order
        if (middle - 1) > first:
            # Add to stack ever the last element after the first
            stack.append(first)
            stack.append(middle - 1)

        # Verify it has a new partition of right side to order
        if (middle + middle_range) < last:
            # Add to stack ever the last element after the first
            stack.append(middle + middle_range)
            stack.append(last)

    return arr, compares, exchanges


# Return the top element of a stack list
def get_from_stack(stack: list):
    top = stack[len(stack) - 1]
    del stack[len(stack) - 1]
    return top


# Select the mean between three elements in a list using their positions
def mean3(arr: list, first: int, last: int, middle: int) -> Any:
    first_value = arr[first]
    last_value = arr[last]
    middle_value = arr[middle]

    if first_value <= middle_value <= last_value or last_value <= middle_value <= first_value:
        return middle_value
    elif middle_value <= first_value <= last_value or last_value <= first_value <= middle_value:
        return first_value
    else:
        return last_value


def improved_quick_partition(arr: list, low: int, high: int, compares: int, exchanges: int) -> (int, int, int, int):
    # Uses the mean-3-way approach
    middle_value = mean3(arr, low, high, low + math.floor((high - low) / 2))

    # Start the sub-lists
    left = []
    right = []
    middle = []

    # Compare to re-order every elements it's necessary
    for i in arr[low:high + 1]:
        if i > middle_value:
            right.append(i)
        elif i < middle_value:
            left.append(i)
        else:
            middle.append(i)
        compares += 1
        exchanges += 1

    # Concatenate the results
    arr[low:high + 1] = left + middle + right
    exchanges += 1

    # Return first the middle value, after the middle range (to not re-order the same values), after the compares and
    # exchanges
    return low + len(left), len(middle), compares, exchanges


# Exchange two values of a list by their positions
def exchange(arr: list, i: int, j: int):
    # exchange two values of an array
    arr[i], arr[j] = arr[j], arr[i]


# Heapsort e funções auxiliares
def heap_sort(array: list) -> (list, int, int):
    compares = 0
    exchanges = 0
    heap_size = len(array)
    qtd_elementos = heap_size - 1

    compares, exchanges = build_heap(array, compares, exchanges)

    for i in range(qtd_elementos, 0, -1):
        compares += 1
        array[i], array[0] = array[0], array[i]  # troca
        heap_size = heap_size - 1
        compares, exchanges = heapify(array, 0, heap_size, compares, exchanges)

    return array, compares, exchanges


# igual a seguinte, mas faz o registro do log com base em operações anteriores e posteriores para que o heap_sort conte-as direito
def build_heap(array: list, compares: int, exchanges: int) -> (int, int):
    ultimo_pai = math.floor(len(array) / 2) - 1
    for indice in range(ultimo_pai, -1, -1):  # range entre [ultimo_pai e -1| (i.e., 0)
        compares, exchanges = heapify(array, indice, len(array), compares, exchanges)
    return compares, exchanges


def filho_e(elemento: int):
    return math.floor(elemento * 2 + 1)


def filho_d(elemento: int):
    return math.floor(elemento * 2 + 2)


def pai(elemento: int):
    return math.floor(elemento / 2)


# heapify: verifica se o elemento na posição passada é um heap e se não for transforma-o em um
# parâmetros: array, índice do elemento a heapificar, tamanho do heap, dicionário de logs
def heapify(array: list, elemento: int, heap_size: int, compares: int, exchanges: int) -> (int, int):
    maior = elemento  # O maior é inicializado como o elemento mãe
    filho_esq = filho_e(elemento)
    filho_dir = filho_d(elemento)

    # Verifica se o filho da esquerda, caso exista, é maior que o maior elemento atual
    if filho_esq < heap_size and array[maior] < array[filho_esq]:
        maior = filho_esq

    # Verifica se o filho da direita, caso exista, é maior que o maior elemento atual
    if filho_dir < heap_size and array[maior] < array[filho_dir]:
        maior = filho_dir

    compares += 2  # Atualiza o número de compareções baseado na comparação direita e esquerda

    # Troca o maior elemento se necessário (quando houver troca)
    if maior != elemento:
        array[elemento], array[maior] = array[maior], array[elemento]
        exchanges += 2  # Atualiza o número de trocas baseado na troca do novo maior elemento
        # Aplica o Heapify novamente no maior elemento.
        compares, exchanges = heapify(array, maior, heap_size, compares, exchanges)

    return compares, exchanges


def heap_get_max(heap: list) -> int:
    if len(heap) == 0:
        return -1

    return heap[0]


def heap_max(heap: list) -> (int, int, int):
    compares = 0
    exchanges = 0

    if len(heap) == 0:
        return -1

    max = heap_get_max(heap)

    heap[0] = heap[-1]
    del heap[-1]

    compares, exchanges = heapify(heap, 0, len(heap), compares, exchanges)

    return max, compares, exchanges


def heap_insert(heap: list, elemento: int) -> (int, int):
    compares = 0
    exchanges = 0
    index = len(heap)
    heap.append(elemento)

    while index != 0:
        p = pai(index)
        if heap[p] < heap[index]:
            heap[p], heap[index] = heap[index], heap[p]
            exchanges += 2

        compares += 1
        index = p

    return compares, exchanges


# Verify if a list is in desc or asc order
def is_sorted(arr: list) -> (int, bool):
    # select the compare function by arr initial order

    compare = smaller

    if len(arr) >= 2:
        if arr[0] > arr[1]:
            compare = bigger

        for i in range(1, len(arr)):
            if not compare(arr[i - 1], arr[i]):
                return i, False

    return -1, True


# Verify if a list is in desc or asc partial order
def is_partial_sorted(arr: list, init: int, end: int) -> (int, bool):
    # select the compare function by arr initial order

    compare = smaller

    if end - init + 1 >= 2:
        if arr[init] > arr[init + 1]:
            compare = bigger

        init += 1

        for i in range(init, end):
            if not compare(arr[i - 1], arr[i]):
                return i, False

    return -1, True


def smaller(val1: int, val2: int) -> bool:
    return val1 <= val2


def bigger(val1: int, val2: int) -> bool:
    return val1 >= val2


def merge_insertion_sort(arr: list) -> (list, int, int):
    compares = exchanges = 0  # Start counters

    last_item = len(arr) - 1

    cut = 14
    init = end = 0

    while end != last_item:
        end = min(init + cut, last_item)
        compares, exchanges = insertion_sort_aux(arr, init, end, compares, exchanges)
        init = end + 1

    while cut < last_item:
        init = 0
        middle = init + cut + 1

        while middle < last_item:
            end = min(init + cut*2 + 1, last_item)
            compares, exchanges = merge_insert_v2(arr, init, middle, end, compares, exchanges)

            init = end + 1
            middle = init + cut + 1

        cut = cut*2 + 1

    return arr, compares, exchanges


def insertion_sort_aux(arr: list, lo: int, hi: int, compares: int, exchanges: int) -> (int, int):
    for i in range(lo, hi + 1):
        j = i

        # exchange i element with the predecessor until find a smaller one
        while j > lo and arr[j] < arr[j - 1]:
            compares += 1  # sum compare
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            exchanges += 1
            j -= 1

    return  compares, exchanges


def merge_insert_v1(arr: list, init_list_1: int, init_list_2: int, end_list_2: int, compares: int, exchanges: int) \
        -> (list, int, int):

    aux = []
    counter_list_2 = init_list_2

    while init_list_1 < init_list_2 and counter_list_2 <= end_list_2:
        if arr[counter_list_2] < arr[init_list_1]:
            aux.append(arr[counter_list_2])
            counter_list_2 += 1
        else:
            aux.append(arr[init_list_1])
            init_list_1 += 1

        compares += 1
        exchanges += 1

    while init_list_1 < init_list_2:
        aux.append(arr[init_list_1])
        init_list_1 += 1
        exchanges += 1

    while counter_list_2 <= end_list_2:
        aux.append(arr[counter_list_2])
        counter_list_2 += 1
        exchanges += 1

    return aux, compares, exchanges


def merge_insert_v2(arr: list, init_list_1: int, init_list_2: int, end_list_2: int, compares: int, exchanges: int) \
        -> (int, int):

    temp = init_list_1
    aux = []
    mid = init_list_2
    print('init_1' + str(end_list_2))
    while init_list_1 < init_list_2 <= end_list_2:
        if len(aux) > 0:
            if init_list_1 < mid:
                aux.append(arr[init_list_1])

            if arr[init_list_2] < aux[0]:  # < is necessary for stability
                arr[init_list_1] = arr[init_list_2]
                init_list_2 += 1
            else:
                arr[init_list_1] = aux[0]
                del aux[0]

            exchanges += 1

        elif arr[init_list_2] < arr[init_list_1]:  # < is necessary for stability
            aux.append(arr[init_list_1])
            arr[init_list_1] = arr[init_list_2]
            init_list_2 += 1

            exchanges += 1

        init_list_1 += 1
        compares += 1

    print(aux)
    while len(aux) > 0:
        arr[init_list_1] = aux[0]
        del aux[0]
        init_list_1 += 1
        exchanges += 1

    teste, sorted = is_partial_sorted(arr, temp, end_list_2)

    print(temp)
    print(end_list_2)
    print(arr)
    print(teste)
    print(arr[teste])
    assert sorted, 'fail'

    return compares, exchanges
