import test_algorithm
import plot_data
import plot_theoretical


def main():
    # get data for both standard heapsort and bottom-up, for worst-case. best-case, average-case
    number_of_keys, time_data_standard, time_all_data_standard, time_data_btm_up, time_all_data_btm_up = test_algorithm.test_algorithm()

    # Plotting the cases for Standard heapsort and standard deviation
    plot_data.plot_data(number_of_keys, time_data_standard, "Standard")
    plot_data.standard_deviation(number_of_keys, time_data_standard, time_all_data_standard, "Standard")

    # plotting the cases for Bottom-up heapsort and standard deviation
    plot_data.plot_data(number_of_keys, time_data_btm_up, "Bottom up")
    plot_data.standard_deviation(number_of_keys, time_data_btm_up, time_all_data_btm_up, "Bottom up")

    # plot a comparison of Standard and Bottom up heapsort
    plot_data.compare_algorithms(number_of_keys, time_data_standard, time_data_btm_up)


if __name__ == "__main__":
    main()
