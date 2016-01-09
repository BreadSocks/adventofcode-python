data = open("input.txt").read()
santaPoints = ["0,0"]
robotPoints = ["0,0"]
for index, character in enumerate(data):
    if index % 2 == 0:
        previousLocation = santaPoints[len(santaPoints) - 1]
    else:
        previousLocation = robotPoints[len(robotPoints) - 1]
    previousPoint = map(int, previousLocation.split(","))
    xAxis = previousPoint[0]
    yAxis = previousPoint[1]
    if character == "^":
        yAxis += 1
    elif character == ">":
        xAxis += 1
    elif character == "v":
        yAxis -= 1
    elif character == "<":
        xAxis -= 1

    house = str(xAxis) + "," + str(yAxis)
    if index % 2 == 0:
        santaPoints.append(house)
    else:
        robotPoints.append(house)

totalList = santaPoints + robotPoints
print "Houses that receive at least one present : ", len(set(totalList))
