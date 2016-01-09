totalFeetOfRibbon = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        # format is l x w x h
        components = map(int, line.split("x"))
        length = components[0]
        width = components[1]
        height = components[2]
        smallestSide = min(components)
        components.remove(smallestSide)  # remove smallest from list
        nextSmallestSide = min(components)
        feetForRibbon = smallestSide + smallestSide + nextSmallestSide + nextSmallestSide
        feetForBow = length * width * height
        totalFeetOfRibbon += feetForRibbon + feetForBow

print "Total Square Feet Required :", totalFeetOfRibbon
