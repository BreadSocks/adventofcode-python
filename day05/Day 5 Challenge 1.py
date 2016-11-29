niceStringsCount = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        if line.__contains__("ab") or line.__contains__("cd") or line.__contains__("pq") or line.__contains__("xy"):
            continue
        vowelCount = 0
        containsDoubleLetters = False
        previousLetter = ""
        for character in line:
            if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
                vowelCount += 1
            if character == previousLetter:
                containsDoubleLetters = True

            previousLetter = character

        if containsDoubleLetters and vowelCount >= 3:
            niceStringsCount += 1

print "Number of nice strings : ", niceStringsCount