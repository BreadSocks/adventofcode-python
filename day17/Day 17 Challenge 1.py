import itertools
numberArray = []
totalPermutationsArray = []
targetCombinationArray = []
target = 25

def recursivepermutation(arrayofnumbers):
    for number in arrayofnumbers:
        newArray = list(arrayofnumbers)
        newArray.remove(number)
        newPermutationsArray = list(itertools.permutations(newArray))
        itertools.co
        totalPermutationsArray.extend(newPermutationsArray)
        recursivepermutation(list(newArray))


with open("example1.txt") as inputFile:
    for line in inputFile:
        numberArray.append(int(line))

print "Filled number array"


print list(itertools.permutations(numberArray))
# 1
# totalPermutationsArray = list(itertools.permutations(numberArray))
# recursivepermutation(list(numberArray))
# 2
for x in range(1, len(numberArray) + 1):
    totalPermutationsArray += itertools.combinations(numberArray, x)

print "Finished ", len(totalPermutationsArray)

for array in totalPermutationsArray:
    total = 0
    for value in array:
        total += value
    if total == target:
        sortedArray = sorted(array)
        # targetCombinationArray.append("".join(str(x) for x in sortedArray))
        # targetCombinationArray.append(sorted(array))
        targetCombinationArray.append(array)

print "FOnd combinations :", len(targetCombinationArray)
print "unique", len(set(targetCombinationArray))
print set(targetCombinationArray)