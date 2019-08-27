import sort
import test


def main():
    repeat = 100
    jump = 1000
    size_min = 1
    size_max = size_min + (10 ** 7)

    '''
    sort_list = [{'function': sort.get_sort_function('insertion_sort'),
                  'name': sort.get_sort_name('insertion_sort')},
                 {'function': sort.get_sort_function('selection_sort'),
                  'name': sort.get_sort_name('selection_sort')},
                 {'function': sort.get_sort_function('shell_sort'),
                  'name': sort.get_sort_name('shell_sort')},
                 {'function': sort.get_sort_function('binary_insertion_sort'),
                  'name': sort.get_sort_name('binary_insertion_sort')},
                 {'function': sort.get_sort_function('merge_sort'),
                  'name': sort.get_sort_name('merge_sort')},
                 {'function': sort.get_sort_function('quick_sort'),
                  'name': sort.get_sort_name('quick_sort')}]
    '''

    sort_list = [{'function': sort.get_sort_function('merge_sort'),
                  'name': sort.get_sort_name('merge_sort')},
                 {'function': sort.get_sort_function('quick_sort'),
                  'name': sort.get_sort_name('quick_sort')}]

    test.test_battery(repeat, size_min, size_max, jump, sort_list)


main()
