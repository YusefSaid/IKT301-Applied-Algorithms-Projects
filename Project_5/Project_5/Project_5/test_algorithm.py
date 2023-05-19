import random
import heap_sort_standard
import heap_sort_bottom_up
import time
import files


# testing both algorithms.
def test_algorithm():
    # the number of times each algorithm and their cases are retested to reduce inaccuracy
    number_of_retests = 3
    # n, the number of data points
    n = 50
    # step is the difference in number of keys between each data point.
    step = 1
    # maximum number of keys
    max_length = step * n

    number_of_keys = [i for i in range(step, max_length + step, step)]

    # accumulated time of the Standard heapsort algorithm for each case
    time_data_random_standard = [0 for i in range(int(max_length / step))]
    time_data_ascending_standard = [0 for i in range(int(max_length / step))]
    time_data_descending_standard = [0 for i in range(int(max_length / step))]

    # all the time data, since we want to find standard deviation for every data point
    time_all_data_random_standard = [[0 for i in range(number_of_retests)] for j in range(n)]
    time_all_data_ascending_standard = [[0 for i in range(number_of_retests)] for j in range(n)]
    time_all_data_descending_standard = [[0 for i in range(number_of_retests)] for j in range(n)]

    #  accumulated time of the Bottom up heapsort algorithm for each case
    time_data_random_btm_up = [0 for i in range(int(max_length / step))]
    time_data_ascending_btm_up = [0 for i in range(int(max_length / step))]
    time_data_descending_btm_up = [0 for i in range(int(max_length / step))]

    # all the time data, since we want to find standard deviation for every data point
    time_all_data_random_btm_up = [[0 for i in range(number_of_retests)] for j in range(n)]
    time_all_data_ascending_btm_up = [[0 for i in range(number_of_retests)] for j in range(n)]
    time_all_data_descending_btm_up = [[0 for i in range(number_of_retests)] for j in range(n)]

    for k in range(number_of_retests):
        print(k)
        for i in range(step, max_length + step, step):
            # key values in random order
            keys = create_test_set_randomized(n=i, max_value=i)

            # testing average case standard algorithm
            time_data = test_standard(keys)
            time_data_random_standard[int(i / step) - 1] += time_data
            time_all_data_random_standard[int(i / step) - 1][k] = time_data

            # testing average case bottom up
            time_data = test_bottom_up(keys)
            time_data_random_btm_up[int(i / step) - 1] += time_data
            time_all_data_random_btm_up[int(i / step) - 1][k] = time_data

            # key values in ascending order
            keys = create_test_set_ascending(n=i)

            # worst case Standard algorithm
            time_data = test_standard(keys)
            time_data_ascending_standard[int(i / step) - 1] += time_data
            time_all_data_ascending_standard[int(i / step) - 1][k] = time_data

            # worst case Bottom up algorithm
            time_data = test_bottom_up(keys)
            time_data_ascending_btm_up[int(i / step) - 1] += time_data
            time_all_data_ascending_btm_up[int(i / step) - 1][k] = time_data

            # key values in descending order
            keys = create_test_set_descending(n=i)

            # best case Standard algorithm
            time_data = test_standard(keys)
            time_data_descending_standard[int(i / step) - 1] += time_data
            time_all_data_descending_standard[int(i / step) - 1][k] = time_data

            # best case Bottom up algorithm
            time_data = test_bottom_up(keys)
            time_data_descending_btm_up[int(i / step) - 1] += time_data
            time_all_data_descending_btm_up[int(i / step) - 1][k] = time_data

    # get the average time for the retests
    for i in range(len(number_of_keys)):
        # Standard
        time_data_random_standard[i] = time_data_random_standard[i] / number_of_retests
        time_data_ascending_standard[i] = time_data_ascending_standard[i] / number_of_retests
        time_data_descending_standard[i] = time_data_descending_standard[i] / number_of_retests
        # Bottom up
        time_data_random_btm_up[i] = time_data_random_btm_up[i] / number_of_retests
        time_data_ascending_btm_up[i] = time_data_ascending_btm_up[i] / number_of_retests
        time_data_descending_btm_up[i] = time_data_descending_btm_up[i] / number_of_retests

    # return all the data, but better ordered in dictionaries.
    return number_of_keys, \
           {'Random': time_data_random_standard,
            'Ascending': time_data_ascending_standard,
            'Descending': time_data_descending_standard}, \
           {'Random': time_all_data_random_standard,
            'Ascending': time_all_data_ascending_standard,
            'Descending': time_all_data_descending_standard}, \
           {'Random': time_data_random_btm_up,
            'Ascending': time_data_ascending_btm_up,
            'Descending': time_data_descending_btm_up}, \
           {'Random': time_all_data_random_btm_up,
            'Ascending': time_all_data_ascending_btm_up,
            'Descending': time_all_data_descending_btm_up}


# returns the time for the standard heapsort to complete
def test_standard(keys):
    a = time.time()
    heap = heap_sort_standard.Heap()
    keys_sorted = heap.heap_sort(keys)
    print(keys_sorted)
    b = time.time()
    time_data = b - a

    return time_data


# returns the time for the bottom-up heapsort to complete
def test_bottom_up(keys):
    a = time.time()
    heap_sort_bottom_up.heapsort(keys)
    b = time.time()
    time_data = b - a

    return time_data


# generate keys in randomized order
def create_test_set_randomized(n, max_value):
    keys = []
    for i in range(n):
        keys.append(random.randint(0, max_value - 1))
    return keys


# generate keys in ascending order
def create_test_set_ascending(n):
    keys = []
    for i in range(n):
        keys.append(i)
    return keys


# generate keys in descending order.
def create_test_set_descending(n):
    keys = []
    for i in range(n - 1, -1, -1):
        keys.append(i)
    return keys
