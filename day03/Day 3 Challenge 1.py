data = open("input.txt").read()
gridPoints = ["0,0"]
for character in data:
    #  get previous point
    previousLocation = gridPoints[len(gridPoints) - 1]
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

    gridPoints.append(str(xAxis) + "," + str(yAxis))
print "Houses that receive at least one present :", len(set(gridPoints))
