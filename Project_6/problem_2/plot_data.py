from matplotlib import pyplot as plt
import math


# plot the data
def plot_data(data, number_of_literals):
    plt.plot(number_of_literals, data["increasing_clauses"], color="blue", label="Increasing Clauses - Worst Case")
    plt.plot(number_of_literals, data["increasing_literals"], color="red", label="Increasing Literals per Clause - Best Case")

    plt.title("Reduction Algorithm - Empiric")
    plt.xlabel("Number of literals")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig("reduction_algorithm_empiric_data.png")
    plt.show()


# plot the std dev of our data
def plot_std_dev(data, all_data, number_of_literals):
    fig, axs = plt.subplots(2)
    fig.tight_layout()
    fig.suptitle("Reduction Algorithm - Standard Deviation")

    std_dev_pos, std_dev_neg = find_std_dev(data["increasing_clauses"], all_data["all_increasing_clauses"])
    axs[0].plot(number_of_literals, data["increasing_clauses"], color="blue", label="Increasing Clauses")
    axs[0].fill_between(number_of_literals, std_dev_neg, std_dev_pos, alpha=0.2)
    axs[0].set_title = "Increasing Clauses"
    axs[0].set_xlabel("Number of Literals")
    axs[0].set_ylabel("Time")
    axs[0].legend(loc="upper left")

    std_dev_pos, std_dev_neg = find_std_dev(data["increasing_literals"], all_data["all_increasing_literals"])
    axs[1].plot(number_of_literals, data["increasing_literals"], color="red", label="Increasing Literals per Clause")
    axs[1].fill_between(number_of_literals, std_dev_neg, std_dev_pos, alpha=0.2)
    axs[1].set_title = "Increasing Literals per Clause"
    axs[1].set_xlabel("Number of Literals")
    axs[1].set_ylabel("Time")
    axs[1].legend(loc="upper left")

    plt.subplots_adjust(left=0.135, top=0.93, bottom=0.1)
    plt.savefig("reduction_algorithm_empiric_data_std_dev.png")
    plt.show()


# algorithm to find the standard deviation
def find_std_dev(data, all_data):
    all_std_dev = []
    std_dev_pos, std_dev_neg = [], []

    # find standard deviation
    for i in range(len(data)):
        std_dev = 0
        for k in range(len(all_data[i])):
            std_dev += (all_data[i][k] - data[i]) ** 2
        std_dev = math.sqrt(std_dev / (len(all_data[i]) - 1))
        all_std_dev.append(std_dev)

    # subtract or add our std dev from/to our average result
    for i in range(len(data)):
        std_dev_pos.append(data[i] + all_std_dev[i])
        std_dev_neg.append(data[i] - all_std_dev[i])

    return std_dev_pos, std_dev_neg
