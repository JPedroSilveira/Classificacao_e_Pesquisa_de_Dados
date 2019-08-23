import sort
import util
import datetime


def main():
    times = 10
    size = 4
    jump = 2
    size_i = 2
    count = 0

    selection_data = {'time': [], 'compare': [], 'exchange': []}
    insertion_data = {'time': [], 'compare': [], 'exchange': []}
    binary_insertion_data = {'time': [], 'compare': [], 'exchange': []}
    shell_data = {'time': [], 'compare': [], 'exchange': []}

    data = [None] * size

    for i in range(0, size):
        data[i] = []

    while size_i <= size:

        #  generate the first arrays to test
        selection_arr = util.generate_random_int_arr(10 ** size_i)
        insertion_arr = selection_arr[:]
        binary_insertion_arr = insertion_arr[:]
        shell_arr = binary_insertion_arr[:]

        for i in range(0, times):  # initialize the number of tests

            print('Time: %d - Hour: %s' % (i, datetime.datetime.now()))  # display the iterator of the array

            # perform selection sort
            st_time = util.get_time()
            t_compare, t_exchange = sort.selection_sort(selection_arr)

            assert sort.isSorted(selection_arr), 'Selection Sort failed'

            # save results
            selection_data['time'].append(util.get_time() - st_time)
            selection_data['compare'].append(t_compare)
            selection_data['exchange'].append(t_exchange)

            # perform insertion sort
            st_time = util.get_time()
            t_compare, t_exchange = sort.insertion_sort(insertion_arr)

            assert sort.isSorted(insertion_arr), 'Insertion Sort failed'

            # save results
            insertion_data['time'].append(util.get_time() - st_time)
            insertion_data['compare'].append(t_compare)
            insertion_data['exchange'].append(t_exchange)

            # perform binary insertion sort
            st_time = util.get_time()
            binary_insertion_arr, t_compare, t_exchange = sort.binary_insertion_sort(binary_insertion_arr)

            assert sort.isSorted(binary_insertion_arr), 'Binary Insertion Sort failed'

            # save results
            binary_insertion_data['time'].append(util.get_time() - st_time)
            binary_insertion_data['compare'].append(t_compare)
            binary_insertion_data['exchange'].append(t_exchange)

            # perform shell sort
            st_time = util.get_time()
            t_compare, t_exchange = sort.shell_sort(shell_arr)

            assert sort.isSorted(shell_arr), 'Shell Sort failed'

            # save results
            shell_data['time'].append(util.get_time() - st_time)
            shell_data['compare'].append(t_compare)
            shell_data['exchange'].append(t_exchange)

            # create new arrays
            selection_arr = util.generate_random_int_arr(10 ** size_i)
            insertion_arr = selection_arr[:]
            binary_insertion_arr = insertion_arr[:]
            shell_arr = binary_insertion_arr[:]

        #  data of selection sort
        f_selection_data = {'algorithm': 'Selection Sort', 'type': 'R', 'size': 10 ** size_i,
                            'md_exchange': util.get_average(selection_data['exchange']),
                            'sd_exchange': util.get_std(selection_data['exchange']),
                            'md_compare': util.get_average(selection_data['compare']),
                            'sd_compare': util.get_std(selection_data['compare']),
                            'md_time': util.get_average(selection_data['time']),
                            'sd_time': util.get_std(selection_data['time'])}

        data[count].append(f_selection_data)
        util.log(f_selection_data)

        #  data of insertion sort
        f_insertion_data = {'algorithm': 'Insertion Sort', 'type': 'R', 'size': 10 ** size_i,
                            'md_exchange': util.get_average(insertion_data['exchange']),
                            'sd_exchange': util.get_std(insertion_data['exchange']),
                            'md_compare': util.get_average(insertion_data['compare']),
                            'sd_compare': util.get_std(insertion_data['compare']),
                            'md_time': util.get_average(insertion_data['time']),
                            'sd_time': util.get_std(insertion_data['time'])}

        data[count].append(f_insertion_data)
        util.log(f_insertion_data)

        #  data of binary insertion sort
        f_binary_insertion_data = {'algorithm': 'Binary Insertion Sort', 'type': 'R', 'size': 10 ** size_i,
                                   'md_exchange': util.get_average(binary_insertion_data['exchange']),
                                   'sd_exchange': util.get_std(binary_insertion_data['exchange']),
                                   'md_compare': util.get_average(binary_insertion_data['compare']),
                                   'sd_compare': util.get_std(binary_insertion_data['compare']),
                                   'md_time': util.get_average(binary_insertion_data['time']),
                                   'sd_time': util.get_std(binary_insertion_data['time'])}

        data[count].append(f_binary_insertion_data)
        util.log(f_binary_insertion_data)

        # data of shell sort
        f_shell_data = {'algorithm': 'Shell Sort', 'type': 'R', 'size': 10 ** size_i,
                        'md_exchange': util.get_average(shell_data['exchange']),
                        'sd_exchange': util.get_std(shell_data['exchange']),
                        'md_compare': util.get_average(shell_data['compare']),
                        'sd_compare': util.get_std(shell_data['compare']),
                        'md_time': util.get_average(shell_data['time']),
                        'sd_time': util.get_std(shell_data['time'])}

        data[count].append(f_shell_data)
        util.log(f_shell_data)

        size_i += jump
        count += 1

    util.show_and_save_data(data)


main()
