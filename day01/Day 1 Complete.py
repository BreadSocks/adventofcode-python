data = open("input.txt").read()
counter = 0
basementStep = -1  # a value the index can't reach
for index, character in enumerate(data):
    if character == '(':
        counter += 1
    else:
        counter -= 1

        if counter == -1 and basementStep == -1:
            basementStep = index + 1

print "Part 1 Answer : He would arrive on the", str(counter) + "th floor"
print "Part 2 Answer : It took", basementStep, "visits before hitting the basement"
