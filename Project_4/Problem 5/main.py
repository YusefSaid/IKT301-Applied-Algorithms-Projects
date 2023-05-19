import fractional,zeroORone


def readData():
    tasks =[]

    with open("p08_c.txt") as f:
        capacity = f.read().splitlines()
    f.close()

    with open("p08_p.txt") as f:
        profit = f.read().splitlines()
    f.close()

    with open("p08_w.txt") as f:
        weight = f.read().splitlines()
    f.close()

    for i in range(len(weight)):
        temp = [int(weight[i]), int(profit[i]), round(int(profit[i])/int(weight[i]),4)]
        tasks.append(temp)


    return capacity,tasks

def main():
    capacity,tasks = readData()

    x = input("Run for fractional (1) or 0/1 (2) solution? ")

    if x == '1':
        solution = fractional.solutionFractional(capacity, tasks)
        fractional.printSolution(solution)
        print("List limit capacity: ", capacity[0])
        fractional.validateSolution(solution)
    elif x == '2':
        solution = zeroORone.solutionZeroORone(capacity, tasks)
        fractional.printSolution(solution)
        print("List limit capacity: ", capacity[0])
        zeroORone.validateSolution(solution,capacity[0])

    else:
        print("Wrong input")





if __name__ == '__main__':
    main()


