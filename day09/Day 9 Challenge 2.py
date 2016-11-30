import itertools

placesArray = []
distanceDictionary = {}

with open("input.txt") as inputFile:
    for line in inputFile:
        placesAndValue = map(str, line.replace("\n", "").split(" = "))
        distance = int(placesAndValue[1])
        places = placesAndValue[0].split("to")
        firstPlace = places[0].strip()
        secondPlace = places[1].strip()
        print "Line reads", firstPlace, "->", secondPlace, "is", distance

        if firstPlace not in placesArray:
            placesArray.append(firstPlace)
        if secondPlace not in placesArray:
            placesArray.append(secondPlace)

        distanceDictionary[firstPlace + "," + secondPlace] = distance
        distanceDictionary[secondPlace + "," + firstPlace] = distance
    print "\nList of Possible Routes"
    listOfPossibleRoutes = list(itertools.permutations(placesArray))
    print listOfPossibleRoutes
    print "\nPossible Values"
    print distanceDictionary
    print "\n"

resultArray = []
for route_tuple in listOfPossibleRoutes:
    # print route_tuple
    journey = {}
    # resultArray = []
    for index, item in enumerate(route_tuple):
        # print index, item
        if index + 1 >= len(route_tuple):
            continue
        # next = route_tuple[index + 1] if index + 1 < len(route_tuple) else route_tuple[0]
        next = route_tuple[index + 1]
        dictionaryKey = item + "," + next
        if dictionaryKey in distanceDictionary:
            journeyTime = distanceDictionary[dictionaryKey]
        else:
            alternateKey = ','.join(dictionaryKey.split(',')[::-1])
            # dictionaryKey = ''.join(dictionaryKey.split(",").reverse())
            journeyTime = distanceDictionary[alternateKey]
        journey[dictionaryKey] = journeyTime
        print item, next
    # print "Journey", journey
    resultArray.append(journey)

print "\n"
print resultArray
print "Possible", len(resultArray), "Journeys"

longestDistance = 0
for journeyDictionary in resultArray:
    distance = 0
    journeyDestinations = ""
    for key, value in journeyDictionary.iteritems():
        journeyDestinations += key
        distance += value
    # print journeyDestinations, distance
    if distance > longestDistance:
        longestDistance = distance

print "Longest Distance:", longestDistance
