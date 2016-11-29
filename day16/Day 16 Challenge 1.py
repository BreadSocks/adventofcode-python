counter = 1
allSueDictionary = {}
potentialSueArray = []
factList = []
mySueDictionary = {"children": 3, "cats": 7,
                   "samoyeds": 2, "pomeranians": 3,
                   "akitas": 0, "vizslas": 0,
                   "goldfish": 5, "trees": 3,
                   "cars": 2, "perfumes": 1}

def create_dictionary(sueLine):
    parts = sueLine.split(", ")
    sueValues = {}
    for part in range(len(parts)):
        fact = parts[part]
        key = fact.split(": ")[0]
        value = int(fact.split(": ")[1])
        factList.append(key)
        sueValues[key] = value
    return sueValues

def filter_further(current_results):
    for suenumber in current_results:
        for filterfact in factList:
            if filterfact in mySueDictionary and filterfact in allSueDictionary[suenumber]:
                if mySueDictionary[filterfact] != allSueDictionary[suenumber][filterfact]:
                    potentialSueArray.remove(suenumber)
                    break

with open("input.txt") as inputFile:
    for line in inputFile:
        linewithoutname = line.replace("Sue " + str(counter) + ": ", "")
        allSueDictionary[counter] = create_dictionary(linewithoutname)
        counter += 1

factList = list(set(factList))  # remove duplicate fact names

for sue in range(1, len(allSueDictionary.keys()) + 1, 1):
    thisSuesDictionary = allSueDictionary[sue]
    for fact in factList:
        if fact in thisSuesDictionary and fact in mySueDictionary:
            if thisSuesDictionary[fact] == mySueDictionary[fact]:
                potentialSueArray.append(sue)
            elif sue in potentialSueArray:
                potentialSueArray.remove(sue)
            break
    print sue, thisSuesDictionary

# we now have a list of any potential sue's. Lets filter on that list till we have one result
while len(potentialSueArray) != 1:
    print potentialSueArray
    filter_further(potentialSueArray)

print "Finished : Sue Number", potentialSueArray[0]
