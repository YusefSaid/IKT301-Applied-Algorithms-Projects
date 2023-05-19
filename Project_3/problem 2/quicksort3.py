from math import cos, asin, sqrt, pi,sin
from random import randint

def placeDistanceHolder(list):

    # for comparison placeholder in list for distance from pole to destination
    for i in range(len(list)):
        list[i].append("placeholder")

    return list

#function to calculate distance between to latitude and longitude positions
def distanceCalculator(lat1,long1,lat2,long2):
    #for radians to degree conversion
    p = pi / 180
    #earth radius
    r=6371
    #Difference in latitude and longitude
    difInLat= lat2 - lat1
    difInLong = long2 - long1

    f1 = sin(difInLat/2*p)**2 + cos(lat1*p)* cos(lat2*p) * sin(difInLong/2*p)**2
    f2 = 2*asin(sqrt(f1))
    f3 = f2*r
    return int(round(f3))


def quickSortThree(curList, indexLat,indexLong,refPointArray):

    #Similar approach as before ref quicksortOne function
    if len(curList) > 1:
        splitLow, splitHigh = [], []
        pivotIndex = randint(0, len(curList) - 1)
        #Fetch pivot values from the city list
        #Next fetch reference point values and send them to distance calculation
        pivotIndexLatValue, pivotIndexLongValue = float(curList[pivotIndex][indexLat]),float(curList[pivotIndex][indexLong])

        refPointToPivotDistance = distanceCalculator(float(refPointArray[0]),float(refPointArray[1]),
                                                  pivotIndexLatValue,pivotIndexLongValue)

        counter=0

        while curList:
            dataForCity= [curList[counter][indexLat],curList[counter][indexLong]]
            #Do the comparsion similarly as discribed on line 34-35
            refPointAndCity=distanceCalculator(float(refPointArray[0]),float(refPointArray[1]),
                                               float(dataForCity[0]),float(dataForCity[1]))


            if refPointAndCity <= refPointToPivotDistance:
                curList[counter][-1]=refPointAndCity
                splitLow.append(curList[counter])
                curList.pop(0)
            else:
                curList[counter][-1]=refPointAndCity
                splitHigh.append(curList[counter])
                curList.pop(0)

        # This little code piece provides a bandage solution to recursion depth issue with this project
        # It does a small check between highest element of highsplit and lowest element of lowsplit
        # If the difference is less than 100, consider the list sorted, do not initiate another recursion
        # Although 150 km is quite big margin of error, this is the lowest number i could use so that algorithm would
        # not return a recursion depth issue
        #
        dif = 151

        if len(splitLow) != 0 and len(splitHigh) != 0:
            dif = float(splitHigh[-1][-1]) - float(splitLow[0][-1])

        if dif <= 150:
            return splitLow + splitHigh

        else:
            # Attempt at quickening sorting process, begins running recursive sort one the list containing lowest number of
            # elements first
            if len(splitLow) < len(splitHigh):
                A = quickSortThree(splitLow, indexLat,indexLong,refPointArray)
                B = quickSortThree(splitHigh, indexLat,indexLong,refPointArray)
                return A + B

            else:
                B = quickSortThree(splitHigh, indexLat,indexLong,refPointArray)
                A = quickSortThree(splitLow, indexLat,indexLong,refPointArray)
                return A + B

    else:
        return curList

def quickSortThreeSimplified(curList, indexLat,indexLong,refPointArray):

    #Similar approach as before ref quicksortOne function
    if len(curList) > 1:
        splitLow, splitHigh = [], []
        pivotIndex = randint(0, len(curList) - 1)
        #Fetch pivot values from the city list
        #Next fetch reference point values and send them to distance calculation
        pivotIndexLatValue, pivotIndexLongValue = float(curList[pivotIndex][indexLat]),float(curList[pivotIndex][indexLong])

        refPointToPivotDistance = distanceCalculator(float(refPointArray[0]),float(refPointArray[1]),
                                                  pivotIndexLatValue,pivotIndexLongValue)

        counter=0

        while curList:
            dataForCity= [curList[counter][indexLat],curList[counter][indexLong]]
            #Do the comparsion similarly as discribed on line 34-35
            refPointAndCity=distanceCalculator(float(refPointArray[0]),float(refPointArray[1]),
                                               float(dataForCity[0]),float(dataForCity[1]))


            if float(refPointAndCity) <= float(refPointToPivotDistance):
                curList[counter][-1]=refPointAndCity
                splitLow.append(curList[counter])
                curList.pop(0)
            else:
                curList[counter][-1]=refPointAndCity
                splitHigh.append(curList[counter])
                curList.pop(0)


        if len(splitLow) < len(splitHigh):
            A = quickSortThreeSimplified(splitLow, indexLat,indexLong,refPointArray)
            B = quickSortThreeSimplified(splitHigh, indexLat,indexLong,refPointArray)
            return A + B

        else:
            B = quickSortThreeSimplified(splitHigh, indexLat,indexLong,refPointArray)
            A = quickSortThreeSimplified(splitLow, indexLat,indexLong,refPointArray)
            return A + B

    else:
        return curList

# Writes the sorted list to empty .csv file in directory, emptyforlatlogsort.csv
def forCsv(list):
    import csv

    with open('emptyforlatlogsort.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)

        for row in range(len(list) - 1):
            writer.writerow(list[row])