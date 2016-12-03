class Ingredient:

    def __init__(self, ingredient_name, ingredient_array):
        self.name = ingredient_name
        self.ingredient_array = ingredient_array
        self.capacity = ingredient_array[0]
        self.durability = ingredient_array[1]
        self.flavour = ingredient_array[2]
        self.texture = ingredient_array[3]
        self.calories = ingredient_array[4]

    def __str__(self):
        return "Name : " + self.name + " Capacity : " + str(self.capacity) \
               + " Durability : " + str(self.durability) + " Flavour : " + str(self.flavour) \
               + " Texture : " + str(self.texture) + " Calories : " + str(self.calories)


class Measure:

    def __init__(self, ingredient, measure):
        self.ingredient = ingredient
        self.teaspoons = measure

    def capacity_score(self):
        return self.teaspoons * self.ingredient.capacity

    def durability_score(self):
        return self.teaspoons * self.ingredient.durability

    def flavour_score(self):
        return self.teaspoons * self.ingredient.flavour

    def texture_score(self):
        return self.teaspoons * self.ingredient.texture

    def calories_score(self):
        return self.teaspoons * self.ingredient.calories

    def measurement_score_array(self):
        measured_array = []
        for ingredient_score in self.ingredient.ingredient_array:
            measured_array.append(self.teaspoons * ingredient_score)
        return measured_array

class Recipe:

    def __init__(self, measurements_array):
        self.measurements_array = measurements_array

    def recipe_score(self):
        capacity = 0
        flavour = 0
        durability = 0
        texture = 0
        for measurement in self.measurements_array:
            capacity += measurement.capacity_score()
            flavour += measurement.flavour_score()
            durability += measurement.durability_score()
            texture += measurement.texture_score()
        if capacity < 0 or flavour < 0 or durability < 0 or texture < 0:
            return 0
        else:
            return capacity * flavour * durability * texture
