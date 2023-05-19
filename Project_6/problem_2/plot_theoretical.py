from matplotlib import pyplot as plt
import numpy as np

# plot theoretical graph
x_values = np.arange(0, 1000, 1)
y_values = (x_values ** 2) / 10_000  # divide by 10,000 so that formatting is easier.

plt.plot(x_values, y_values, color="green")

plt.title("Reduction Algorithm - Theoretical")
plt.xlabel("Number of literals")
plt.ylabel("Time Complexity")
plt.legend()
plt.savefig("reduction_algorithm_theoretical.png")
plt.show()
