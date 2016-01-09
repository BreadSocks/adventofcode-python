data = open("input.txt").read()
santaPoints = ["0,0"]
robotPoints = ["0,0"]


def go_to_next_house(array, next_character):
    previous_location = array[len(array) - 1]
    previous_point = map(int, previous_location.split(","))
    x_axis = previous_point[0]
    y_axis = previous_point[1]
    if next_character == "^":
        y_axis += 1
    elif next_character == ">":
        x_axis += 1
    elif next_character == "v":
        y_axis -= 1
    elif next_character == "<":
        x_axis -= 1
    house = str(x_axis) + "," + str(y_axis)
    array.append(house)

for index, character in enumerate(data):
    if index % 2 == 0:
        go_to_next_house(santaPoints, character)
    else:
        go_to_next_house(robotPoints, character)

totalList = santaPoints + robotPoints
print "Houses that receive at least one present : ", len(set(totalList))
