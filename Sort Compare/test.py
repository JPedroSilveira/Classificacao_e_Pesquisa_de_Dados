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
#       arr_type: string, type of array, random(R), repeated(E), desc(D).
def test_battery(repeat: int, size_min: int, size_max: int, jump: int, sort_list: list, arr_type: str):
    results = []

    for i in range(0, len(sort_list)):
        size = size_min

        while size <= size_max:

            result = test_sort_n_times(sort_list[i]['function'], sort_list[i]['name'], size, repeat, arr_type)

            results.append(result)

            size += jump

    data.generate_analysis(results)


#   Realize "repeat" tests with arrays of N size in a sort function
#       repeat: int, how many times a test of N size will be repeated
#       size: int, random array size
#       sort_function: function, sort function
#       sort_name: string, name of the sort algorithm
#       arr_type: string, type of array, random(R), repeated(E), desc(D).
def test_sort_n_times(sort_function: function, sort_name: str, size: int, repeat: int, arr_type: str) -> dict:
    test_data = {'time': [], 'compare': [], 'exchange': []}

    for i in range(0, repeat):  # initialize the number of tests
        # test sort and get the results
        time, compare, exchange = test_sort(sort_function, sort_name, size, arr_type)
        test_data['time'].append(time)
        test_data['compare'].append(compare)
        test_data['exchange'].append(exchange)

        # display info about execution
        print('Sort: %s - Size: %d - Time: %d - Finished at: %s' % (sort_name, size, i, util.get_data_time()))

    return {'algorithm': sort_name, 'type': arr_type, 'size': size,
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
#       arr_type: string, type of array, random(R), repeated(E), desc(D).
def test_sort(sort_function: function, sort_name: str, size: int, arr_type: str) -> (float, int, int):
    if arr_type == 'R':
        array = util.generate_random_int_arr(size)  # generate random array
    elif arr_type == 'E':
        array = util.generate_equal_int_arr(size)  # generate a array with only one element repeated
    elif arr_type == 'D':
        array = util.generate_desc_int_arr(size)  # generate a array in desc order

    st_time = util.get_time()  # get init time

    sorted_arr, t_compare, t_exchange = sort_function(array)  # sort array

    f_time = util.get_time() - st_time

    index, is_sorted = sort.is_sorted(sorted_arr)

    if not is_sorted:
        print(sorted_arr)

    assert is_sorted, 'failed with ' + sort_name + ' in index ' + str(index)

    return f_time, t_compare, t_exchange
