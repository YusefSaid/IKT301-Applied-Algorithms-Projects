import csv

with open('worldcities.csv', 'r', encoding="utf8") as wc_csv_file:
    reader = csv.DictReader(wc_csv_file)

    count = 0
    latitude_List = []
    city_List = []
    longitude_List = []
    for row in reader:
        latitude_List.append(row['lat'])
        city_List.append(row['city'])
        longitude_List.append(row['lng'])

print(f"Total amount of latitude values: {len(latitude_List):,}")
print(f"Total amount of longitude: {len(longitude_List):,}")
print(f"Total amount of cities: {len(city_List):,}")

# Using dictionary comprehension to convert lists into dictionary
dict_Pairs = {city_List[i]: latitude_List[i] for i in range(len(city_List))}

# implementation of MergeSort
def mergeSort(latitude):
    global count
    if len(latitude) > 1:
        # Finding the mid of the array
        mid = len(latitude) // 2
        # Dividing the array elements
        L = latitude[:mid]
        # into 2 halves
        R = latitude[mid:]
        # Sorting the Left half side
        mergeSort(L)
        # Sorting the Right half side
        mergeSort(R)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                latitude[k] = L[i]
                i += 1
            else:
                latitude[k] = R[j]
                j += 1
                k += 1
                # Merge that will be counted.
                count = count + 1

        # Checking if any element was left
        while i < len(L):
            latitude[k] = L[i]
            i += 1
            k += 1
            # Merge that will be counted.
            count = count + 1

        while j < len(R):
            latitude[k] = R[j]
            j += 1
            k += 1
            # Merge that will be counted.
            count = count + 1

    count = count + 1


# Code to print the list
def printList(latitude):
    for i in range(len(latitude)):
        print(latitude[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    latitude = latitude_List
    print("Given array is", end="\n")
    printList(latitude)
    mergeSort(latitude)
    print("Sorted array is: ", end="\n")
    printList(latitude)

    print("Count: ", count)