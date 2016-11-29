from Day15 import Ingredient, Measure, Recipe
import itertools

ingredientArray = []
# read file
with open("example.txt") as inputFile:
    for line in inputFile:
        firstSplit = line.split(": ")
        name = firstSplit[0]
        scoreArray = []
        secondSplit = firstSplit[1].split(", ")
        for key_value in secondSplit:
            scoreArray.append(int(key_value.split(" ")[1]))
        ingredient = Ingredient(name, scoreArray)
        ingredientArray.append(ingredient)

targetCombinationArray = []

combinations = itertools.combinations_with_replacement(range(101), len(ingredientArray))
for index in combinations:
    if sum(index) == 100:
        targetCombinationArray.append(index)

targetCombinationArray = list(set(targetCombinationArray))
allRecipeMeasurements = []

for measurement in targetCombinationArray:
    allRecipeMeasurements.extend(list(itertools.permutations(measurement)))

measurementArray = []

for measurements in allRecipeMeasurements:
    for measurement_index in len(measurements):
        chosen_ingredient = ingredientArray[measurement_index]
        chosen_measurement = measurements[measurement_index]
        measure = Measure(chosen_ingredient, chosen_measurement)


