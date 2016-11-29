stringLiteralLength = 0
stringMemoryLength = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        lineWithoutEnd = line.replace("\n", "")
        stringLiteralLength += len(lineWithoutEnd)
        stringMemoryLength += len(eval(lineWithoutEnd))
        print "Memory Size ", len(eval(lineWithoutEnd)), \
            " Literal Size ", len(lineWithoutEnd), \
            " For Line ", lineWithoutEnd
print stringLiteralLength - stringMemoryLength