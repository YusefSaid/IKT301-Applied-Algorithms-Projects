from random import randint

# variables for comparison in exercise 2.2
comparison = 0
comparisonForSimplified = 0

# fetches index for lat parameter in list, only for 3.1 and 3.2, can be disregarded
def fetchIndex(list):
    for i in range(len(list[0])):
        if list[0][i] == "lat":
            return i


def quickSortOne(curList, indexIn):
    global comparison

    #Begin sorting the list, the lenght of which is not 1 or less
    #Create two list for sorting, for lower value than pivot or higher
    #Fetch value for pivot from list
    if len(curList) > 1:
        splitLow, splitHigh = [], []
        pivotIndex = randint(0, len(curList) - 1)
        pivotIndexValue = curList[pivotIndex][indexIn]
        counter=0

        #Sort the element list until it is empty
        #Sorting happens with 1 decimal precision

        while curList:
            comparison += 1
            if float(curList[counter][indexIn]) <= float(pivotIndexValue):
                splitLow.append(curList[counter])
                curList.pop(0)
            else:
                splitHigh.append(curList[counter])
                curList.pop(0)

        #This little code piece provides a bandage solution to recursion depth issue with this project
        #It does a small check between highest element of highsplit and lowest element of lowsplit
        #If the difference is less than 0.5, consider the list sorted, do not initiate another recursion
        #0.5 difference is the smallest number I could get to with code running 4/5 times with consistent data output
        dif = 2
        if len(splitLow) != 0 and len(splitHigh) != 0:
            dif = float(splitHigh[-1][indexIn]) - float(splitLow[0][indexIn])

        if dif <= 1:
            return splitLow + splitHigh

        else:
            #Attempt at quickening sorting process, begins running recursive sort one the list containing lowest number of
            #elements first
                if len(splitLow) < len(splitHigh):
                    A = quickSortOne(splitLow, indexIn)
                    B = quickSortOne(splitHigh, indexIn)
                    return A + B

                else:
                    B = quickSortOne(splitHigh, indexIn)
                    A = quickSortOne(splitLow, indexIn)
                    return A + B

    #return a list if it contains no or just one element
    else:
        return curList


#Simplified version of script adjusted for smaller lists
def quickSortSimplified(curList, indexIn):
    global comparisonForSimplified

    #Begin sorting the list, the lenght of which is not 1 or less
    #Create two list for sorting, for lower value than pivot or higher
    #Fetch value for pivot from list
    if len(curList) > 1:
        splitLow, splitHigh = [], []
        pivotIndex = randint(0, len(curList) - 1)
        pivotIndexValue = curList[pivotIndex][indexIn]
        counter=0

        #Sort the element list until it is empty
        #Sorting happens with 1 decimal precision

        while curList:
            comparisonForSimplified += 1
            x,y = float(curList[counter][indexIn]),float(pivotIndexValue)

            if x <= y:
                splitLow.append(curList[counter])
                curList.pop(0)
            else:
                splitHigh.append(curList[counter])
                curList.pop(0)

        #Attempt at quickening sorting process, begins running recursive sort one the list containing lowest number of
        #elements first
        if len(splitLow) < len(splitHigh):
            A = quickSortSimplified(splitLow, indexIn)
            B = quickSortSimplified(splitHigh, indexIn)
            return A + B

        else:
            B = quickSortSimplified(splitHigh, indexIn)
            A = quickSortSimplified(splitLow, indexIn)
            return A + B

    #return a list if it contains no or just one element
    else:
        return curList


# Prints out the sorted list
def forPrint(list):
    print("\nSorted list: \n")
    for i in range(len(list)):
        print(list[i])

# Writes the sorted list to empty .csv file in directory, emptyforlatsort.csv
def forCsv(list):
    import csv

    with open('emptyforlatsort.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)

        for row in range(len(list) - 1):
            writer.writerow(list[row])