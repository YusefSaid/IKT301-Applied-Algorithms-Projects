import csv
import operator

with open('worldcities.csv', 'r', encoding="utf8") as wc_csv_file:
    reader = csv.DictReader(wc_csv_file)

    count = 0

    latitude_List = []
    city_List = []

    for row in reader:
        count = count + 1
        latitude_List.append(row['lat'])
        city_List.append(row['city'])

dict_Pairs = {city_List[i]: latitude_List[i] for i in range(len(city_List))}


def binarySearchAppr(arr, start, end, x):
    # check condition
    if end >= start:
        mid = start + (end - start) // 2
        # If element is present at the middle
        if arr[mid] == x:
            return mid
        # If element is smaller than mid
        elif operator.gt(arr[mid], x):
            return binarySearchAppr(arr, start, mid - 1, x)
        # Else the element greater than mid
        else:
            return binarySearchAppr(arr, mid + 1, end, x)
    else:
        # Element is not found in the array
        return -1


def menu():
    choice = '0'
    while choice == '0':
        print("\nWhat do you want to do?")
        print("1. City     -> Latitude")
        print("2. Latitude -> City")

        choice = input("Please make a choice: ")

        if choice == "1":
            print(f"Which City do you want to find the 'latitude' of? ")
            CityName = input()
            CityLatitude = dict_Pairs.get(CityName)
            print(f"{CityName}'s latitude is: '{CityLatitude}'")

            menu()
        elif choice == "2":
            latitude_List.sort()
            arr = latitude_List

            x = (input("Enter Latitude: "))
            result = binarySearchAppr(arr, 0, len(arr) - 1, x)
            if result != -1:
                print(
                    f"The City with latitude '{x}' is '{list(dict_Pairs.keys())[list(dict_Pairs.values()).index(x)]}'")
            else:
                print(f"There exists no city with the latitude '{x}'")
        else:
            print("Invalid choice.")
        menu()


if __name__ == "__main__":
    menu()
