#Problem 4:
#1. Implement a backtracking solution


#Program to generate n-bit Gray codes
# We create a function def that will be assigned
# to generate for us all n bit Gray.
# The function will give us an output,
# this output will out Gray code. And prints the generated codes.

def generateGrayarray(n):

    # Base case:
    # We set a condition for our n bit.
    # if 'n' is smaller or equal to 0.
    if (n <= 0):
        return

    # We create a variable named 'array'
    # This variable will store all generated codes.
    array = list()

    # To begin with, we use one-bit pattern.
    array.append("0")
    array.append("1")

    # We now need to create a iteration which will be a process of a repeating steps.
    # And for every iteration of this loop. There will be generated.
    # We will therefor add a variable x which will define how many times it will be generated.
    # So we decide to say that our variable x will generate 2 times Gray code from the previousely generated x codes.
    x = 2
    z = 0
    while (True):

        if x >= 1 << n:
            break



        # Here we enter the latest or previous generate code
        # This happens again in 'array[]', but in reversed order.
        # There is double number of gray code generated in 'Nor array[]'
        for z in range(x - 1, -1, -1):
            array.append(array[z])

        # This 'for' loop will append 0 to the first half.
        for z in range(x):
            array[z] = "0" + array[z]

        # This 'for' loop will append 1 to the second half.
        for z in range(x, 2 * x):
            array[z] = "1" + array[z]
        x = x << 1

    # This 'for' loop will print out the content of 'array[]'.
    for x in range(len(array)):
        print(array[x])

# Our 'generateGrayarray' will generate our 'n'.
# And that will generate 'n' = 3 bit gray code.
generateGrayarray(3)

