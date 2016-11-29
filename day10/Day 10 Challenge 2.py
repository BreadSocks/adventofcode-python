data = "3113322113"
counter = 0
while counter < 50:
    i = 0
    newString = ""
    while i < len(data):
        innerCounter = 1
        j = i + 1
        while j < len(data):
            if data[i] == data[j]:
                innerCounter += 1
                j += 1
            else:
                break
        # print "Found ", innerCounter, " ", data[i], "'s"
        newString = newString + str(innerCounter) + str(data[i])
        i += innerCounter
    print "Pass", counter, "String Length: ", len(newString)
    data = newString
    counter += 1
