grid = {}

for x in range(1000):
    for y in range(1000):
        grid[x, y] = 0

print "Grid Initialised"
with open("input.txt") as inputFile:
    for line in inputFile:
        # print "Working on line :", line
        components = line.split()
        newValue = ""
        function = "toggle"
        # all coordinates are x,y
        if line.startswith("turn off"):
            bottomLeft = components[2]
            topRight = components[4]
            function = "off"
        elif line.startswith("toggle"):
            bottomLeft = components[1]
            topRight = components[3]
        elif line.startswith("turn on"):
            bottomLeft = components[2]
            topRight = components[4]
            function = "on"

        bottomLeftX = map(int, bottomLeft.split(","))[0]
        bottomLeftY = map(int, bottomLeft.split(","))[1]
        topRightX = map(int, topRight.split(","))[0]
        topRightY = map(int, topRight.split(","))[1]

        for x in range(bottomLeftX, topRightX + 1):  # to include last number
            for y in range (bottomLeftY, topRightY + 1):
                oldValue = int(grid[x, y])
                if function == "toggle":
                    oldValue += 2
                elif function == "on":
                    oldValue += 1
                else:
                    oldValue -= 1 if oldValue > 0 else oldValue
                grid[x, y] = oldValue

brightnessCount = 0
for x in range(1000):
    for y in range(1000):
        value = int(grid[x, y])
        brightnessCount += value
print "Brightness Counter", brightnessCount
