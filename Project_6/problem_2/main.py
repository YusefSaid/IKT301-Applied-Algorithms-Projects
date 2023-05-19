import test_algorithm
import plot_data
import reduction_algorithm


def main():
    # an example to show that the algorithm works
    reduction_algorithm.logic_example()

    # test the algorithm
    data, all_data, number_of_literals = test_algorithm.test_algorithm()

    # plot our data.
    plot_data.plot_data(data, number_of_literals)
    plot_data.plot_std_dev(data, all_data, number_of_literals)


if __name__ == "__main__":
    main()
