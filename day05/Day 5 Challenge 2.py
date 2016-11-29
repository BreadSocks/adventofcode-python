niceStringsCount = 0
gappyCount = 0
doubleCount = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        lettersWithGap = False
        lettersDouble = False
        for index, character in enumerate(line):
            if index <= len(line) - 3:  # one for newline, two for gap
                if line[index] == line[index + 2]:
                    lettersWithGap = True
                pairCounter = index + 1
                while pairCounter < len(line):
                    if line.count(line[index] + line[pairCounter]) >1:
                        lettersDouble = True
                        break
                    else:
                        pairCounter += 1

        if lettersWithGap:
            gappyCount += 1
            print "Found gappy", line
        if lettersDouble:
            doubleCount += 1
            print "found double", line
        if (lettersWithGap and lettersDouble):
            niceStringsCount += 1
            print "found nice string"
print "Number of words with gaps : ", gappyCount
print "Number of words with doubles : ", doubleCount
print "Number of nice : ", niceStringsCount
