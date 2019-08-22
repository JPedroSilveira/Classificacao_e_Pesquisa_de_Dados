def shell_sort(arr: list) -> (int, int):
    # count the number of exchanges and compares
    compares = 0
    exchanges = 0

    n = len(arr)  # save the length of the array
    h = 1  # starts h

    while h < (n/3):
        h = 3*h + 1  # 1, 4, 13, 40, 121, ... Set the h value by the array length

    while h >= 1:  # h-sort the array
        i = h  # start i with h value
        while i < n:  # insert arr[i] among a[i-h], a[i-2*h], a[i-3*h], ...
            j = i  # start j with i value
            while j >= h and arr[j] < arr[j - h]:
                exchanges += 1  # increase the exchange count value
                compares += 1   # increase the compare count value
                exchange(arr, j, j - h)
                j -= h
            i += 1
        h = int(h/3)

    return compares, exchanges


def insertion_sort(arr: list) -> (int, int):
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

    return compares, exchanges


def selection_sort(arr: list) -> int:
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

    return compares, exchanges


def exchange(arr: list, i: int, j: int):
    # exchange two values of an array
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
