import numpy as np
from copy import deepcopy

# Problem 4
# n-bit gray codes

# Function to convert
# decimal to binary

L1 = []  # global variable to use


def decimalToBinaryNumber(x, n):
    global L1
    list = []
    binaryNumber = [0] * x
    i = 0
    while (x > 0):
        binaryNumber[i] = x % 2
        x = x // 2
        i += 1

    # leftmost digits are
    # filled with 0
    for j in range(0, n - i):
        list.append(0)  # append to list which is then appended to the global list L1
        # print('0', end="")

    for j in range(i - 1, -1, -1):
        list.append(binaryNumber[j])
        # print(binaryNumber[j], end="")

    L1.append(list)


# Function to generate
# gray code
def generateGrayarr(n):
    N = 1 << n
    for i in range(N):
        # generate gray code of
        # corresponding binary
        # number of integer i.
        x = i ^ (i >> 1)
        # printing gray code
        decimalToBinaryNumber(x, n)
        # print()


def greedy_algorithm():
    global L1  # take the global variable and make it available in this function
    L2 = deepcopy(L1[::-1])  # create L2 which is the reverse of L1
    list_1 = []
    list_2 = []
    for i in range(len(L1)):
        L1[i].insert(0, 0)  # insert 0 infront of each gray code in L1  eg 10 becomes 010
        L2[i].insert(0, 1)  # insert 1 infront of each gray code in L2 eg 10 becomes 110

        list_1.append("".join(map(str, (L1[i]))))  # create a string of each gray code eg [0, 1, 1] becomes ['011']
        list_2.append("".join(map(str, (L2[i]))))  # create a string of each gray code eg [0, 1, 1] becomes ['011']

    list = list_1 + list_2  # concatenate lists
    for item in list:  # print list
        print(item)


# Driver code
if __name__ == '__main__':
    n = 3
    generateGrayarr(n - 1)
    greedy_algorithm()
