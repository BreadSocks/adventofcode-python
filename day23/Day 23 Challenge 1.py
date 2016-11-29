registerDictionary = {}
instructionArray = []

def handlejump(jumpline):
    if jumpline.__contains__("+"):
        jumpby = int(jumpline.replace("+", ""))
    else:
        jumpby = int(jumpline.replace("-", ""))
        jumpby *= -1

    return jumpby

def handlespecialjump(specialjumpline):
    specialinstruction = specialjumpline[0]
    specialregister = str(specialjumpline[1]).replace(",", "")
    specialjump = str(specialjumpline[2])
    if specialjump.__contains__("+"):
        specialjump = int(specialjump.replace("+", ""))
    else:
        specialjump = int(specialjump.replace("-", ""))
        specialjump *= 1

    if specialinstruction == "jie" and registerDictionary[specialregister] % 2 == 0:
        return specialjump
    elif specialinstruction == "jio" and registerDictionary[specialregister] == 1:
        return specialjump
    else:
        return 1  # so we increment normally

with open("input.txt") as inputFile:
    for line in inputFile:
        instructionArray.append(line)

index = 0
while 0 <= index < len(instructionArray):
    currentLine = str(instructionArray[index])
    # print index, currentLine
    splitLine = currentLine.split(" ")
    instruction = splitLine[0]
    if instruction == "jmp":
        index += handlejump(splitLine[1])
        continue

    register = splitLine[1].replace(",", "").replace("\n", "")
    registerValue = 0
    if register in registerDictionary.keys():
        registerValue = registerDictionary[register]
    else:
        registerDictionary[register] = registerValue

    if currentLine.__contains__(","):
        index += handlespecialjump(splitLine)
        continue

    if instruction == "inc":
        registerDictionary[register] = registerValue + 1
    elif instruction == "tpl":
        registerDictionary[register] = registerValue * 3
    elif instruction == "hlf":
        registerDictionary[register] = registerValue / 2

    index += 1  # go to next instruction
    print registerDictionary

print registerDictionary
