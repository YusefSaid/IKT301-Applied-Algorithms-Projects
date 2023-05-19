import quicksort1_2
import quicksort3
#recursion limit inscreased, because of the way the pivot value is choosen, the sorting can land on unfavorable value
#causing an excessive increase in reccursion depth.
# In case of meating recursion depth limit, rerunning program can provide a more favorable recursion path
import sys
sys.setrecursionlimit(10000)


#read the csv dataset and covert it to list
def readCSV(choice):
    import csv

    world_cities = []
    #Choice of list downscaled list and full scaled list
    if choice == 1:
        file = "./worldcitiesDS.csv"
    else:
        file = "./worldcities.csv"

    with open(file, encoding="utf-8") as csv_file:
        csv = csv.reader(csv_file, delimiter=',')
        for row in csv:
            if len(row) != 1:
                world_cities.append(row)

    index = quicksort1_2.fetchIndex(world_cities)
    world_cities.pop(0)

    return world_cities,index

def main():

    #The alghoritms running for bigger dataset are adjusted, and can sometimes run more inconsistently and unprecisely
    #If you wish to simply test corectivness of sorting alghoritm functionality use smaller data set.
    # Alghoritms running for larger dataset do what they are expected but due to reccursion depth issue, they may require
    # some reruning until sorting alghoritms goes through more fortunate piviting points, allowing reduction in recursion
    #depth
    choice =  int(input("Do you wish to run for downscaled list (250 entries)? 1 - yes, 0 - no (40k input) "))

    if choice != 0 and choice != 1:
        print("Wrong input")
        return 0

    #Read the csv file
    curList, index = readCSV(choice)


    #Exercise 3.1

    if choice == 1:
        sortedList = quicksort1_2.quickSortSimplified(curList, index)
        # Exercise 3.2
        quicksort1_2.forCsv(sortedList)
        quicksort1_2.forPrint(sortedList)
        print("\nNumber of comparisons made on a simplified list: ", quicksort1_2.comparisonForSimplified)
    else:
        sortedList = quicksort1_2.quickSortOne(curList, index)
        #Additional sort to without limitations speciefied in quickSortOne (for avoiding recursion depth issue), should
        #provide more preciselly sorted data, as sorted list is less chaotic structually
        x=quicksort1_2.comparison
        sortedList = quicksort1_2.quickSortOne(sortedList, index)
        # Exercise 3.2
        quicksort1_2.forCsv(sortedList)
        quicksort1_2.forPrint(sortedList)
        print("\nNumber of comparisons made under sorting of big list with margin of error: ",  x)
        print("\nTotal number of comparisons made under sorting to get it as precise as possible: ",  quicksort1_2.comparison)


    choice2 = input("\nDo you wish to run latitude and logitude sort next? 1 - yes, 0 - no ")

    if int(choice2) != 1:
        print("Done")
        return 0

    #Exercise 3.3
    
    #Define latitude and longitude for northPole
    northPole=[90,0]

    curList, index = readCSV(choice)

    # Simply creates an empty data field in csv to store distance from reference point, placeded as the element in the list.
    curlistAdjusted = quicksort3.placeDistanceHolder(curList)

    if int(choice) == 1:
        sortedListFor3 = quicksort3.quickSortThreeSimplified(curlistAdjusted, 2, 3, northPole)
        # Prints list in console
        quicksort1_2.forPrint(sortedListFor3)
        # Writes the sorted list to empty.csv file in directory for better oversight
        quicksort1_2.forCsv(sortedListFor3)

    else:
        #Run to sort the list by distance from reference point

        # As it is very strenuous on a script recusivly, we first the script through a version that allows a margin of
        # error, then we run the sorted list through the same sort without limitation of error margin
        # although, it does take more time, it does provide more accurate data without running into reccursion problem
        sortedListFor3 = quicksort3.quickSortThree(curlistAdjusted,2,3,northPole)

        sortedListFor3 = quicksort3.quickSortThree(sortedListFor3, 2, 3, northPole)
        #Prints list in console
        quicksort1_2.forPrint(sortedListFor3)
        #Writes the sorted list to empty.csv file in directory for better oversight
        quicksort1_2.forCsv(sortedListFor3)

if __name__ == '__main__':
    main()

