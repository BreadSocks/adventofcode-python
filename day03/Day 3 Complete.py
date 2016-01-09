from Day3 import SantaRoute
data = open("input.txt").read()
santaPoints = SantaRoute()
robotPoints = SantaRoute()
aloneSantaPoints = SantaRoute()

for index, character in enumerate(data):
    # part 1
    aloneSantaPoints.go_to_next_house(character)

    # part 2
    if index % 2 == 0:
        santaPoints.go_to_next_house(character)
    else:
        robotPoints.go_to_next_house(character)

totalList = santaPoints.housePoints + robotPoints.housePoints
print "Part 1 Answer : Houses that receive at least one present :", aloneSantaPoints.number_of_unique_houses()
print "Part 2 Answer : Houses that receive at least one present :", len(set(totalList))
