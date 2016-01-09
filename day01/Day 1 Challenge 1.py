data = open("input.txt").read()
counter = 0
for character in data:
    if character == '(':
        counter += 1
    else:
        counter -= 1

print "Answer : He would arrive on the " + str(counter) + "th floor"
