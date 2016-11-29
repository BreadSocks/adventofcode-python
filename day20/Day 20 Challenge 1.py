goal = 29000000
highestPresentCount = 0
houseDictionary = {}
house = 1
# house = 665279

while highestPresentCount < goal:
    presentCount = 0
    for elf in range(house):
        if house % (elf + 1) == 0:
            presentCount += (elf + 1) * 10

    houseDictionary[house] = presentCount
    print "House", house, "has", presentCount, "presents"
    highestPresentCount = presentCount
    house += 1
print houseDictionary
