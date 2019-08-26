import math

from pandas.compat.numpy import function


def get_sort_name(sort_id: str) -> str:
    dic = {'shell_sort': 'Shell Sort', 'selection_sort': 'Selection Sort',
           'insertion_sort': 'Insertion Sort', 'binary_insertion_sort': 'Binary Search Sort'}
    return dic[sort_id]


def get_sort_function(sort_id: str) -> function:
    dic = {'shell_sort': shell_sort, 'selection_sort': selection_sort,
           'insertion_sort': insertion_sort, 'binary_insertion_sort': binary_insertion_sort}
    return dic[sort_id]


def get_shell_sort_id() -> str:
    return 'shell_sort'


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


def get_selection_sort_id() -> str:
    return 'selection_sort'


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


def get_insertion_sort_id() -> str:
    return 'insertion_sort'


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


def get_binary_insertion_sort_id() -> str:
    return 'binary_insertion_sort_id'


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


def exchange(arr: list, i: int, j: int):
    # exchange two values of an array
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


def is_sorted(arr: list) -> bool:
    # select the compare function by arr initial order

    compare = smaller

    if arr[0] > arr[1]:
        compare = bigger

    for i in range(1, len(arr)):
        if not compare(arr[i - 1], arr[i]):
            return False

    return True


def smaller(val1: int, val2: int) -> bool:
    return val1 <= val2


def bigger(val1: int, val2: int) -> bool:
    return val1 >= val2
