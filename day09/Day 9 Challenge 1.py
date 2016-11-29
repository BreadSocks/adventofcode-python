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


with open("example1.txt") as inputFile:
    for line in inputFile:
        placesAndValue = map(str, line.replace("\n", "").split(" = "))
        distance = int(placesAndValue[1])
        places = placesAndValue[0].split(" to ")
        firstPlace = places[0]
        secondPlace = places[1]
        print "Line reads ", firstPlace, " -> ", secondPlace, " is ", distance

        if firstPlace not in placesArray:
            placesArray.append(firstPlace)
        if secondPlace not in placesArray:
            placesArray.append(secondPlace)

        distanceDictionary[firstPlace + "," + secondPlace] = distance
        # distanceDictionary[secondPlace + "," + firstPlace] = distance
    newList = list(itertools.permutations(distanceDictionary))
    print newList
    # print placesArray
    # print distanceDictionary



# for place in placesArray:
#     recursiveLoopForPlaceInArray(place, placesArray, {})


print "Number of potential routes : ",  len(resultsDictionary), "\nWith results: ", resultsDictionary
