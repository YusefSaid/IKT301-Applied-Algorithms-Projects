import quickSort

def solutionFractional(capacity,tasks):

    limit = int(capacity[0])
    solution = []


    # loaned my old quicksort from project 3, and adjusted it for high to low sort by profit/weight ratio of the
    # task list
    tasks = quickSort.sort(tasks,2)

    while limit > 0:
        if limit - tasks[0][0] < 0:
            #remaining workload
            rw = limit/tasks[0][0]
            limit -= rw

            for i in range(len(tasks[0])-1):
                tasks[0][i]= rw* float(tasks[0][i])

            solution.append(tasks[0])
            return solution

        else:
            limit -= tasks[0][0]
            solution.append(tasks[0])
            tasks.pop(0)

def validateSolution(list):

    capacity = 0
    profit = 0

    for i in range(len(list)):
        capacity += list[i][0]
        profit += list[i][1]


    print("Current solution list capacity: ", capacity)
    print("Current solution list profit value: ", profit)

def printSolution(list):

    for i in range(len(list)):
        print(list[i])

    print("\nVisual representation of the solution list above")