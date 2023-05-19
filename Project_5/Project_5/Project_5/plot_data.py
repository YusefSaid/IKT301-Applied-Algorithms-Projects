import matplotlib.pyplot as plt
import math


# plot a heapsort algorithm and its worst-case, best-case and average-case, in the same plot.
def plot_data(number_of_keys, time_data, type):
    plt.plot(number_of_keys, time_data['Random'], color="green", label="Average Case")  # Random
    plt.plot(number_of_keys, time_data['Ascending'], color="red", label="Worst Case")  # Ascending
    plt.plot(number_of_keys, time_data['Descending'], color="blue", label="Best Case")  # Descending

    plt.subplots_adjust(left=0.15)
    plt.title("Heapsort Algorithm - " + type)
    plt.xlabel("Number of Keys")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("Heapsort_Algorithm - " + type + ".png")
    plt.show()


# compare two algorithms by plotting them togethet, for best-case, worst-case, average-case
def compare_algorithms(number_of_keys, time_data_std, time_data_btm_up):
    # compare when keys are randomized
    compare_algorithms_plot(number_of_keys, time_data_std['Random'], time_data_btm_up['Random'], label="Average Case")

    # compare for ascending
    compare_algorithms_plot(number_of_keys, time_data_std['Ascending'], time_data_btm_up['Ascending'],
                            label="Worst Case")

    # compare for descending
    compare_algorithms_plot(number_of_keys, time_data_std['Descending'], time_data_btm_up['Descending'],
                            label="Best Case")


# plot the comparison of two algorithms and the chosen time complexity case.
def compare_algorithms_plot(number_of_keys, time_data_std, time_data_btm_up, label):
    plt.plot(number_of_keys, time_data_std, color="blue", label='Standard Heapsort')
    plt.plot(number_of_keys, time_data_btm_up, color="red", label='Bottom Up Heapsort')

    plt.subplots_adjust(left=0.15)
    plt.title("Heapsort Algorithm Comparison - " + label)
    plt.xlabel("Number of Keys")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("Heapsort_Algorithm_Comparison_" + label + ".png")
    plt.show()


# plot the standard deviation together with its corresponding graph.
def plot_standard_deviation(number_of_keys, time_data, std_dev_pos, std_dev_neg, col, label, type):
    plt.plot(number_of_keys, time_data, color=col, label='Data')
    plt.fill_between(number_of_keys, std_dev_neg, std_dev_pos, alpha=0.2)

    plt.subplots_adjust(left=0.15)
    plt.title("Heapsort Algorithm - " + type + ', ' + label + " - Standard Deviation")
    plt.xlabel("Number of Keys")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("Heapsort_Algorithm_" + type + ', ' + label + "_Standard_Deviation.png")
    plt.show()


# to making the plotting of standard deviation more generalized.
def standard_deviation(number_of_keys, time_data, time_all_data, type):
    # Random - average case
    std_dev_pos, std_dev_neg = calculate_standard_deviation(time_data['Random'], time_all_data['Random'])
    plot_standard_deviation(number_of_keys, time_data['Random'], std_dev_pos, std_dev_neg, "green", 'Average Case',
                            type)

    # Ascending - worst case
    std_dev_pos, std_dev_neg = calculate_standard_deviation(time_data['Ascending'], time_all_data['Ascending'])
    plot_standard_deviation(number_of_keys, time_data['Ascending'], std_dev_pos, std_dev_neg, "red", 'Worst Case', type)

    # Descending - best case
    std_dev_pos, std_dev_neg = calculate_standard_deviation(time_data['Descending'], time_all_data['Descending'])
    plot_standard_deviation(number_of_keys, time_data['Descending'], std_dev_pos, std_dev_neg, "blue", 'Best Case',
                            type)


# take all the data points and calculate their standard deviaton
# then calculate the standard deviation negative and positive.
# formula is:
# sqrt((sum(a measured value for a data point - average value for that datapoint) ** 2) / (number of data points - ))
def calculate_standard_deviation(time_data, time_all_data):
    std_dev_all_points = [None for i in range(len(time_all_data))]

    for i in range(len(time_all_data)):
        std_dev = 0
        for k in range(len(time_all_data[i])):
            std_dev += (time_all_data[i][k] - time_data[i]) ** 2
        std_dev = math.sqrt(std_dev / (len(time_all_data[i]) - 1))
        std_dev_all_points[i] = std_dev

    std_dev_pos = [i + j for i, j in zip(time_data, std_dev_all_points)]
    std_dev_neg = [i - j for i, j in zip(time_data, std_dev_all_points)]
    return std_dev_pos, std_dev_neg
