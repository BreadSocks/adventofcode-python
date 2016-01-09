totalSquareFeet = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        # format is l x w x h
        components = map(int, line.split("x"))
        length = components[0]
        width = components[1]
        height = components[2]
        calc1 = length * width
        calc2 = width * height
        calc3 = height * length
        minSurface = min(calc1, calc2, calc3)
        # Surface area is : 2*l*w + 2*w*h + 2*h*l + smallest area
        totalSquareFeet += (2 * calc1) + (2 * calc2) + (2 * calc3) + minSurface

print "Total Square Feet Required :", totalSquareFeet
