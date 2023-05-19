import matplotlib.pyplot as plt
import math
import numpy as np


# plot the theoretical heapsort time complexity for both 20 and 20,000 keys
def plot_theoretical(n, type, best, avg, worst):
    # step is the number of keys difference between each list of kets
    step = 1
    # the maximum number of keys
    max_length = step * n

    x_values = np.arange(1, max_length, step)
    y_values_best_case = best * x_values * np.log(x_values)
    y_values_worst_case = worst * x_values * np.log(x_values)
    y_values_avg_case = avg * x_values * np.log(x_values)

    plt.plot(x_values, y_values_best_case, color="blue", label="Best Case")
    plt.plot(x_values, y_values_worst_case, color="red", label="Worst Case")
    plt.plot(x_values, y_values_avg_case, color="green", label="Average Case")

    plt.title(type + " Heapsort Algorithm - Theoretical, " + str(n) + " keys")
    plt.xlabel("Number of Keys")
    plt.ylabel("Time Complexity")
    plt.legend()
    plt.savefig("Theoretical_Heapsort_Algorithm_" + type + '_' + str(n) + ".png")

    plt.show()


# plot for standard heapsort
plot_theoretical(n=20, type="standard", best=1, avg=1.5, worst=2)
plot_theoretical(n=20_000, type="standard", best=1, avg=1.5, worst=2)

# plot for Bottom up heapsort.
plot_theoretical(n=20, type="Bottom-Up", best=1, avg=1.25, worst=1.5)
plot_theoretical(n=20_000, type="Bottom-Up", best=1, avg=1.25, worst=1.5)
