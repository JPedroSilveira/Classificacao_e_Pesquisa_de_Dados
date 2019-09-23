import sort
import test


def main():

    repeat = 30
    jump = 10000
    size_min = 10000
    size_max = 100000

    arr_type = 'R'

    sort_list = sort.get_sorts(['heap_sort', 'merge_sort', 'quick_sort'])

    test.test_battery(repeat, size_min, size_max, jump, sort_list, arr_type)

    '''
    arr = util.generate_random_int_arr(10000)
    compares = 0
    exchanges = 0
    arr, compares, exchanges = sort.merge_insertion_sort(arr)

    print(sort.is_sorted(arr))
    '''


main()
