class SantaRoute:
    def __init__(self):
        self.housePoints = ["0,0"]

    def go_to_next_house(self, character):
        previous_location = self.housePoints[-1]
        previous_point = map(int, previous_location.split(","))
        x_axis = previous_point[0]
        y_axis = previous_point[1]
        if character == "^":
            y_axis += 1
        elif character == ">":
            x_axis += 1
        elif character == "v":
            y_axis -= 1
        elif character == "<":
            x_axis -= 1
        house = str(x_axis) + "," + str(y_axis)
        self.housePoints.append(house)

    def number_of_unique_houses(self):
        return len(set(self.housePoints))
