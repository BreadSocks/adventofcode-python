from Day15 import Ingredient, Measure, Recipe
import itertools

ingredientArray = []
# read file
with open("input.txt") as inputFile:
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

recipes = []

for measurements in allRecipeMeasurements:
    measurements_array = []
    for measurement_index, measurement in enumerate(measurements):
        chosen_ingredient = ingredientArray[measurement_index]
        chosen_measurement = measurements[measurement_index]
        measure = Measure(chosen_ingredient, chosen_measurement)
        measurements_array.append(measure)
        print measure.ingredient.name, measure.measurement_score_array()
    print "\n"
    recipe = Recipe(measurements_array)
    recipes.append(recipe)

recipe_scores = []
for recipe in recipes:
    recipe_scores.append(recipe.recipe_score())

print max(recipe_scores)
