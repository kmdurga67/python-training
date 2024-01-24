import csv
routeDistances = csv.DictReader(open("Distances.csv"))


def buildDistance():
    distances = {}
    for row in routeDistances:
        from_city, to_city, distance = row['from'], row['to'], int(
            row['distance'])
        distances[(from_city, to_city)] = distance
        distances[(to_city, from_city)] = distance
    return distances
