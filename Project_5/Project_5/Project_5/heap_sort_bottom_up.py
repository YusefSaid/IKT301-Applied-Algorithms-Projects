
def heapsort(inputList):
    print("Origin list: ",inputList)
    for elementInList in range(len(inputList) - 2 // 2, -1, -1):
        print(inputList)
        moveElement(inputList, elementInList, len(inputList))


    for lastElement in range(len(inputList) - 1, 0, -1):
        print(inputList)
        switch(inputList, 0, lastElement)
        print(inputList)
        moveElement(inputList, 0, lastElement)

    print("Sorted: ", inputList)

#switch the positions of the elements on the list
def switch(inputList, x, y):
    inputList[x], inputList[y] = inputList[y], inputList[x]


def moveElement(inputList, curNode, lim):
    #in this context the curNode variable is the parent of children

    while True:
        # identification for left and right child on the list
        leftChild, rightChild = curNode * 2 + 1, curNode * 2 + 2
        # parent node has two children under upper bound of the list
        if max(leftChild, rightChild) < lim:
            # compare if children are not bigger then parent
            if inputList[curNode] >= max(inputList[leftChild], inputList[rightChild]):
                break
            #perform a rotation of child parent, and check if underlying children are still smaller than parent
            elif inputList[leftChild] > inputList[rightChild]:
                switch(inputList, curNode, leftChild)
                curNode = leftChild
            else:
                switch(inputList, curNode, rightChild)
                curNode = rightChild
        # consider if left child node is less then upper limit
        elif leftChild < lim:
            # rotate parent with left child, check if parent is still larger then children
            if inputList[leftChild] > inputList[curNode]:
                switch(inputList, curNode, leftChild)
                curNode = leftChild
            else:
                break
        # consider if right child node is less then upper limit
        elif rightChild < lim:
            # rotate parent with right child, check if parent is still larger then children
            if inputList[rightChild] > inputList[curNode]:
                switch(inputList, curNode, rightChild)
                curNode = rightChild
            else:
                break
        # check if there are no children for parent node
        else:
            break

#small test, can be removed
def main():
    a = [5,2,6,4,7,3,1]
    heapsort(a)

if __name__ == "__main__":
    main()