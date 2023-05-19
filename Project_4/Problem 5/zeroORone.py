import quickSort

def solutionZeroORone(capacity,tasks):

    limit = int(capacity[0])
    solution = []

    # loaned my old quicksort from project 3, and adjusted it for high to low sort by profit/weight ratio of the
    # task list
    tasks = quickSort.sort(tasks,2)

    while limit > 0 and len(tasks)!=0:
        if limit - tasks[0][0] < 0:
            counter = 0
            adjusted = []
            while counter != len(tasks):
                if limit > tasks[counter][0]:
                    adjusted.append(tasks[counter])
                counter += 1
            tasks = adjusted

        else:
            limit -= tasks[0][0]
            solution.append(tasks[0])
            tasks.pop(0)

    return solution

def validateSolution(list,capacityStart):

    capacity = 0
    profit = 0

    for i in range(len(list)):
        capacity += list[i][0]
        profit += list[i][1]


    print("Current solution list capacity: ", capacity)
    print("Unutilized capacity: ", int(capacityStart)-capacity)
    print("Current solution list profit value: ", profit)
