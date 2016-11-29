import re
stringLiteralLength = 0
stringEncodedLength = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        lineWithoutEnd = line.replace("\n", "")
        encodedString = re.escape(lineWithoutEnd)
        stringLiteralLength += len(lineWithoutEnd)
        stringEncodedLength += len(encodedString) + 2  # plus additional quotes " "
        print "Encoded Size ", len(encodedString) + 2, \
            " Literal Size ", len(lineWithoutEnd), \
            " For Line ", lineWithoutEnd, \
            " Encoded Line ", encodedString
print stringEncodedLength - stringLiteralLength
