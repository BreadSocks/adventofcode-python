counter = 1
allSueDictionary = {}
potentialSueArray = []
factList = []
mySueDictionary = {"children": 3, "cats": 7,
                   "samoyeds": 2, "pomeranians": 3,
                   "akitas": 0, "vizslas": 0,
                   "goldfish": 5, "trees": 3,
                   "cars": 2, "perfumes": 1}

# 260, IS THE RIGHT ANSWER. FIX FIX FIX NEEDED

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
        currentDictionary = allSueDictionary[suenumber]
        for filterfact in factList:
            if filterfact in mySueDictionary and filterfact in currentDictionary:
                if (filterfact == "trees" or filterfact == "cats") and currentDictionary[filterfact] <= \
                        mySueDictionary[filterfact]:
                    potentialSueArray.remove(suenumber)
                    break
                elif (filterfact == "pomeranians" or filterfact == "goldfish") and currentDictionary[filterfact] >= mySueDictionary[filterfact]:
                    potentialSueArray.remove(suenumber)
                    break
                # elif currentDictionary[filterfact] is not mySueDictionary[filterfact] and filterfact is not "trees" and filterfact is not "cats" and filterfact is not "pomeranians" and filterfact is not "goldfish":
                #     potentialSueArray.remove(suenumber)
                #     break
                    # can't have outside break as it means we'll skip fact checks


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
            if (fact == "trees" or fact == "cats") and thisSuesDictionary[fact] > mySueDictionary[fact]:
                potentialSueArray.append(sue)
            elif (fact == "pomeranians" or fact == "goldfish") and thisSuesDictionary[fact] < mySueDictionary[fact]:
                potentialSueArray.append(sue)
            elif thisSuesDictionary[fact] == mySueDictionary[fact] and fact is not "trees" and fact is not "cats" and fact is not "pomeranians" and fact is not "goldfish":
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
