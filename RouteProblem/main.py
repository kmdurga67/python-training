import csv
from calculate_distance import calculateTotalDistance
from build_distance import buildDistance


def main():

    distances = buildDistance()

    routes = csv.DictReader(open("Routes.csv"))
    for row in routes:
        stops = row['stops'].split(', ')

        totalDistance = calculateTotalDistance(stops, distances)

        print(
            f"Total distance from {row['source']} to {row['destination']} via {stops}: {totalDistance} kilometers")


if __name__ == "__main__":
    main()
