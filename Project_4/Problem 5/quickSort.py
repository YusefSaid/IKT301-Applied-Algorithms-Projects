from random import randint

def sort(curList, indexIn):
    #Begin sorting the list, the lenght of which is not 1 or less
    #Create two list for sorting, for lower value than pivot or higher
    #Fetch value for pivot from list

    if len(curList) > 1:
        splitLow, splitHigh = [], []
        pivotIndex = randint(0, len(curList) - 1)
        pivotIndexValue = curList[pivotIndex][indexIn]
        counter=0

        while curList:
            x,y = float(curList[counter][indexIn]),float(pivotIndexValue)

            if x <= y:
                splitLow.append(curList[counter])
                curList.pop(0)
            else:
                splitHigh.append(curList[counter])
                curList.pop(0)

        A = sort(splitLow, indexIn)
        B = sort(splitHigh, indexIn)

        return B+A

    else:
        return curList
