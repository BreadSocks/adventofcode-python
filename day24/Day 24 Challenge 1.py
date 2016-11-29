import itertools
import time

start = time.clock()

weightArray = []
workingArray = []

with open("example1.txt") as inputFile:
    for line in inputFile:
        weightArray.append(int(line))

weightPerGroup = sum(weightArray) / 3

print "Weights are : ", weightArray, "with a total weight of", sum(weightArray), "with", weightPerGroup, "per group"

# print "Combinations", itertools.combinations(weightArray)
permutations = list(itertools.permutations(weightArray))
print "Possible permutations", len(permutations)

for chance in permutations:
    group1 = []
    group2 = []
    group3 = []
    for number in chance:
        if sum(group1) < weightPerGroup:
            group1.append(number)
        elif sum(group2) < weightPerGroup:
            group2.append(number)
        elif sum(group3) < weightPerGroup:
            group3.append(number)

        # if group1 > weightPerGroup or group2 > weightPerGroup or group3 > weightPerGroup:
        #     continue
    if sum(group1) == weightPerGroup and sum(group2) == weightPerGroup and sum(group3) == weightPerGroup:
        workingArray.append([group1, group2, group3])

print "Finished with", len(workingArray), "solutions"
# Now only get solutions in descending order
orderedArray = []
for workingChance in workingArray:
    orderedArray.append([sorted(workingChance[0]), sorted(workingChance[1]), sorted( workingChance[2])])

print "Found", len(orderedArray)
print "Unique", len(set(orderedArray))

end = time.clock()

print "Time taken", end - start, "seconds"
