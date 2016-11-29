import itertools

nameArray = []
relationsDictionary = {}
resultsDictionary = {}

with open("input.txt") as inputFile:
    for line in inputFile:
        splitLine = line.split(" ")
        nameOne = splitLine[0]
        nameTwo = splitLine[len(splitLine) - 1].replace("\n", "").replace(".", "")
        happiness = int(splitLine[3])
        if line.__contains__("lose"):
            happiness *= -1
        nameArray.append(nameOne)
        relationsDictionary[nameOne, nameTwo] = happiness

# part 2
for name in nameArray:
    relationsDictionary["David B", name] = 0
    relationsDictionary[name, "David B"] = 0
nameArray.append("David B")

nameArray = list(set(nameArray))
permutationsArray = list(itertools.permutations(nameArray))

print "Names", nameArray
print "Permutations", permutationsArray
print "Number :", len(permutationsArray)

for permutation in permutationsArray:
    numberofNames = len(permutation)
    clockwiseCounter = 0
    counterClockwiseCounter = 0
    for clockwise in range(numberofNames):
        clockwiseName1 = permutation[clockwise]
        if clockwise + 1 == numberofNames:
            clockwiseName2 = permutation[0]
        else:
            clockwiseName2 = permutation[clockwise + 1]
        print "Clockwise Comparing", clockwiseName1, clockwiseName2
        clockwiseCounter += relationsDictionary[clockwiseName1, clockwiseName2]

    print ""

    for counterwise in range(numberofNames - 1, -1, -1):
        counterwiseName1 = permutation[counterwise]
        if counterwise - 1 == -1:
            counterwiseName2 = permutation[numberofNames - 1]
        else :
            counterwiseName2 = permutation[counterwise - 1]
        print "Counter Clockwise Comparing", counterwiseName1, counterwiseName2
        counterClockwiseCounter += relationsDictionary[counterwiseName1, counterwiseName2]

    print ""

    print "Adding", clockwiseCounter, counterClockwiseCounter
    resultsDictionary[permutation] = clockwiseCounter + counterClockwiseCounter

bestResult = max(resultsDictionary.values())
for arrangement, score in resultsDictionary.iteritems():
    if score == bestResult:
        print "Finished", arrangement, bestResult
