import sort
import test


def main():
    repeat = 50
    jump = 200000
    size_min = 100000
    size_max = 1000000

    sort_list = sort.get_sorts(['merge_sort', 'quick_sort', 'improved_quick_sort'])

    test.test_battery(repeat, size_min, size_max, jump, sort_list)


main()
