import itertools
placesArray = []
distanceDictionary = {}
resultsDictionary = []

def secondrecursiveloop(currentPlace, currentArray, currentDictionary):
    xxplacearray = list(currentArray)
    xxplacearray = xxplacearray.remove(currentPlace)

    for nextPlace in xxplacearray:
        key = currentPlace + "," + nextPlace
        reverseKey = nextPlace + "," + currentPlace

        dictionaryCopy = dict(currentDictionary)
        if key in distanceDictionary:
            dictionaryCopy[key] = distanceDictionary[key]
            secondrecursiveloop(nextPlace, xxplacearray)
        elif reverseKey in distanceDictionary:
            dictionaryCopy[reverseKey] = distanceDictionary[reverseKey]
            secondrecursiveloop(nextPlace, xxplacearray)

    if len(xxplacearray) == 0:
        print "Solution Found", currentDictionary
        resultsDictionary.append(currentDictionary)

def recursiveLoopForPlaceInArray(currentPlace, currentArray, currentDictionary):
    xplacearray = list(placesArray)
    xplacearray.remove(currentPlace)

    for nextPlace in xplacearray:
        key = currentPlace + "," + nextPlace
        reverseKey = nextPlace + "," + currentPlace

        dictionaryCopy = dict(currentDictionary)
        if key in distanceDictionary:
            dictionaryCopy[key] = distanceDictionary[key]
            secondrecursiveloop(nextPlace, xplacearray, currentDictionary)
        elif reverseKey in distanceDictionary:
            dictionaryCopy[reverseKey] = distanceDictionary[reverseKey]
            secondrecursiveloop(nextPlace, xplacearray, currentDictionary)


with open("example.txt") as inputFile:
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
    print route_tuple
    journey = {}
    # resultArray = []
    for index, item in enumerate(route_tuple):
        print index, item
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
    print "Journey", journey
    resultArray.append(journey)

print "\n"
print resultArray
print "Possible", len(resultArray), "Journeys"

for journeyDictionary in resultArray:
    distance = 0
    journeyDestinations = ""
    for key, value in journeyDictionary.iteritems():
        journeyDestinations += key
        distance += value
    print journeyDestinations, distance
