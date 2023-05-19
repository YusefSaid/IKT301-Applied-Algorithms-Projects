#Problem 4:
#2. Count the number of visited and promising nodes in the search tree.


#Program to generate n-bit Gray codes
# We create a function def that will be assigned
# to generate for us all n bit Gray.
# The function will give us an output,
# this output will out Gray code. And prints the generated codes.


def grayCodeUtil(res, n, num):
    # base case when we run out of bits to process
    # we simply include it in gray code sequence.
    if (n == 0):
        res.append(num[0])
        return

    # ignore the bit.
    grayCodeUtil(res, n - 1, num)

    # invert the bit.
    num[0] = num[0] ^ (1 << (n - 1))
    grayCodeUtil(res, n - 1, num)


# Our function 'def grayCodes' will return the vector containing
# the gray code sequence of n bits.
def grayCodes(n):
    res = []

    # Our variable 'num' keeps track of the current gray code.
    # Num is therefor passed by reference.
    # And therefor can keep track of the current gray code.
    num = [0]
    grayCodeUtil(res, n, num)
    return res


# Driver Code
n = 3
code = grayCodes(n)
for i in range(len(code)):
    print(code[i])

