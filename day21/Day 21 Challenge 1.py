import copy
bossHitPoints = 0
bossDamage = 0
bossArmour = 0

playerHitPoints = 100
playerDamage = 0
playerArmour = 0

weaponArray = []
armourArray = []
ringArray = []

costArray = []

def initialiseboss():
    global bossHitPoints
    global bossDamage
    global bossArmour
    with open("input.txt") as inputFile:
        for line in inputFile:
            if line.startswith("Hit Points"):
                bossHitPoints = int(line.replace("Hit Points: ", ""))
            elif line.startswith("Damage"):
                 bossDamage = int(line.replace("Damage: ", ""))
            elif line.startswith("Armor"):
                bossArmour = int(line.replace("Armor: ", ""))

def initialiseitems():
    global weaponArray, armourArray, ringArray
    weaponArray = [["Dagger", 8, 4, 0], ["Shortsword", 10, 5, 0], ["Warhammer", 25, 6, 0], ["Longsword", 40, 7, 0], ["Greataxe", 74, 8, 0]]
    # armourArray = [["Leather", 13, 0, 1], ["Chainmal", 31, 0, 2], ["Splintmail", 53, 0, 3], ["Bandedmail", 75, 0, 4], ["Platemail", 102, 0, 5]]
    armourArray = [["No Armour", 0, 0, 0], ["Leather", 13, 0, 1], ["Chainmal", 31, 0, 2], ["Splintmail", 53, 0, 3], ["Bandedmail", 75, 0, 4], ["Platemail", 102, 0, 5]]
    # ringArray = [["Damage +1", 25, 1, 0], ["Damage +2", 50, 2, 0], ["Damage +3", 100, 3, 0], ["Defense +1", 20, 0, 1], ["Defense +2", 40, 0, 2], ["Defense +3", 80, 0, 3]]
    ringArray = [["No LH Ring", 0, 0, 0], ["No RH Ring", 0, 0, 0], ["Damage +1", 25, 1, 0], ["Damage +2", 50, 2, 0], ["Damage +3", 100, 3, 0], ["Defense +1", 20, 0, 1], ["Defense +2", 40, 0, 2], ["Defense +3", 80, 0, 3]]


def simulate(health, damage, armour, bossHealth, bossDamage, bossArmour):
    playersTurn = True

    while health > 0 and bossHealth > 0:
        if playersTurn:
            bossHealth -= (damage - bossArmour)
            playersTurn = False
        else:
            health -= (bossDamage - armour)
            playersTurn = True

    if health > bossHealth:
        print "Player Won!\nPlayer Health : ", health, "\nBoss Health : ", bossHealth
        return True
    else:
        print "Player Lost!"
        return False

initialiseboss()
initialiseitems()
print "Boss has Hit Points :", bossHitPoints, "Damage :", bossDamage, "Armour :", bossArmour

for weapon in range(len(weaponArray)):
    chosenWeapon = weaponArray[weapon]
    for armour in range(len(armourArray)):
        chosenArmour = armourArray[armour]
        for ring in range(len(ringArray)):
            chosenRing = ringArray[ring]
            secondaryList = list(ringArray)
            secondaryList.remove(ringArray[ring])
            for nextRing in range(len(secondaryList)):
                secondRing = secondaryList[nextRing]
                print chosenWeapon[0], chosenArmour[0], chosenRing[0], secondRing[0]
                newDamage = chosenWeapon[2] + chosenRing[2] + secondRing[2]
                newArmour = chosenArmour[3] + chosenRing[3] + secondRing[3]
                success = simulate(copy.copy(playerHitPoints), newDamage, newArmour, copy.copy(bossHitPoints), copy.copy(bossDamage), copy.copy(bossArmour))
                if (success):
                    print "Found good combination"
                    costArray.append(chosenWeapon[1] + chosenArmour[1] + chosenRing[1] + secondRing[1])


# simulate(copy.copy(playerHitPoints), copy.copy(playerDamage), copy.copy(playerArmour),
#          copy.copy(bossHitPoints), copy.copy(bossDamage), copy.copy(bossArmour))
print "Lowest price is :", min(costArray)