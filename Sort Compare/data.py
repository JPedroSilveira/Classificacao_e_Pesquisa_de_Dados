import pandas
import matplotlib.pyplot as plt
import numpy
import dir


# Generate graphs and save a csv with the results of all tests
#   data: list, list with dictionaries with:
#       'algorithm': str, algorithm name
#       'type': str, 'type' of the test
#       'size': int, size of each tested array
#       'md_exchange': double, arithmetic median of exchanges
#       'sd_exchange': double, standard deviation of exchanges
#       'md_compare': double, arithmetic median of compares
#       'sd_compare': double, standard deviation of compares
#       'md_time': double, arithmetic median of time
#       'sd_time': double, standard deviation of time
def generate_analysis(data: list):
    # create paths to save the results
    path_compare_algorithms = dir.create_folder_on_root('compare algorithms by exchanges, compares and time')
    path_compare_algorithm_test_list_size = dir.create_folder_on_root('execution analysis of exchanges, compares and '
                                                                      'time changing test size')
    path_csv_folder = dir.create_folder_on_root('test results, complete csv')

    compare_algorithms_folder = dir.get_new_test_folder(path_compare_algorithms)
    compare_algorithm_by_test_list_size_folder = dir.get_new_test_folder(path_compare_algorithm_test_list_size)
    csv_folder = dir.get_new_test_folder(path_csv_folder)

    # generate a csv with all results
    generate_csv(data, csv_folder)

    # generate graphics comparing the algorithms
    list_by_size = get_by(data, 'size')

    for i in range(0, len(list_by_size)):
        generate_analysis_group_by_size(list_by_size[i]['content'], compare_algorithms_folder)

    # generate graphics comparing algorithm performance by list size
    list_by_algorithm = get_by(data, 'algorithm')

    for i in range(0, len(list_by_algorithm)):
        generate_analysis_group_by_algorithm(list_by_algorithm[i]['content'],
                                             compare_algorithm_by_test_list_size_folder)


# Generate a csv with the results of all tests
#   data: list, list with dictionaries with:
#       'algorithm': str, algorithm name
#       'type': str, 'type' of the test
#       'size': int, size of each tested array
#       'md_exchange': double, arithmetic median of exchanges
#       'sd_exchange': double, standard deviation of exchanges
#       'md_compare': double, arithmetic median of compares
#       'sd_compare': double, standard deviation of compares
#       'md_time': double, arithmetic median of time
#       'sd_time': double, standard deviation of time
#   path: str, path to save the results
def generate_csv(data: list, path: str):
    cols = ['algorithm', 'type', 'size', 'md_exchange', 'md_compare', 'md_time']

    df = pandas.DataFrame(data)
    df = df[cols]
    df.to_csv(path + '/test_results.csv')


# Generate graphs comparing speed, exchange and compare of all sorts
#   data: list, list with dictionaries with:
#       'algorithm': str, algorithm name
#       'type': str, 'type' of the test
#       'size': int, size of each tested array
#       'md_exchange': double, arithmetic median of exchanges
#       'sd_exchange': double, standard deviation of exchanges
#       'md_compare': double, arithmetic median of compares
#       'sd_compare': double, standard deviation of compares
#       'md_time': double, arithmetic median of time
#       'sd_time': double, standard deviation of time
#   path: str, path to save the results
def generate_analysis_group_by_size(data: list, path: str):
    values_time = []
    values_time_sd = []
    values_exchange = []
    values_exchange_sd = []
    values_compare = []
    values_compare_sd = []

    for i in range(0, len(data)):
        values_time.append(data[i]['md_time'] * 1000)
        values_time_sd.append(data[i]['sd_time'] * 1000)
        values_exchange.append(data[i]['md_exchange'])
        values_exchange_sd.append(data[i]['sd_exchange'])
        values_compare.append(data[i]['md_compare'])
        values_compare_sd.append(data[i]['sd_compare'])

    generate_graphic_group_by_size(data, 'Algorithm - Time average', 'Time (ms)', values_time, values_time_sd, path)

    generate_graphic_group_by_size(data, 'Algorithm - Exchanges average', 'Number of Exchanges', values_exchange,
                                   values_exchange_sd, path)

    generate_graphic_group_by_size(data, 'Algorithm - Compares average', 'Number of Compares', values_compare,
                                   values_compare_sd, path)


