import sort
import util


def main():
    times = 100000
    size = 10 ** 4

    selection_data = {'time': [], 'compare': [], 'exchange': []}
    insertion_data = {'time': [], 'compare': [], 'exchange': []}
    shell_data = {'time': [], 'compare': [], 'exchange': []}

    #  generate the first arrays to test
    selection_arr = util.generate_random_int_arr(size)
    insertion_arr = selection_arr[:]
    shell_arr = insertion_arr[:]

    for i in range(0, times):  # initialize the number of tests

        # perform selection sort
        st_time = util.get_time()
        t_compare, t_exchange = sort.selection_sort(selection_arr)

        # save results
        selection_data['time'].append(util.get_time() - st_time)
        selection_data['compare'].append(t_compare)
        selection_data['exchange'].append(t_exchange)

        # perform insertion sort
        st_time = util.get_time()
        t_compare, t_exchange = sort.insertion_sort(insertion_arr)

        # save results
        insertion_data['time'].append(util.get_time() - st_time)
        insertion_data['compare'].append(t_compare)
        insertion_data['exchange'].append(t_exchange)

        # perform shell sort
        st_time = util.get_time()
        t_compare, t_exchange = sort.shell_sort(shell_arr)

        # save results
        shell_data['time'].append(util.get_time() - st_time)
        shell_data['compare'].append(t_compare)
        shell_data['exchange'].append(t_exchange)

        # create new arrays
        selection_arr = util.generate_random_int_arr(size)
        insertion_arr = selection_arr[:]
        shell_arr = insertion_arr[:]

    data = []

    #  data of selection sort
    f_selection_data = {'algorithm': 'Selection Sort', 'type': 'R', 'size': size,
                        'md_exchange': util.get_average(selection_data['exchange']),
                        'sd_exchange': util.get_std(selection_data['exchange']),
                        'md_compare': util.get_average(selection_data['compare']),
                        'sd_compare': util.get_std(selection_data['compare']),
                        'md_time': util.get_average(selection_data['time']),
                        'sd_time': util.get_std(selection_data['time'])}

    data.append(f_selection_data)
    util.log(f_selection_data)

    #  data of insertion sort
    f_insertion_data = {'algorithm': 'Insertion Sort', 'type': 'R', 'size': size,
                        'md_exchange': util.get_average(insertion_data['exchange']),
                        'sd_exchange': util.get_std(insertion_data['exchange']),
                        'md_compare': util.get_average(insertion_data['compare']),
                        'sd_compare': util.get_std(insertion_data['compare']),
                        'md_time': util.get_average(insertion_data['time']),
                        'sd_time': util.get_std(insertion_data['time'])}

    data.append(f_insertion_data)
    util.log(f_insertion_data)

    # data of shell sort
    f_shell_data = {'algorithm': 'Shell Sort', 'type': 'R', 'size': size,
                    'md_exchange': util.get_average(shell_data['exchange']),
                    'sd_exchange': util.get_std(shell_data['exchange']),
                    'md_compare': util.get_average(shell_data['compare']),
                    'sd_compare': util.get_std(shell_data['compare']),
                    'md_time': util.get_average(shell_data['time']),
                    'sd_time': util.get_std(shell_data['time'])}

    data.append(f_shell_data)
    util.log(f_shell_data)

    util.show_and_save_data(data)


main()
