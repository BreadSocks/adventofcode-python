import re
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

for replacement in listOfReplacements:
    parts = str(replacement).split(" => ")
    matchArray = [m.start() for m in re.finditer(parts[0], molecule)]
    for match in matchArray:
        newMolecule = molecule[:match] + molecule[match:].replace(parts[0], parts[1], 1)
        moleculeArray.append(newMolecule)

print moleculeArray
print list(set(moleculeArray))

print "Found", len(moleculeArray), "results and", len(list(set(moleculeArray))), "unique results"
