from Day3 import SantaRoute
data = open("input.txt").read()
gridPoints = SantaRoute()
for character in data:
    gridPoints.go_to_next_house(character)

print "Houses that receive at least one present :", gridPoints.number_of_unique_houses()
