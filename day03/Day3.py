def get_next_house(x_axis, y_axis, character):
    if character == "^":
        y_axis += 1
    elif character == ">":
        x_axis += 1
    elif character == "v":
        y_axis -= 1
    elif character == "<":
        x_axis -= 1
    return str(x_axis) + "," + str(y_axis)


class SantaRoute:
    def __init__(self):
        self.housePoints = ["0,0"]

    def go_to_next_house(self, character):
        previous_location = self.housePoints[-1]
        previous_point = map(int, previous_location.split(","))
        house = get_next_house(previous_point[0], previous_point[1], character)
        self.housePoints.append(house)

    def number_of_unique_houses(self):
        return len(set(self.housePoints))
