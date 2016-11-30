import string
alphabet = list(string.ascii_lowercase)
disallowed = ["i", "o", "l"]
# data = "abcdefgh" # correct
# data = "ghijklmn"  # gets stuck somewhere
data = "hxbxwxba"


def create_valid_password(currentpassword):
    for character in disallowed:
        if character in currentpassword:
            invalid_index = currentpassword.index(character)
            currentpasswordlist = list(currentpassword)
            # currentpasswordlist[invalid_index] = alphabet[invalid_index + 1] if invalid_index < len(alphabet) else alphabet[0]
            new_letter_index = alphabet.index(character) + 1
            currentpasswordlist[invalid_index] = alphabet[new_letter_index] if new_letter_index < len(alphabet) else \
            alphabet[0]
            for x in range(invalid_index + 1, len(currentpassword)):
                currentpasswordlist[x] = alphabet[0]
            currentpassword = "".join(currentpasswordlist)
    return currentpassword


def nextpassword(currentpassword):
    contains_invalid_letters = True
    while contains_invalid_letter(currentpassword):
        currentpassword = create_valid_password(currentpassword)
        contains_invalid_letters = contains_invalid_letter(currentpassword)


    passwordasarray = list(currentpassword)
    lettertochange = passwordasarray[len(passwordasarray) - 1]
    if lettertochange != alphabet[len(alphabet) - 1]:
        newletter = alphabet[alphabet.index(lettertochange) + 1]
        passwordasarray[len(passwordasarray) - 1] = newletter
    else:
        for n in range(len(currentpassword) - 1, 0, -1):
            if currentpassword[n] == alphabet[len(alphabet) - 1]:
                passwordasarray[n] = alphabet[0]
            else:
                passwordasarray[n] = alphabet[alphabet.index(passwordasarray[n]) + 1]
                break
    return "".join(passwordasarray)


def contains_invalid_letter(password):
    for character in disallowed:
        if character in password:
            return True
    return False


def isvalidpassword(generatedpassword):
    if generatedpassword == "ghjaabcc":
        print "found"

    foundrun = False
    firstpairindex = -1
    pairsfound = 0
    for character in generatedpassword:
        if disallowed.__contains__(character):
            return False

        if generatedpassword.index(character) < len(generatedpassword) - 2 and alphabet.index(character) < len(alphabet) - 2:
            secondcharacter = alphabet[alphabet.index(character) + 1]
            thirdcharacter = alphabet[alphabet.index(character) + 2]
            if generatedpassword.__contains__(character + secondcharacter + thirdcharacter):
                foundrun = True

        if generatedpassword.index(character) < len(generatedpassword) - 1:
            if generatedpassword.count(character + character) > 0:
                if firstpairindex == -1:
                    firstpairindex = generatedpassword.index(character + character)
                    pairsfound += 1
                elif generatedpassword.index(character + character) != firstpairindex:
                    pairsfound += 1
    return foundrun and pairsfound > 1

foundValidPassword = False
counter = 0
while foundValidPassword is False:
    data = nextpassword(data)
    foundValidPassword = isvalidpassword(data)
    counter += 1
    print data

print "Found password", data


# def getnextpassword(currentpassword):
#     print "--------------------"
#     for n in range(len(currentpassword) - 1, -1, -1):
#         listcopyofcurrentpassword = list(currentpassword)
#         charactetoincrease = currentpassword[n]
#         indexoflastletterinalpha = alphabet.index(charactetoincrease)
#         if indexoflastletterinalpha + 1 == len(alphabet):
#             newcharacter = "a"
#             listcopyofcurrentpassword[n] = newcharacter
#         else:
#             newcharacter = alphabet[indexoflastletterinalpha + 1]
#             listcopyofcurrentpassword[n] = newcharacter
#         print charactetoincrease, " -> ", newcharacter, " -> ", "".join(listcopyofcurrentpassword)
#
# getnextpassword(data)