# Generate a graphic comparing a property of the sorts execution
# data: list, list with dictionaries with:
#       'algorithm': str, algorithm name
#       'type': str, 'type' of the test
#       'size': int, size of each tested array
#       'md_exchange': double, arithmetic median of exchanges
#       'sd_exchange': double, standard deviation of exchanges
#       'md_compare': double, arithmetic median of compares
#       'sd_compare': double, standard deviation of compares
#       'md_time': double, arithmetic median of time
#       'sd_time': double, standard deviation of time
# title: str, a title for the graphic
# label: str, a sub label for the graphic
# values: list, list with the number values to compare
# dps: list, list with the standard deviation of each data compared
# path: str, path to save the results
def generate_graphic_group_by_size(data: list, title: str, label: str, values: list, dps: list, path: str):
    # Plot
    names = []

    if len(data) > 0:
        size = data[0]['size']

    for i in range(0, len(data)):
        names.append(data[i]['algorithm'])

    fig, ax = plt.subplots()
    y_pos = numpy.arange(len(data))

    ax.barh(y_pos, values, xerr=dps, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel(label)
    ax.set_title(title + ', size: %d' % size)

    plt.savefig(path + '/' + title + ' - size ' + str(size) + '.png')
    plt.close(fig)


# Generate graphs comparing speed, exchange and compare of all sorts
#   data: list, list with dictionaries with:
#       'algorithm': str, algorithm name
#       'type': str, 'type' of the test
#       'size': int, size of each tested array
#       'md_exchange': double, arithmetic median of exchanges
#       'sd_exchange': double, standard deviation of exchanges
#       'md_compare': double, arithmetic median of compares
#       'sd_compare': double, standard deviation of compares
#       'md_time': double, arithmetic median of time
#       'sd_time': double, standard deviation of time
#   path: str, path to save the results
def generate_analysis_group_by_algorithm(data: list, path: str):
    max_size = 0
    size = [0]
    time = [0]
    exchange = [0]
    compare = [0]
    all_data = []

    if len(data):  # all data should be of the same algorithm
        name = data[0]['algorithm']  # get the name of the algorithm

    for i in range(0, len(data)):  # get values to generate the graphics
        time.append(data[i]['md_time'] * 1000)
        exchange.append(data[i]['md_exchange'])
        compare.append(data[i]['md_compare'])
        size.append(data[i]['size'])
        if data[i]['size'] > max_size:
            max_size = data[i]['size']

    # save the values in a defined dictionary
    time_data = {'title': 'Execution time', 'content': time}
    exchange_data = {'title': 'Exchange count', 'content': exchange}
    compare_data = {'title': 'Compare count', 'content': compare}

    # save all data in a vector for a general graphic
    all_data.append(time_data)
    all_data.append(exchange_data)
    all_data.append(compare_data)

    # generate time graphic
    generate_graphic_group_by_algorithm('%s - Time average by test size' % name, 'Time (ms)', max_size,
                                        [time_data], size, path)

    # generate exchange graphic
    generate_graphic_group_by_algorithm('%s - Exchanges average by test size' % name, 'Number of Exchanges', max_size,
                                        [exchange_data], size, path)

    # generate compare graphic
    generate_graphic_group_by_algorithm('%s - Compares average by test size' % name, 'Number of Compares', max_size,
                                        [compare_data], size, path)

    # generate a general graphic
    generate_graphic_group_by_algorithm('%s - Exchange, time and compare average by test size' % name,
                                        'Number of compares, exchanges and time(ms)', max_size, all_data, size,
                                        path)


# Generate a graphic comparing n properties of a sort execution by ordered array size
# data: list, list with dictionaries with:
#       'algorithm': str, algorithm name
#       'type': str, 'type' of the test
#       'size': int, size of each tested array
#       'md_exchange': double, arithmetic median of exchanges
#       'sd_exchange': double, standard deviation of exchanges
#       'md_compare': double, arithmetic median of compares
#       'sd_compare': double, standard deviation of compares
#       'md_time': double, arithmetic median of time
#       'sd_time': double, standard deviation of time
# title: str, a title for the graphic
# label: str, a sub label for the graphic
# max_size: int, the size of the biggest test
# data: list, list with dictionaries with
#   'title': the data title
#   'content': the data list
# size: list, list with the sizes to compare
# path: str, path to save the results
def generate_graphic_group_by_algorithm(title: str, label: str, max_size: int, data: list, size: list,
                                        path: str):
    fig, ax = plt.subplots()

    len_data = len(data)

    for i in range(0, len_data):
        line, = ax.plot(size, data[i]['content'])
        line.set_label(data[i]['title'])

    ax.legend(loc='upper right', shadow=True)
    ax.set_xlim(0, max_size)
    ax.set_xlabel('Size')
    ax.set_ylabel(label)
    ax.set_title(title)
    ax.grid(True)

    plt.savefig(path + '/' + title + '.png')
    plt.close(fig)


# Return a list of dictionaries in which each dictionary represent one group of the dic_id data
#   data: list, list with dictionaries with:
#       'algorithm': str, algorithm name
#       'type': str, 'type' of the test
#       'size': int, size of each tested array
#       'md_exchange': double, arithmetic median of exchanges
#       'sd_exchange': double, standard deviation of exchanges
#       'md_compare': double, arithmetic median of compares
#       'sd_compare': double, standard deviation of compares
#       'md_time': double, arithmetic median of time
#       'sd_time': double, standard deviation of time
#   dic_id: str, id of the dic data to group by
#   return:
#       list of dictionaries with:
#           '[dic_id]': the column of group by
#           'content': list, list with each item of the group
def get_by(data: list, dic_id: str) -> list:
    result_list = []
    found_list = []

    for i in range(0, len(data)):
        if data[i][dic_id] not in found_list:
            found_list.append(data[i][dic_id])
            item = {dic_id: data[i][dic_id], 'content': []}
            item['content'].append(data[i])
            result_list.append(item)
        else:
            for x in range(0, len(result_list)):
                if result_list[x][dic_id] == data[i][dic_id]:
                    result_list[x]['content'].append(data[i])
                    break

    return result_list
