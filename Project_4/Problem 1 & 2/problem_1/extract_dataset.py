def open_file():
    import csv
    world_cities = []
    file = "./worldcities.csv"
    with open(file, encoding="utf-8") as csv_file:
        csv = csv.DictReader(csv_file, delimiter=',')
        for row in csv:
            world_cities.append([row['city'], row['lat'], row['lng'], row['country']])

    norwegian_cities = get_norwegian_cities(world_cities)
    return norwegian_cities

def get_norwegian_cities(world_cities):
    norwegian_cities = []

    for city in world_cities:
        if "Norway" in city:
            norwegian_cities.append(city)

    return norwegian_cities#sorted(norwegian_cities, key=lambda norwegian_cities: norwegian_cities[1])

