from reindeer import Reindeer

reindeer_array = []

maxTime = 2503
# maxTime = 1000

with open("input.txt") as inputFile:
    # with open("example.txt") as inputFile:
    for line in inputFile:
        reindeerStringArray = line.split(" ")
        reindeerName = reindeerStringArray[0]
        reindeerSpeed = reindeerStringArray[3]
        reindeerSpeedDuration = reindeerStringArray[6]
        reindeerRestDuration = reindeerStringArray[13]
        reindeer = Reindeer(reindeerName, int(reindeerSpeed), int(reindeerSpeedDuration), int(reindeerRestDuration))
        reindeer_array.append(reindeer)
        print reindeer

for second in range(maxTime):
    for reindeer in reindeer_array:
        reindeer.travel()

for reindeer in reindeer_array:
    reindeer.final_stats()
