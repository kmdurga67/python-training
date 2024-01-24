def calculateTotalDistance(stops, distances):
    totalDistance = 0

    for i in range(len(stops) - 1):
        currentStop = stops[i]
        nextStop = stops[i + 1]
        totalDistance += distances.get((currentStop, nextStop), 0)

    return totalDistance
