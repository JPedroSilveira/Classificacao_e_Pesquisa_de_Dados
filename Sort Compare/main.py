import sort
import test


def main():
    repeat = 10
    jump = 10000
    size_min = 1000
    size_max = 101000

    arr_type = 'R'

    sort_list = sort.get_sorts(['heap_sort'])

    test.test_battery(repeat, size_min, size_max, jump, sort_list, arr_type)

main()
