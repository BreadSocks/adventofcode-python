import copy

bossHitPoints = 0
bossDamage = 0

playerHitPoints = 50
playerMana = 500
playerArmour = 0

spellArray = []

costArray = []
maxCostArray = []

effectDictionary = {}
possibleVariations = 0

def initialiseboss():
    global bossHitPoints
    global bossDamage
    with open("input.txt") as inputFile:
        for line in inputFile:
            if line.startswith("Hit Points"):
                bossHitPoints = int(line.replace("Hit Points: ", ""))
            elif line.startswith("Damage"):
                bossDamage = int(line.replace("Damage: ", ""))


def initialiseitems():
    global spellArray
    # Order : Name, Mana Cost, Instant Damage, Instant Heal, Effect Length, Armour Increase, Boss Damage, Mana Recharge
    spellArray = [["Magic Missile", 53, 4, 0, 0, 0, 0, 0],
                  ["Drain", 73, 2, 2, 0, 0, 0, 0],
                  ["Shield", 113, 0, 0, 6, 7, 0, 0],
                  ["Poison", 173, 0, 0, 6, 0, 3, 0],
                  ["Recharge", 229, 0, 0, 5, 0, 0, 101]]

def simulate(playersHealth, playersArmour, playersMana, bosssHealth, bosssAttack, spellArray):
    playersTurn = True
    print spellArray
    # while playersHealth > 0 and bosssHealth > 0:

# def simulate(health, damage, armour, bossHealth, bossDamage, bossArmour):
#     playersTurn = True
#
#     while health > 0 and bossHealth > 0:
#         if playersTurn:
#             bossHealth -= (damage - bossArmour)
#             playersTurn = False
#         else:
#             health -= (bossDamage - armour)
#             playersTurn = True
#
#     if health > bossHealth:
#         print "Player Won!\nPlayer Health : ", health, "\nBoss Health : ", bossHealth
#         return True
#     else:
#         print "Player Lost!"
#         return False

initialiseboss()
initialiseitems()
print "Boss has Hit Points :", bossHitPoints, "Damage :", bossDamage

for i in range(len(spellArray)):
    firstSpell = spellArray[i]
    secondList = list(spellArray)
    secondList.remove(firstSpell)
    for j in range(len(secondList)):
        secondSpell = secondList[j]
        thirdList = list(secondList)
        thirdList.remove(secondSpell)
        for k in range(len(thirdList)):
            thirdSpell = thirdList[k]
            fourthList = list(thirdList)
            fourthList.remove(thirdSpell)
            for l in range(len(fourthList)):
                fourthSpell = fourthList[l]
                fifthList = list(fourthList)
                fifthList.remove(fourthSpell)
                for m in range(len(fifthList)):
                    fifthSpell = fifthList[m]
                    if len(fifthList) == 1:
                        possibleVariations += 1
                        print firstSpell, secondSpell, thirdSpell, fourthSpell, fifthSpell
                        chosenSpellArray = [firstSpell, secondSpell, thirdSpell, fourthSpell, fifthSpell]
                        simulate(copy.copy(playerHitPoints), copy.copy(playerArmour), copy.copy(playerMana),
                                           copy.copy(bossHitPoints), copy.copy(bossDamage), chosenSpellArray)


print "Possible Attack Patterns :", possibleVariations
