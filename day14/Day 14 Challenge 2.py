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

reindeer_at_front = []
for second in range(maxTime):
    # they should all travel before awarding points
    for reindeer in reindeer_array:
        reindeer.travel()

    # work out who is at the front
    for reindeer in reindeer_array:
        if len(reindeer_at_front) == 0:
            reindeer_at_front.append(reindeer)
        else:
            if reindeer.distance_travelled > reindeer_at_front[0].distance_travelled:
                reindeer_at_front = []
                reindeer_at_front.append(reindeer)  # replace
            elif reindeer.distance_travelled == reindeer_at_front[
                0].distance_travelled and reindeer not in reindeer_at_front:
                reindeer_at_front.append(reindeer)

    # award reindeer at the front
    for reindeer in reindeer_at_front:
        reindeer.award_point()

for reindeer in reindeer_array:
    reindeer.final_stats()
