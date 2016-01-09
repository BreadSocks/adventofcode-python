from Day3 import SantaRoute
data = open("input.txt").read()
santaPoints = SantaRoute()
robotPoints = SantaRoute()

for index, character in enumerate(data):
    if index % 2 == 0:
        santaPoints.go_to_next_house(character)
    else:
        robotPoints.go_to_next_house(character)

totalList = santaPoints.housePoints + robotPoints.housePoints
print "Houses that receive at least one present : ", len(set(totalList))
