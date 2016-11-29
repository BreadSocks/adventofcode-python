reindeerNameArray = []
reindeerSpeedDictionary = {}
reindeerSpeedDurationDictionary = {}
reindeerRestDurationDictionary = {}
reindeerResultDictionary = {}

maxTime = 2503

def fillDictionaries():
    with open("input.txt") as inputFile:
        for line in inputFile:
            reindeerStringArray = line.split(" ")
            reindeerName = reindeerStringArray[0]
            reindeerSpeed = reindeerStringArray[3]
            reindeerSpeedDuration = reindeerStringArray[6]
            reindeerRestDuration = reindeerStringArray[13]
            reindeerNameArray.append(reindeerName)
            reindeerSpeedDictionary[reindeerName] = int(reindeerSpeed)
            reindeerSpeedDurationDictionary[reindeerName] = int(reindeerSpeedDuration)
            reindeerRestDurationDictionary[reindeerName] = int(reindeerRestDuration)

fillDictionaries()
for second in range(maxTime):
    for reindeer in reindeerNameArray:
        
for reindeer in reindeerNameArray:
    distance = 0
    secondsResting = 0
    secondsFlying = 0
    restTimeLeft = 0
    startNextRun = True
    skip = True
    maxSprintDistance = (reindeerSpeedDictionary[reindeer] * reindeerSpeedDurationDictionary[reindeer])
    for second in range(maxTime):
        if restTimeLeft != 0:
            restTimeLeft -= 1
            secondsResting += 1
            if restTimeLeft == 0:
                startNextRun = True
                skip = True
        elif not skip and (distance >= maxSprintDistance and distance % maxSprintDistance == 0):
            restTimeLeft = reindeerRestDurationDictionary[reindeer]
            restTimeLeft -= 1  # for this round we rest
            secondsResting += 1
            startNextRun = False
        elif startNextRun:
            skip = False
            distance += reindeerSpeedDictionary[reindeer]
            secondsFlying += 1
    reindeerResultDictionary[reindeer] = distance
    print reindeer, "Rested for :", secondsResting, "seconds, Flew for :", secondsFlying
print reindeerResultDictionary
print "Fastest reindeer travelled ", max(reindeerResultDictionary.itervalues()), " km"
