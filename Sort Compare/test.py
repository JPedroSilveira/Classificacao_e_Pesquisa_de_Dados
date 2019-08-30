from pandas.compat.numpy import function

import util
import sort
import data


#   Realize "repeat" tests with arrays of "size_min", "size_min + jump", ..., "size_max" in a list of sort functions
#   Plus: Display the log and the graphics
#       repeat: int, how many times a test of N size will be repeated
#       size_min: int, random array size of the initial test
#       size_max: int, random array size of the last test
#       jump: int, distance of arrays sizes that will be tested between the size_min and size_max
#       sort: list, list of dictionaries with:
#           function: function, the sort function
#           name: string, the function name
def test_battery(repeat: int, size_min: int, size_max: int, jump: int, sort_list: list):
    results = []

    for i in range(0, len(sort_list)):
        size = size_min

        while size <= size_max:

            result = test_sort_n_times(sort_list[i]['function'], sort_list[i]['name'], size, repeat)

            results.append(result)

            size += jump

    data.generate_analysis(results)


#   Realize "repeat" tests with arrays of N size in a sort function
#       repeat: int, how many times a test of N size will be repeated
#       size: int, random array size
#       sort_function: function, sort function
#       sort_name: string, name of the sort algorithm
def test_sort_n_times(sort_function: function, sort_name: str, size: int, repeat: int) -> dict:
    test_data = {'time': [], 'compare': [], 'exchange': []}

    for i in range(0, repeat):  # initialize the number of tests
        # test sort and get the results
        time, compare, exchange = test_sort(sort_function, sort_name, size)
        test_data['time'].append(time)
        test_data['compare'].append(compare)
        test_data['exchange'].append(exchange)

        # display info about execution
        print('Sort: %s - Size: %d - Time: %d - Finished at: %s' % (sort_name, size, i, util.get_data_time()))

    return {'algorithm': sort_name, 'type': 'R', 'size': size,
            'md_exchange': util.get_average(test_data['exchange']),
            'sd_exchange': util.get_std(test_data['exchange']),
            'md_compare': util.get_average(test_data['compare']),
            'sd_compare': util.get_std(test_data['compare']),
            'md_time': util.get_average(test_data['time']),
            'sd_time': util.get_std(test_data['time'])}


#   Realize a test with an array of N size in a sort function
#       size: int, random array size
#       sort_function: function, sort function
#       sort_name: string, name of the sort algorithm
def test_sort(sort_function: function, sort_name: str, size: int) -> (float, int, int):
    array = util.generate_random_int_arr(size)  # generate random array
    st_time = util.get_time()  # get init time

    sorted_arr, t_compare, t_exchange = sort_function(array)  # sort array

    f_time = util.get_time() - st_time

    assert sort.is_sorted(sorted_arr), '%s failed' % sort_name

    return f_time, t_compare, t_exchange
