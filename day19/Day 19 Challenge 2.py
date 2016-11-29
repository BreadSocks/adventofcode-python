import re, itertools
listOfReplacements = []
moleculeLine = -1
moleculeArray = []

inputFile = open("input.txt")
for index, line, in enumerate(inputFile):
    if line == "\n":
        moleculeLine = index + 1
    elif index == moleculeLine:
        molecule = line
    else:
        listOfReplacements.append(line.replace("\n", ""))

print molecule, listOfReplacements

print "Starting allSteps"
allPermutations = itertools.permutations(listOfReplacements)
allSteps = list(allPermutations)
print "Finished allSteps"
print len(allSteps)
print "Finished length allSteps"
