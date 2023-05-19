import csv


# store data on the performance of each algorithm if necessary
def store_data(number_of_keys, time_data_random, time_data_ascending, time_data_descending, file_name):
    field_names = ["number_of_keys", "time_data_random", "time_data_ascending", "time_data_descending"]
    data = {field_names[0]: number_of_keys, field_names[1]: time_data_random, field_names[2]: time_data_ascending,
            field_names[3]: time_data_descending}
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerow(data)


# retrieve data on each algorithm.
def open_file(file_name):
    with open(file_name, 'r') as csvfile:
        number_of_keys, time_data_random, time_data_ascending, time_data_descending = [], [], [], []
        reader = csv.DictReader(csvfile)
        for row in reader:
            number_of_keys.append(row["number_of_keys"])
            time_data_random.append(row["time_data_random"])
            time_data_ascending.append(row["time_data_ascending"])
            time_data_descending.append(row["time_data_descending"])

    return number_of_keys, time_data_random, time_data_ascending, time_data_descending
