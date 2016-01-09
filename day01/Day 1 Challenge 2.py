data = open("input.txt").read()
counter = 0
for index, character in enumerate(data):
    if character == '(':
        counter += 1
    else:
        counter -= 1

        if counter == -1:
            # +1 on index as first character is 0 in array but 1 in count
            print "Answer : It took", index + 1, "visits before hitting the basement"
            break
