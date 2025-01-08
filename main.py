import random


def shuffleAndCreateDeck():  # Shuffles the deck
    global numberOfTimesDeckHasRunOut
    numberOfTimesDeckHasRunOut += 1
    functionDeck = []
    makeDeck = cardsLeftInDiscardAndPickupPile
    while max(makeDeck) > 0:  # While there are still cards to shuffle into the deck
        randomCard = random.randint(1,
                                    makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4] + makeDeck[3] + makeDeck[2] +
                                    makeDeck[1] + makeDeck[0])  # Takes a random card
        # These next lines of code check what card was taken
        if randomCard > makeDeck[7]:
            if randomCard > makeDeck[7] + makeDeck[6]:
                if randomCard > makeDeck[7] + makeDeck[6] + makeDeck[5]:
                    if randomCard > makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4]:
                        if randomCard > makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4] + makeDeck[3]:
                            if randomCard > makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4] + makeDeck[3] + \
                                    makeDeck[2]:
                                if randomCard > makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4] + makeDeck[3] + \
                                        makeDeck[2] + makeDeck[1]:
                                    functionDeck.append(20)
                                    makeDeck[0] -= 1
                                else:
                                    functionDeck.append(18)
                                    makeDeck[1] -= 1
                            else:
                                functionDeck.append(16)
                                makeDeck[2] -= 1
                        else:
                            functionDeck.append(14)
                            makeDeck[3] -= 1
                    else:
                        functionDeck.append(12)
                        makeDeck[4] -= 1
                else:
                    functionDeck.append(10)
                    makeDeck[5] -= 1
            else:
                functionDeck.append(8)
                makeDeck[6] -= 1
        else:
            functionDeck.append(6)
            makeDeck[7] -= 1
    return functionDeck  # returns the deck


def showFieldsOfPlayer(player):  # This function shows the fields of player (the beans that player has planted)
    if player == 5:  # If player == 5, the fields shown are the trading cards
        global deck  # These next 20 lines are just in case
        global numberOfTimesDeckHasRunOut  # the deck runs out here
        if len(deck) == 0:
            if not numberOfTimesDeckHasRunOut == 2:
                if numberOfTimesDeckHasRunOut == 0:
                    print(playerBoldedColoursANSI[5] + "The deck has now run out for the first time")
                else:
                    print(playerBoldedColoursANSI[5] + "The deck has now run out for the second time")
                deck = shuffleAndCreateDeck()
            else:
                numberOfTimesDeckHasRunOut += 1
                endTheGame()
        typeOfBeansInFields[5][0] = deck.pop(0)
        if len(deck) == 0:
            if not numberOfTimesDeckHasRunOut == 2:
                if numberOfTimesDeckHasRunOut == 0:
                    print(playerBoldedColoursANSI[5] + "The deck has now run out for the first time")
                else:
                    print(playerBoldedColoursANSI[5] + "The deck has now run out for the second time")
                deck = shuffleAndCreateDeck()
            else:
                numberOfTimesDeckHasRunOut += 1
                endTheGame()
        typeOfBeansInFields[5][1] = deck.pop(0)
        tradingCards[0] = typeOfBeansInFields[5][0]
        tradingCards[1] = typeOfBeansInFields[5][1]
    else:
        print(playerColoursANSI[player] + playerNames[player] + "'s fields:")
    if numberOfPlayers > 3 or player == 5:
        field = [0, 0]  # fields are 22 spaces wide with 4 spaces in between
        # this field list is used to print multiple fields beside each other
        print(playerColoursANSI[player] + " ______________________      ______________________ ")
        print("/                      \\    /                      \\")
        print("|          1.          |    |          2.          |")
    else:
        field = [0, 0, 0]
        # this field list is used to print multiple fields beside each other
        print(playerColoursANSI[player] + " ______________________      ______________________      "
                                          "______________________ ")
        print("/                      \\    /                      \\    /                      \\")
        print("|          1.          |    |          2.          |    |          3.          |")
    for l in range(numberOfFieldsInUse):
        if len(str((typeOfBeansInFields[player])[l])) == 1:
            field[l] = "|          0" + str(typeOfBeansInFields[player][l]) + "          |"
        else:
            field[l] = "|          " + str(typeOfBeansInFields[player][l]) + "          |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
        print("|                      |    |                      |")
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
        print("|                      |    |                      |    |                      |")
    for l in range(5):  # These next lines print the text art on the cards
        for m in range(numberOfFieldsInUse):
            field[m] = "|" + ASCIIArt[typeOfBeansInFields[player][m]][l] + "|"
        if numberOfFieldsInUse == 2:
            print(str(field[0]) + "    " + str(field[1]))
        else:
            print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for l in range(numberOfFieldsInUse):
        if len(str(quantityOfBeansInFields[player][l])) == 1:
            quantity = "0" + str(quantityOfBeansInFields[player][l])
        else:
            quantity = str(quantityOfBeansInFields[player][l])
        if typeOfBeansInFields[player][l] == 0:  # These next lines print the type of bean and the quantity of that bean
            field[l] = "|                      |"
        elif typeOfBeansInFields[player][l] == 6:
            field[l] = "|  Garden Bean (" + quantity + "x)   |"
        elif typeOfBeansInFields[player][l] == 8:
            field[l] = "|    Red Bean (" + quantity + "x)    |"
        elif typeOfBeansInFields[player][l] == 10:
            field[l] = "|Black-Eyed Bean (" + quantity + "x) |"
        elif typeOfBeansInFields[player][l] == 12:
            field[l] = "|    Soy Bean (" + quantity + "x)    |"
        elif typeOfBeansInFields[player][l] == 14:
            field[l] = "|   Green Bean (" + quantity + "x)   |"
        elif typeOfBeansInFields[player][l] == 16:
            field[l] = "|   Stink Bean (" + quantity + "x)   |"
        elif typeOfBeansInFields[player][l] == 18:
            field[l] = "|   Chili Bean (" + quantity + "x)   |"
        else:
            field[l] = "|   Blue Bean (" + quantity + "x)    |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for l in range(numberOfFieldsInUse):  # The rest of this function prints the bottom of the cards
        if typeOfBeansInFields[player][l] == 0:
            field[l] = "|                      |"
        elif typeOfBeansInFields[player][l] == 6:
            field[l] = "|                      |"
        else:
            field[l] = "|                  O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for l in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][l] == 0:
            field[l] = "|                      |"
        elif typeOfBeansInFields[player][l] == 6:
            field[l] = "|             O        |"
        else:
            field[l] = "|             O    O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for l in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][l] == 0:
            field[l] = "|                      |"
        elif typeOfBeansInFields[player][l] == 6:
            field[l] = "|        O    O        |"
        else:
            field[l] = "|        O    O    O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for l in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][l] == 0:
            field[l] = "|                      |"
        elif typeOfBeansInFields[player][k] == 6:
            field[l] = "|        O    O        |"
        else:
            field[l] = "|   O    O    O    O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for l in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][l] == 0:
            field[l] = "|                      |"
        elif typeOfBeansInFields[player][l] == 6:
            field[l] = "|        2    3        |"
        elif typeOfBeansInFields[player][l] == 8:
            field[l] = "|   2    3    4    5   |"
        elif typeOfBeansInFields[player][l] == 10:
            field[l] = "|   2    4    5    6   |"
        elif typeOfBeansInFields[player][l] == 12:
            field[l] = "|   2    4    6    7   |"
        elif typeOfBeansInFields[player][l] == 14:
            field[l] = "|   3    5    6    7   |"
        elif typeOfBeansInFields[player][l] == 16:
            field[l] = "|   3    5    7    8   |"
        elif typeOfBeansInFields[player][l] == 18:
            field[l] = "|   3    6    8    9   |"
        elif typeOfBeansInFields[player][l] == 20:
            field[l] = "|   4    6    8   10   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
        print("\\______________________/    \\______________________/")
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
        print("\\______________________/    \\______________________/    \\______________________/")


def showHandOfPlayer(player):  # Shows what cards player has in their hand
    for l in range(len(playerHands[player])):
        if playerHands[player][l] == 6:
            print(playerColoursANSI[player] + str(l + 1) + ". Garden Bean (6)")
        elif playerHands[player][l] == 8:
            print(playerColoursANSI[player] + str(l + 1) + ". Red Bean (8)")
        elif playerHands[player][l] == 10:
            print(playerColoursANSI[player] + str(l + 1) + ". Black-Eyed Bean (10)")
        elif playerHands[player][l] == 12:
            print(playerColoursANSI[player] + str(l + 1) + ". Soy Bean (12)")
        elif playerHands[player][l] == 14:
            print(playerColoursANSI[player] + str(l + 1) + ". Green Bean (14)")
        elif playerHands[player][l] == 16:
            print(playerColoursANSI[player] + str(l + 1) + ". Stink Bean (16)")
        elif playerHands[player][l] == 18:
            print(playerColoursANSI[player] + str(l + 1) + ". Chili Bean (18)")
        elif playerHands[player][l] == 20:
            print(playerColoursANSI[player] + str(l + 1) + ". Blue Bean (20)")


def harvestBeans(player, field):  # Harvests all beans in player's field
    if typeOfBeansInFields[player][field] == 6:
        if quantityOfBeansInFields[player][field] == 1:
            print(
                playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Garden Bean")
        else:
            print(
                playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Garden Beans")
        if quantityOfBeansInFields[player][field] >= 2:
            if quantityOfBeansInFields[player][field] >= 3:
                coins[player] += 3
                cardsLeftInDiscardAndPickupPile[7] -= 3
                print(playerNames[player] + " earned 3 coins!")
            else:
                coins[player] += 2
                cardsLeftInDiscardAndPickupPile[7] -= 2
                print(playerNames[player] + " earned 2 coins!")
    elif typeOfBeansInFields[player][field] == 8:
        if quantityOfBeansInFields[player][field] == 1:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Red Bean")
        else:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Red Beans")
        if quantityOfBeansInFields[player][field] >= 2:
            if quantityOfBeansInFields[player][field] >= 3:
                if quantityOfBeansInFields[player][field] >= 4:
                    if quantityOfBeansInFields[player][field] >= 5:
                        coins[player] += 4
                        cardsLeftInDiscardAndPickupPile[6] -= 4
                        print(playerNames[player] + " earned 4 coins!")
                    else:
                        coins[player] += 3
                        cardsLeftInDiscardAndPickupPile[6] -= 3
                        print(playerNames[player] + " earned 3 coins!")
                else:
                    coins[player] += 2
                    cardsLeftInDiscardAndPickupPile[6] -= 2
                    print(playerNames[player] + " earned 2 coins!")
            else:
                coins[player] += 1
                cardsLeftInDiscardAndPickupPile[6] -= 1
                print(playerNames[player] + " earned 1 coin!")
    elif typeOfBeansInFields[player][field] == 10:
        if quantityOfBeansInFields[player][field] == 1:
            print(playerNames[player] + " is harvesting " + str(
                quantityOfBeansInFields[player][field]) + " Black-Eyed Bean")
        else:
            print(playerNames[player] + " is harvesting " + str(
                quantityOfBeansInFields[player][field]) + " Black-Eyed Beans")
        if quantityOfBeansInFields[player][field] >= 2:
            if quantityOfBeansInFields[player][field] >= 4:
                if quantityOfBeansInFields[player][field] >= 5:
                    if quantityOfBeansInFields[player][field] >= 6:
                        coins[player] += 4
                        cardsLeftInDiscardAndPickupPile[5] -= 4
                        print(playerNames[player] + " earned 4 coins!")
                    else:
                        coins[player] += 3
                        cardsLeftInDiscardAndPickupPile[5] -= 3
                        print(playerNames[player] + " earned 3 coins!")
                else:
                    coins[player] += 2
                    cardsLeftInDiscardAndPickupPile[5] -= 2
                    print(playerNames[player] + " earned 2 coins!")
            else:
                coins[player] += 1
                cardsLeftInDiscardAndPickupPile[5] -= 1
                print(playerNames[player] + " earned 1 coins!")
    elif typeOfBeansInFields[player][field] == 12:
        if quantityOfBeansInFields[player][field] == 1:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Soy Bean")
        else:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Soy Beans")
        if quantityOfBeansInFields[player][field] >= 2:
            if quantityOfBeansInFields[player][field] >= 4:
                if quantityOfBeansInFields[player][field] >= 6:
                    if quantityOfBeansInFields[player][field] >= 7:
                        coins[player] += 4
                        cardsLeftInDiscardAndPickupPile[4] -= 4
                        print(playerNames[player] + " earned 4 coins!")
                    else:
                        coins[player] += 3
                        cardsLeftInDiscardAndPickupPile[4] -= 3
                        print(playerNames[player] + " earned 3 coins!")
                else:
                    coins[player] += 2
                    cardsLeftInDiscardAndPickupPile[4] -= 2
                    print(playerNames[player] + " earned 2 coins!")
            else:
                coins[player] += 1
                cardsLeftInDiscardAndPickupPile[4] -= 1
                print(playerNames[player] + " earned 1 coin!")
    elif typeOfBeansInFields[player][field] == 14:
        if quantityOfBeansInFields[player][field] == 1:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Green Bean")
        else:
            print(
                playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Green Beans")
        if quantityOfBeansInFields[player][field] >= 3:
            if quantityOfBeansInFields[player][field] >= 5:
                if quantityOfBeansInFields[player][field] >= 6:
                    if quantityOfBeansInFields[player][field] >= 7:
                        coins[player] += 4
                        cardsLeftInDiscardAndPickupPile[3] -= 4
                        print(playerNames[player] + " earned 4 coins!")
                    else:
                        coins[player] += 3
                        cardsLeftInDiscardAndPickupPile[3] -= 3
                        print(playerNames[player] + " earned 3 coins!")
                else:
                    coins[player] += 2
                    cardsLeftInDiscardAndPickupPile[3] -= 2
                    print(playerNames[player] + " earned 2 coins!")
            else:
                coins[player] += 1
                cardsLeftInDiscardAndPickupPile[3] -= 1
                print(playerNames[player] + " earned 1 coin!")
    elif typeOfBeansInFields[player][field] == 16:
        if quantityOfBeansInFields[player][field] == 1:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Stink Bean")
        else:
            print(
                playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Stink Beans")
        if quantityOfBeansInFields[player][field] >= 3:
            if quantityOfBeansInFields[player][field] >= 5:
                if quantityOfBeansInFields[player][field] >= 7:
                    if quantityOfBeansInFields[player][field] >= 8:
                        coins[player] += 4
                        cardsLeftInDiscardAndPickupPile[2] -= 4
                        print(playerNames[player] + " earned 4 coins!")
                    else:
                        coins[player] += 3
                        cardsLeftInDiscardAndPickupPile[2] -= 3
                        print(playerNames[player] + " earned 3 coins!")
                else:
                    coins[player] += 2
                    cardsLeftInDiscardAndPickupPile[2] -= 2
                    print(playerNames[player] + " earned 2 coins!")
            else:
                coins[player] += 1
                cardsLeftInDiscardAndPickupPile[2] -= 1
                print(playerNames[player] + " earned 1 coin!")
    elif typeOfBeansInFields[player][field] == 18:
        if quantityOfBeansInFields[player][field] == 1:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Chili Bean")
        else:
            print(
                playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Chili Beans")
        if quantityOfBeansInFields[player][field] >= 3:
            if quantityOfBeansInFields[player][field] >= 6:
                if quantityOfBeansInFields[player][field] >= 8:
                    if quantityOfBeansInFields[player][field] >= 9:
                        coins[player] += 4
                        cardsLeftInDiscardAndPickupPile[1] -= 4
                        print(playerNames[player] + " earned 4 coins!")
                    else:
                        coins[player] += 3
                        cardsLeftInDiscardAndPickupPile[1] -= 3
                        print(playerNames[player] + " earned 3 coins!")
                else:
                    coins[player] += 2
                    cardsLeftInDiscardAndPickupPile[1] -= 2
                    print(playerNames[player] + " earned 2 coins!")
            else:
                coins[player] += 1
                cardsLeftInDiscardAndPickupPile[1] -= 1
                print(playerNames[player] + " earned 1 coin!")
    elif typeOfBeansInFields[player][field] == 20:
        if quantityOfBeansInFields[player][field] == 1:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Blue Bean")
        else:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Blue Beans")
        if quantityOfBeansInFields[player][field] >= 4:
            if quantityOfBeansInFields[player][field] >= 6:
                if quantityOfBeansInFields[player][field] >= 8:
                    if quantityOfBeansInFields[player][field] >= 10:
                        coins[player] += 4
                        cardsLeftInDiscardAndPickupPile[0] -= 4
                        print(playerNames[player] + " earned 4 coins!")
                    else:
                        coins[player] += 3
                        cardsLeftInDiscardAndPickupPile[0] -= 3
                        print(playerNames[player] + " earned 3 coins!")
                else:
                    coins[player] += 2
                    cardsLeftInDiscardAndPickupPile[0] -= 2
                    print(playerNames[player] + " earned 2 coins!")
            else:
                coins[player] += 1
                cardsLeftInDiscardAndPickupPile[0] -= 1
                print(playerNames[player] + " earned 1 coin!")
    quantityOfBeansInFields[player][field] = 0  # Empties that
    typeOfBeansInFields[player][field] = 0  # field


def decideWhereToPlantBean(player, bean):  # How the AI decides where to plant its beans
    global response
    response = "undecided"
    if bean in typeOfBeansInFields[player]:  # If the AI has a field that already has the same kind of bean,
        response = typeOfBeansInFields[player].index(bean)  # then plant the bean there
    else:
        for l in range(numberOfFieldsInUse):
            if quantityOfBeansInFields[player][l] > 0:
                if maxQuantityOfBeans[typeOfBeansInFields[player][l]] <= quantityOfBeansInFields[playerTurn][
                    l]:               # If the AI has a field that has the maximum amount of beans,
                    response = l + 1  # then plant the bean there
                    break
    if response == "undecided":
        if numberOfFieldsInUse == 2:
            if quantityOfBeansInFields[player][0] == 0 or quantityOfBeansInFields[player][
                1] == 0:  # If the AI has an empty field,
                response = quantityOfBeansInFields[player].index(0) + 1  # then plant the bean there
        else:
            if quantityOfBeansInFields[player][0] == 0 or quantityOfBeansInFields[player][1] == 0 or \
                    quantityOfBeansInFields[player][1] == 0:  # The same two lines (almost),
                response = quantityOfBeansInFields[player].index(0) + 1  # but just for using three fields
    if response == "undecided":
        if numberOfFieldsInUse == 2:
            if minQuantityOfBeans[typeOfBeansInFields[player][0]] <= quantityOfBeansInFields[player][0] and \
                    minQuantityOfBeans[typeOfBeansInFields[player][1]] <= quantityOfBeansInFields[player][
                1]:  # If the AI gains coins no matter where it harvests,
                if maxQuantityOfBeans[typeOfBeansInFields[player][0]] - quantityOfBeansInFields[player][0] < \
                        maxQuantityOfBeans[typeOfBeansInFields[player][1]] - quantityOfBeansInFields[player][
                    1]:  # the AI will harvest the beans that are closest to the max
                    response = 1
                else:
                    response = 2
        elif minQuantityOfBeans[typeOfBeansInFields[player][0]] <= quantityOfBeansInFields[player][0] and \
                minQuantityOfBeans[typeOfBeansInFields[player][1]] <= quantityOfBeansInFields[player][1] and \
                minQuantityOfBeans[typeOfBeansInFields[player][2]] <= quantityOfBeansInFields[player][2]:
            if maxQuantityOfBeans[typeOfBeansInFields[player][0]] - quantityOfBeansInFields[player][0] < \
                    maxQuantityOfBeans[typeOfBeansInFields[player][1]] - quantityOfBeansInFields[player][1]:
                if maxQuantityOfBeans[typeOfBeansInFields[player][0]] - quantityOfBeansInFields[player][0] < \
                        maxQuantityOfBeans[typeOfBeansInFields[player][2]] - quantityOfBeansInFields[player][2]:
                    response = 1
                else:
                    response = 2
            elif maxQuantityOfBeans[typeOfBeansInFields[player][2]] - quantityOfBeansInFields[player][2] < \
                    maxQuantityOfBeans[typeOfBeansInFields[player][1]] - quantityOfBeansInFields[player][1]:
                response = 3
            else:
                response = 2
    if response == "undecided":  # If the AI still hasn't decided where to plant its beans,
        if numberOfFieldsInUse == 2:
            if abs(quantityOfBeansInFields[player][0] - minQuantityOfBeans[typeOfBeansInFields[player][0]]) > abs(
                    quantityOfBeansInFields[player][1] - minQuantityOfBeans[typeOfBeansInFields[player][
                        1]]):  # the AI will plant its beans in the field where the beans are the farthest away from the minimum
                response = 1
            else:
                response = 2
        elif abs(quantityOfBeansInFields[player][0] - minQuantityOfBeans[typeOfBeansInFields[player][0]]) > abs(
                quantityOfBeansInFields[player][1] - minQuantityOfBeans[typeOfBeansInFields[player][1]]):
            if abs(quantityOfBeansInFields[player][2] - minQuantityOfBeans[typeOfBeansInFields[player][2]]) > abs(
                    quantityOfBeansInFields[player][0] - minQuantityOfBeans[typeOfBeansInFields[player][0]]):
                response = 3
            else:
                response = 1
        elif abs(quantityOfBeansInFields[player][2] - minQuantityOfBeans[typeOfBeansInFields[player][2]]) > abs(
                quantityOfBeansInFields[player][1] - minQuantityOfBeans[typeOfBeansInFields[player][1]]):
            response = 3
        else:
            response = 2
    print(AIResponseColoursANSI[playerTurn] + str(response))


def checkForHacks():  # Checks if the response is valid
    goodResponse = False
    global response
    while not goodResponse:
        if len(response) > 0:
            if response[-1] == "!":
                response = response[:-1]
            if responseExpected == "y/n":
                if response.lower() in yes:
                    response = "yes"
                if response.lower() in no:
                    response = "no"
            if responseExpected == "int" and response in numbers:
                response = numbers.index(response)
            if str(response).isdigit():
                if (not responseExpected == "int" or int(response) > responseMax or int(
                        response) < responseMin or responseCantBe == response) and not (
                        response in playerNames and responseExpected == "name"):
                    checkForHacksBodyCode(response)
                else:
                    goodResponse = True
            elif (responseExpected == "name" and response not in playerNames) or (
                    responseExpected == "y/n" and not response.lower() == "yes" and not response.lower() == "no") or responseExpected == "int":
                checkForHacksBodyCode(response)
            else:
                goodResponse = True
        else:
            response = input(response)


def checkForHacksBodyCode(command):  # Checks if the response is a command (like "/checkStats") and then asks the user for another input
    global response
    global forcedEnd
    if command == "/help":
        print(playerColoursANSI[5] + "/checkStats - see some of the game's current stats")
        print("/endGame - end the game")
    elif command.lower() == "/endgame":  # if this command, end the game
        forcedEnd = True
        endTheGame()
    elif command.lower() == "/checkstats":  # if this command, print out a bunch of stats like everyone's coins
        print(playerColoursANSI[playerTurn] + "Current player: " + playerNames[playerTurn])
        print(playerColoursANSI[startingPlayer] + "Starting player: " + playerNames[startingPlayer])
        print(playerColoursANSI[5] + "Coins of players:")
        print(playerColoursANSI[0] + playerNames[0] + ": " + str(coins[0]))
        print(playerColoursANSI[1] + playerNames[1] + ": " + str(coins[1]))
        print(playerColoursANSI[2] + playerNames[2] + ": " + str(coins[2]))
        if numberOfPlayers >= 4:
            print(playerColoursANSI[3] + playerNames[3] + ": " + str(coins[3]))
        if numberOfPlayers >= 5:
            print(playerColoursANSI[4] + playerNames[4] + ": " + str(coins[4]))
        print(playerColoursANSI[5] + "Number of times deck has run out: " + str(numberOfTimesDeckHasRunOut))
    response = input()


def endTheGame():
    global forcedEnd
    if forcedEnd:  # if someone typed "/endGame"
        print(playerColoursANSI[5] + "The game has been ended.")
    else:
        print("The deck has run out for the third and final time. The game is now over.")
    print("All beans in all players' fields are now being harvested")
    for l in range(numberOfPlayers):
        for m in range(numberOfFieldsInUse):
            harvestBeans(l, m)
    actualCoins = coins
    if "Evan" in playerNames:  # Nothing to see here
        actualCoins[playerNames.index("Evan")] -= 1000
    coinsInOrder = []
    positionsInReverseOrder = []
    for l in range(numberOfPlayers):  # Figures out what position each of the players are in (based on their coins)
        coinsInOrder.append(min(coins))  # Takes the lowest value and puts it into this list
        positionsInReverseOrder.append(int(coins.index(min(coins))))  # Takes the player that had the lowest # of coins and puts it into this list
        coins[coins.index(min(coins))] += 9999999999999999999999  # Increases the lowest value of coins so that in the next loop, the program finds the 2nd lowest value (and 3rd and so on)
    print("Press enter to go through the results")
    input()
    if numberOfPlayers >= 5:
        print(playerColoursANSI[5] + "In fifth place...")
        input()
        if coinsInOrder[0] == 1:
            print(playerColoursANSI[positionsInReverseOrder[0]] + "is " + playerNames[
                positionsInReverseOrder[0]] + " with 1 coin")
        else:
            print(playerColoursANSI[positionsInReverseOrder[0]] + "is " + playerNames[
                positionsInReverseOrder[0]] + " with " + str(coinsInOrder[0]) + " coins")
        input()
    if numberOfPlayers >= 4:
        print(playerColoursANSI[5] + "In fourth place...")
        input()
        if coinsInOrder[numberOfPlayers - 4] == 1:
            print(playerColoursANSI[positionsInReverseOrder[numberOfPlayers - 4]] + "is " + playerNames[
                positionsInReverseOrder[numberOfPlayers - 4]] + " with 1 coin")
        else:
            print(playerColoursANSI[positionsInReverseOrder[numberOfPlayers - 4]] + "is " + playerNames[
                positionsInReverseOrder[numberOfPlayers - 4]] + " with " + str(coinsInOrder[0]) + " coins")
        input()
    print(playerColoursANSI[5] + "In third place...")
    input()
    if coinsInOrder[numberOfPlayers - 3] == 1:
        print(playerColoursANSI[positionsInReverseOrder[numberOfPlayers - 3]] + "is " + playerNames[
            positionsInReverseOrder[numberOfPlayers - 3]] + " with 1 coin")
    else:
        print(playerColoursANSI[positionsInReverseOrder[numberOfPlayers - 3]] + "is " + playerNames[
            positionsInReverseOrder[numberOfPlayers - 3]] + " with " + str(coinsInOrder[0]) + " coins")
    input()
    print(playerColoursANSI[5] + "In second place...")
    input()
    if coinsInOrder[numberOfPlayers - 2] == 1:
        print(playerColoursANSI[positionsInReverseOrder[numberOfPlayers - 2]] + "is " + playerNames[
            positionsInReverseOrder[numberOfPlayers - 2]] + " with 1 coin")
    else:
        print(playerColoursANSI[positionsInReverseOrder[numberOfPlayers - 2]] + "is " + playerNames[
            positionsInReverseOrder[numberOfPlayers - 2]] + " with " + str(coinsInOrder[0]) + " coins")
    input()
    print(playerColoursANSI[positionsInReverseOrder[numberOfPlayers - 1]] + "That means that " + playerNames[
        positionsInReverseOrder[numberOfPlayers - 1]] + " won!")
    if coinsInOrder[numberOfPlayers - 1] == 1:
        print(playerNames[positionsInReverseOrder[numberOfPlayers - 1]] + " won with one" + str(
            coinsInOrder[numberOfPlayers - 1]) + " coin!")
    else:
        print(playerNames[positionsInReverseOrder[numberOfPlayers - 1]] + " won with " + str(
            coinsInOrder[numberOfPlayers - 1]) + " coins!")
    
    if "Evan" in playerNames and 1 == 0:  # Nothing to see here. It doesn't work anyways for some reason, so I've stopped it from running with the "1 == 0"
        input()
        print(playerColoursANSI[5] + "I'm kidding :)")
        coinsInOrder = []
        positionsInReverseOrder = []
        for l in range(numberOfPlayers):
            coinsInOrder.append(min(actualCoins))
            positionsInReverseOrder.append(int(actualCoins.index(min(actualCoins))))
            actualCoins[actualCoins.index(min(actualCoins))] += 9999999999999999999999
        input()
        print("Here are the real results:")
        if numberOfPlayers >= 5:
            print("5. " + playerNames[positionsInReverseOrder[numberOfPlayers - 5]] + " with " + str(
                coinsInOrder[numberOfPlayers - 5]) + "coins")
        if numberOfPlayers >= 4:
            print("4. " + playerNames[positionsInReverseOrder[numberOfPlayers - 4]] + " with " + str(
                coinsInOrder[numberOfPlayers - 4]) + "coins")
        print("3. " + playerNames[positionsInReverseOrder[numberOfPlayers - 3]] + " with " + str(
            coinsInOrder[numberOfPlayers - 3]) + "coins")
        print("2. " + playerNames[positionsInReverseOrder[numberOfPlayers - 2]] + " with " + str(
            coinsInOrder[numberOfPlayers - 2]) + "coins")
        print("1. " + playerNames[positionsInReverseOrder[numberOfPlayers - 1]] + " with " + str(
            coinsInOrder[numberOfPlayers - 1]) + "coins")
    exit()  # Ends the code


forcedEnd = False
numberOfTimesDeckHasRunOut = -1
playerColourNames = ["red", "blue", "green", "yellow", "purple", "white", "black"]
# Code for the coloured text
playerColoursANSI = ["\033[1;31;40m", "\033[1;34;40m", "\033[1;32;40m", "\033[1;33;40m", "\033[1;35;40m",
                     "\033[1;37;40m", "\033[1;30;47m"]
playerBoldedColoursANSI = ["\033[1;30;41m", "\033[1;30;44m", "\033[1;30;42m", "\033[1;30;43m", "\033[1;30;45m",
                           "\033[1;30;47"]
AIResponseColoursANSI = ["\033[0;31;40m", "\033[0;34;40m", "\033[0;32;40m", "\033[0;33;40m", "\033[0;35;40m"]
cardsLeftInDiscardAndPickupPile = [20, 18, 16, 14, 12, 10, 8, 6]
cardNames = [0, 1, 2, 3, 4, 5, "Garden Bean", 7, "Red Bean", 9, "Black-eyed Bean", 11, "Soy Bean", 13, "Green Bean", 15,
             "Stink Bean", 17, "Chili Bean", 19, "Blue Bean"]
# Words that mean yes or no that can be used to respond to yes/no questions
yes = ["yes", "all right", "alright", "very well", "of course", "of course", "by all means", "sure", "certainly",
       "absolutely", "indeed", "affirmative", "agreed", "aye aye", "yeah", "ya", "yah", "yep", "yup", "uh-huh", "okay",
       "ok", "okey-dokey", "okie-dokie", "okey-doke", "yea", "yes please", "yes, please", "oui"]
no = ["no", "absolutely not", "certainly not", "most certainly not", "of course not", "under no circumstances",
      "by no means", "not at all", "negative", "never", "not really", "no thanks", "no, thanks", "nae", "nope", "nah",
      "no way", "no siree", "nay", "unfortunately not", "non"]
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
           "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
coins = [9999, 9999, 9999, 9999, 9999]
typeOfBeansInFields = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0], [0, 0], [0, 0]]
quantityOfBeansInFields = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0], [0, 0], [1, 1]]
deck = shuffleAndCreateDeck()
tradingCards = [0, 0]
responseCantBe = ""
maxQuantityOfBeans = ["These", "words", "don't", "matter,", "but", "the", 3, "numbers", 5, "do", 6, "for", 7, "the", 7,
                      "AI", 8, "players", 9, "", 10]
minQuantityOfBeans = ["These", "words", "also", "don't", "matter,", "but", 2, "the", 2, "numbers", 2, "do", 2, "for", 3,
                      "the", 3, "AI", 3, "players", 4]
cardOffers = [[], [], [], [], []]
# The next line is blank (for empty fields), the line after that is the art for the Garden Bean (6), the line after that is for the Red Bean (8), and so on
ASCIIArt = [["                      ", "                      ", "                      ", "                      ",
             "                      ", "                     "], 1, 2, 3, 4, 5, [
                "          / \\-        ", "        / /           ", "       |@|            ",
                "      / \\v|           ", "      |_              "], 7, [
                "       \\  |  /        ", "     -   ___   -      ", "     -  |00 \\  -      ",
                "         |U_/         ", "         /  \\         "], 9, [
                "        * *           ", "      *  __  *        ", "      o_|@ |          ", "        |__|_o        ",
                "        |  |          "], 11, [
                "         \\            ", "        | |           ", "      ”_|”|           ", "        |_|           ",
                "         L|           "], 13, [
                "       \\   8          ", "       \\o\\ |          ", "        \\~\\+,         ",
                "         \\_|          ", "         | |\\         "], 15, [
                "                      ", "        _____         ", "     o_| ..  |        ", "       |     |        ",
                "    |_|_______|       "], 17, [
                "          \\           ", "         /\\           ", "        |”| _-.       ",
                "       _|u||  |       ", "       / / |  |       "], 19, [
                "         __n__        ", "          |'|         ", "          |_|         ", "         -|_|-        ",
                "          |  \\        "]]
print(playerColoursANSI[5] + "Welcome to Bohnanza!")
breaker = False
print("Would you like a tutorial to learn how to play?")
response = input()
while not breaker:
    if len(response) > 0:
        if response[-1] == "!":
            response = response[:-1]
        if response.lower() in no or response.lower() in yes:
            if response.lower() in yes:
                breaker = True
                response = "yes"
            else:
                breaker = True
                response = "no"
        else:
            response = input()
    else:
        response = input()
# Here is the tutorial
if response.lower() == "yes":
    print("Press enter to go through the tutorial")
    input()
    print("To play Bohnanza, you plant beans and harvest them to try to get more coins than anyone else")
    input()
    print("To start, everyone gets dealt five cards. Whenever you check your hand, you will see something like this:")
    print("1. Black-Eyed Bean (10)")
    print("2. Soy Bean (12)")
    print("3. Chili Bean (18)")
    print("4. Green Bean (14)")
    print("5. Black-Eyed Bean (10)")
    input()
    print(
        "There are eight types of beans in this game, and each type has a different quantity in the deck, indicated by the number in brackets.")
    input()
    print("When you are planting a bean, you must either start a bean pile, or continue a bean pile.")
    print(
        "You may only plant one type of bean in a field. If you try to plant a different type of bean in a field, you will harvest the planted beans (more about that later)")
    input()
    print(
        "In a 3 player game, everyone has 3 fields to plant beans in, but in a 4-5 player game, everyone has 2 fields to plant beans in")
    input()
    print("The more beans you have in one of your fields, the more money you can earn when you harvest them")
    print("For example:")
    print(playerColoursANSI[2] + "Zach's fields:")
    print(" ______________________      ______________________ ")
    print("/                      \\    /                      \\")
    print("|          1.          |    |          2.          |   <- Field number")
    print(
        "|          20          |    |          16          |   <- Quantity of this card in the deck (also shown when you check your hand)")
    print("|                      |    |                      |")
    print("|         __n__        |    |                      |")
    print("|          |'|         |    |        _____         |")
    print(
        "|          |_|         |    |     o_| ..  |        |  <- A nice picture of the bean (taken from the actual game)")
    print("|         -|_|-        |    |       |     |        |")
    print("|          |  \\        |    |    |_|_______|       |")
    print(
        "|   Blue Bean (09x)    |    |   Stink Bean (02x)   |  <- The name of the bean and the quantity of the bean Zach has planted in brackets")
    print("|                  O   |    |                  O   |")
    print("|             O    O   |    |             O    O   |")
    print(
        "|        O    O    O   |    |        O    O    O   |  <- The number of beans required to earn this amount of coins (3 stink beans are")
    print(
        "|   O    O    O    O   |    |   O    O    O    O   |     required to earn 1 coin, 5 are required to earn two coins, and so on. Each type")
    print(
        "|   4    6    8   10   |    |   3    5    7    8   |     of bean needs a different number of beans to get coins based on how rare they ")
    print("\\______________________/    \\______________________/     are in the deck.")
    print(playerColoursANSI[
              5] + "In this situation, if Zach were to harvest his blue beans, he would earn 3 coins, as indicated on the bottom of the card.")
    print(
        "Zach does not have enough stink beans to earn any coins if he were to harvest them, however (he has two, but needs at least three).")
    input()
    print("At the beginning of your turn, you must plant the first card in your hand.")
    print("Then you decide if you want to plant the second card in your hand")
    input()
    print(
        "After that, the top two cards from the draw pile will be revealed. You must decide if you want to keep these cards or trade them with another player")
    input()
    print(
        "At this time, bartering and discussion between the players is encouraged. Two players come to agreement to the terms of a trade before the active player inputs that they will trade")
    print("If you don't want the cards, but no one else is willing to trade, you must deal with it and take the cards")
    input()
    print(
        "At this time, only the active player is allowed to trade with the other players-- the non-active players cannot trade with each other")
    print(
        "When trading, you are allowed to trade with as many cards as you have in your hand (you can also trade with zero cards)")
    input()
    print(
        "After any trades have been finished and all the traded beans have been planted, you will be dealt three cards to end your turn.")
    input()
    print("The game ends when the deck runs out for the third time")
    print("You can also end the game early by typing \"/endGame\"")
    input()
    print("At the end of the game, the player with the most coins wins")
    input()
    print(
        "If you have any more questions, visit https://www.riograndegames.com/wp-content/uploads/2013/02/Bohnanza-Rules.pdf to read the official rules")
    print(
        "You can ignore the \"bean protection rule\" on the 6th page of the rulebook. This game does not implement that rule, so you don't have to play by it")
    input()
    print("Type \"/help\" at any time after the first player starts playing to learn how to use some commands")
    input()
    print("Press enter to start playing the game")
    input()
print("How many human players are there? There must be between 0 and 5 human players.")
response = input().lower()
breaker = False
while not breaker:
    if len(response) > 0:
        if response[-1] == "!":
            response = response[:-1]
        if response in numbers:
            response = numbers.index(response)
        if str(response).isdigit():
            if 0 <= int(response) <= 5:
                breaker = True
            else:
                response = input().lower()
        else:
            response = input().lower()
    else:
        response = input().lower()
numberOfPlayers = int(response)
if numberOfPlayers < 5:
    print("How many AI players are there? There must be between " + str(max(0, (3 - int(response)))) + " and " + str(
        5 - int(response)) + " players. Note: the code for the AI players is not finished yet.")
    response = input().lower()
    breaker = False
    while not breaker:
        if len(response) > 0:
            if response[-1] == "!":
                response = response[:-1]
            if response in numbers:
                response = numbers.index(response)
            if str(response).isdigit():
                if max(0, (3 - numberOfPlayers <= int(response))) <= 5 - numberOfPlayers:
                    breaker = True
                else:
                    response = input().lower()
            else:
                response = input().lower()
        else:
            response = input().lower()
    numberOfPlayers += int(response)
    numberOfAIPlayers = int(response)
else:
    numberOfAIPlayers = 0
playerNames = []
lowerCasePlayerNames = []
if numberOfPlayers == 3:
    numberOfFieldsInUse = 3
else:
    numberOfFieldsInUse = 2
playerHands = [0, 0, 0, 0, 0]
for i in range(numberOfPlayers):
    if numberOfPlayers - numberOfAIPlayers > i:  # The first players are human; the last are AI
        print(playerColoursANSI[i] + "What is player " + str(i + 1) + "'s name? This human player will be " +
              playerColourNames[i])
    else:
        print(playerColoursANSI[i] + "What is player " + str(i + 1) + "'s name? This AI player will be " +
              playerColourNames[i])
    playerHands[i] = [deck.pop(0), deck.pop(1), deck.pop(2), deck.pop(3), deck.pop(4)]
    response = input()
    while len(response) == 0 or response in playerNames:
        response = input()
    playerNames.append(response)
    lowerCasePlayerNames.append(response.lower())
    if response == "Evan":
        coins[i] = 1000
    else:
        coins[i] = 0
if numberOfAIPlayers < 5:
    print(playerColoursANSI[5] + "This question is to determine which player goes first:")
    if numberOfAIPlayers == 0:
        print("Who most recently ate beans?")
    else:
        minutes = random.randint(0, 59)
        if len(str(minutes)) == 1:
            minutes = "0" + str(minutes)
        if numberOfAIPlayers == 1:
            print("Who most recently ate beans? The AI player ate beans " + numbers[
                random.randint(1, 5)] + " days ago for breakfast at " + str(random.randint(5, 9)) + ":" + str(minutes))
        else:
            print("Who most recently ate beans? The AI players ate beans at the same time " + numbers[
                random.randint(1, 5)] + " days ago for breakfast at " + str(random.randint(5, 9)) + ":" + str(minutes))
    response = input()
    responseExpected = "name"
    checkForHacks()
    startingPlayerName = response
    startingPlayer = playerNames.index(startingPlayerName)
else:
    startingPlayer = random.randint(0, 4)
playerTurn = startingPlayer
while True:
    print(playerBoldedColoursANSI[playerTurn] + "It is now " + playerNames[playerTurn] + "'s turn")
    showFieldsOfPlayer(playerTurn)
    showHandOfPlayer(playerTurn)
    if len(playerHands[playerTurn]) > 0:
        print("Where would you like to plant the first card in your hand (enter a number between 1 and " + str(
            numberOfFieldsInUse) + ")?")
        if playerTurn <= numberOfPlayers - numberOfAIPlayers:  # If human player, go through these lines of code
            response = input()
            responseExpected = "int"
            responseMax = numberOfFieldsInUse
            responseMin = 1
            checkForHacks()
            response = int(response)
        else:  # If AI player, do this function
            decideWhereToPlantBean(playerTurn, playerHands[playerTurn][0])
        if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][
                                                                                  response - 1] == \
                                                                              playerHands[playerTurn][0]:
            harvestBeans(playerTurn, response - 1)
        quantityOfBeansInFields[playerTurn][response - 1] += 1
        typeOfBeansInFields[playerTurn][response - 1] = playerHands[playerTurn].pop(0)
        showFieldsOfPlayer(playerTurn)
        showHandOfPlayer(playerTurn)
        if len(playerHands[playerTurn]) > 0:
            print("Would you like to plant the next card in your hand?")
            if playerTurn <= numberOfPlayers - numberOfAIPlayers:  # If human player, go through these lines of code
                response = input()
                responseExpected = "y/n"
                checkForHacks()
            elif typeOfBeansInFields[playerTurn][0] == playerHands[0] or typeOfBeansInFields[playerTurn][1] == \
                    playerHands[0] or (
                    typeOfBeansInFields[playerTurn][-1] == playerHands[0] and numberOfFieldsInUse == 3):
                response = "Yes"
            else:
                response = "No"
                for i in range(numberOfFieldsInUse):
                    if quantityOfBeansInFields[playerTurn][i] == 0 or (
                            quantityOfBeansInFields[playerTurn][i] >= maxQuantityOfBeans[
                        typeOfBeansInFields[playerTurn][i]]):
                        response = "Yes"
            if response.lower() == "yes":
                print("Where would you like to plant the first card in your hand (enter a number between 1 and " + str(
                    numberOfFieldsInUse) + ")?")
                if playerTurn <= numberOfPlayers - numberOfAIPlayers:
                    response = input()
                    responseExpected = "int"
                    responseMax = numberOfFieldsInUse
                    responseMin = 1
                    checkForHacks()
                    response = int(response)
                else:
                    decideWhereToPlantBean(playerTurn, playerHands[0])
                if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][
                                                                                          response - 1] == \
                                                                                      playerHands[playerTurn][0]:
                    harvestBeans(playerTurn, response - 1)
                quantityOfBeansInFields[playerTurn][response - 1] += 1
                typeOfBeansInFields[playerTurn][response - 1] = playerHands[playerTurn].pop(0)
        else:
            print("You don't have any beans left in your hand, so you don't have the option of planting a second bean")
    else:
        print("You don't have any beans left in your hand, so you can't plant any beans at this time")
    print(playerColoursANSI[5] + "Here are the top two cards from the deck. " + playerNames[
        playerTurn] + " must decide whether to keep these cards or trade them.")
    numberOfFieldsInUse = 2
    showFieldsOfPlayer(5)
    print("")
    if numberOfPlayers == 3:
        numberOfFieldsInUse = 3
    else:
        numberOfFieldsInUse = 2
    showFieldsOfPlayer(0)
    showHandOfPlayer(0)
    print("")
    showFieldsOfPlayer(1)
    showHandOfPlayer(1)
    print("")
    showFieldsOfPlayer(2)
    showHandOfPlayer(2)
    if numberOfPlayers > 3:
        print("")
        showFieldsOfPlayer(3)
        showHandOfPlayer(3)
        if numberOfPlayers > 4:
            print("")
            showFieldsOfPlayer(4)
            showHandOfPlayer(4)
    tradingCardsOfOtherPlayer = []
    for i in range(2):  # Trading stage (loop of range(2) because two cards are flipped over)
        if i == 0:
            print(playerColoursANSI[5] + "Would anyone like to trade for the first card (a " + cardNames[
                tradingCards[0]] + ")?")
        else:
            print(playerColoursANSI[5] + "Would anyone like to trade for the second card (a " + cardNames[
                tradingCards[1]] + ")?")
        print("If " + playerNames[playerTurn] + " would like this card (or no one else wants it), enter no.")
        print("Otherwise, the non-active players should give offers to " + playerNames[
            playerTurn] + " and they should enter yes")
        if playerTurn <= numberOfPlayers - numberOfAIPlayers:
            response = input()
            responseExpected = "y/n"
            checkForHacks()
        else:
            if tradingCards[i] in typeOfBeansInFields[playerTurn] or (
                    quantityOfBeansInFields[playerTurn][0] == 0 or quantityOfBeansInFields[playerTurn][1] == 0 or
                    quantityOfBeansInFields[playerTurn][0] >= maxQuantityOfBeans[typeOfBeansInFields[playerTurn][0]] or
                    quantityOfBeansInFields[playerTurn][1] >= maxQuantityOfBeans[
                        typeOfBeansInFields[playerTurn][1]]) and playerHands[playerTurn][0] == tradingCards[i]:
                response = "No"
            elif numberOfFieldsInUse == 3:
                if (quantityOfBeansInFields[playerTurn][2] >= maxQuantityOfBeans[typeOfBeansInFields[playerTurn][2]] or
                        quantityOfBeansInFields[playerTurn][2]) and playerHands[playerTurn][0] == tradingCards[i]:
                    response = "No"
            else:
                for j in range(numberOfPlayers):
                    if not j == playerTurn:
                        print(playerNames[playerTurn] + " would like to trade. Would " + playerNames[
                            j] + " like to trade for the " + cardNames[tradingCards[i]] + "?")
                        if playerTurn <= numberOfPlayers - numberOfAIPlayers:
                            response = input()
                            responseExpected = "y/n"
                            checkForHacks()
                            if response.lower() == "yes":
                                print("How many cards are you offering to trade with?")
                                showHandOfPlayer(j)
                                response = input()
                                responseExpected = "int"
                                responseMax = len(playerHands[j])
                                responseMin = 0
                                checkForHacks()
                                response = int(response)
                                for k in range(response):
                                    if response != 1:
                                        if str(k)[-1] == "0":
                                            print(playerColoursANSI[5] + "Enter the placement of the " + str(
                                                k + 1) + "st card you want to trade with. Enter a number between 1 and " + str(
                                                len(playerHands[j])))
                                        elif str(k)[-1] == "1":
                                            print(playerColoursANSI[5] + "Enter the placement of the " + str(
                                                k + 1) + "nd card you want to trade with. Enter a number between 1 and " + str(
                                                len(playerHands[j])))
                                        elif str(k)[-1] == "2":
                                            print(playerColoursANSI[5] + "Enter the placement of the " + str(
                                                k + 1) + "rd card you want to trade with. Enter a number between 1 and " + str(
                                                len(playerHands[j])))
                                        else:
                                            print(playerColoursANSI[5] + "Enter the placement of the " + str(
                                                k + 1) + "th card you want to trade with. Enter a number between 1 and " + str(
                                                len(playerHands[j])))
                                    else:
                                        print(playerColoursANSI[
                                                  5] + "Enter the placement of the card you agreed to trade with. Enter a "
                                                       "number between 1 and " + str(len(playerHands[j])) + ".")
                                    response = input()
                                    responseExpected = "int"
                                    responseMax = len(playerHands[j])
                                    responseMin = 1
                                    checkForHacks()
                                    response = int(response)
                                    cardOffers[j].append(playerHands[response])
                        else:
                            # Here is where the AIs that aren't the active player give offers for the trading cards
                            if tradingCards[i] in typeOfBeansInFields[j]:
                                response = "Yes"
                                cardOffers[j].append(playerHands[j][random.randint(0,len(playerHands[j]))])
                            else:
                                response = "No"
                            print(AIResponseColoursANSI[j] + response)
            print(AIResponseColoursANSI[playerTurn] + str(response))
        if response.lower() == "no":
            print("Where would " + playerNames[playerTurn] + " like to plant this " + cardNames[
                tradingCards[i]] + " (enter a number between 1 and " +
                  str(numberOfFieldsInUse) + ")?")
            showFieldsOfPlayer(playerTurn)
            if playerTurn <= numberOfPlayers - numberOfAIPlayers:
                response = input()
                responseExpected = "int"
                responseMax = numberOfFieldsInUse
                responseMin = 1
                checkForHacks()
                response = int(response)
            else:
                decideWhereToPlantBean(playerTurn, tradingCards[i])
            if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][
                                                                                      response - 1] == tradingCards[i]:
                harvestBeans(playerTurn, response - 1)
            quantityOfBeansInFields[playerTurn][response - 1] += 1
            typeOfBeansInFields[playerTurn][response - 1] = tradingCards[i]
        else:
            print("After " + playerNames[
                playerTurn] + " has decided on who to trade with, enter the name of that person.")
            response = input()
            responseExpected = "name"
            responseCantBe = playerNames[playerTurn]  # This line doesn't work for some reason
            checkForHacks()
            tradingPlayer = lowerCasePlayerNames.index(response.lower())
            showFieldsOfPlayer(tradingPlayer)
            print(playerNames[tradingPlayer] + ", where would you like to plant your new " + cardNames[
                tradingCards[i]] + "?")
            response = input()
            responseExpected = "int"
            responseMax = numberOfFieldsInUse
            responseMin = 1
            checkForHacks()
            response = int(response)
            if not quantityOfBeansInFields[tradingPlayer][response - 1] == 0 and not typeOfBeansInFields[tradingPlayer][
                                                                                         response - 1] == tradingCards[
                                                                                         i]:
                harvestBeans(tradingPlayer, response - 1)
            quantityOfBeansInFields[tradingPlayer][response - 1] += 1
            typeOfBeansInFields[tradingPlayer][response - 1] = tradingCards[i]
            print(playerColoursANSI[5] + "How many beans did " + playerNames[
                tradingPlayer] + " agree to trade for this bean? Enter a number between 0 and " + str(
                len(playerHands[tradingPlayer])))
            print(playerNames[tradingPlayer] + "'s cards:")
            showHandOfPlayer(tradingPlayer)
            response = input()
            responseExpected = "int"
            responseMax = len(playerHands[tradingPlayer])
            responseMin = 0
            checkForHacks()
            response = int(response)
            for j in range(response):
                if response != 1:
                    if str(j)[-1] == "0":
                        print(playerColoursANSI[5] + "Enter the placement of the " + str(
                            j + 1) + "st card you want to trade with. Enter a number between 1 and " + str(
                            len(playerHands[tradingPlayer])))
                    elif str(j)[-1] == "1":
                        print(playerColoursANSI[5] + "Enter the placement of the " + str(
                            j + 1) + "nd card you want to trade with. Enter a number between 1 and " + str(
                            len(playerHands[tradingPlayer])))
                    elif str(j)[-1] == "2":
                        print(playerColoursANSI[5] + "Enter the placement of the " + str(
                            j + 1) + "rd card you want to trade with. Enter a number between 1 and " + str(
                            len(playerHands[tradingPlayer])))
                    else:
                        print(playerColoursANSI[5] + "Enter the placement of the " + str(
                            j + 1) + "th card you want to trade with. Enter a number between 1 and " + str(
                            len(playerHands[tradingPlayer])))
                else:
                    print(playerColoursANSI[5] + "Enter the placement of the card you agreed to trade with. Enter a "
                                                 "number between 1 and " + str(len(playerHands[tradingPlayer])) + ".")
                response = input()
                responseExpected = "int"
                responseMax = len(playerHands[tradingPlayer])
                responseMin = 1
                checkForHacks()
                response = int(response)
                tradingCardsOfOtherPlayer.append(playerHands[tradingPlayer].pop(response - 1))
                print(playerColoursANSI[5] + playerNames[tradingPlayer] + "'s cards:")
                showHandOfPlayer(tradingPlayer)
    for i in range(len(tradingCardsOfOtherPlayer)):  # active player now plants the cards they got in trading
        print(playerColoursANSI[5] + "Where would " + playerNames[playerTurn] + " like to plant their new " + cardNames[
            tradingCardsOfOtherPlayer[i]] + "?")
        showFieldsOfPlayer(playerTurn)
        response = input()
        responseExpected = "int"
        responseMax = numberOfFieldsInUse
        responseMin = 1
        checkForHacks()
        response = int(response)
        if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][
                                                                                  response - 1] == \
                                                                              tradingCardsOfOtherPlayer[i]:
            harvestBeans(playerTurn, response - 1)
        quantityOfBeansInFields[playerTurn][response - 1] += 1
        typeOfBeansInFields[playerTurn][response - 1] = tradingCardsOfOtherPlayer[i]
    print(playerColoursANSI[5] + playerNames[playerTurn] + " now picks up three cards to finish their turn:")
    for i in range(3):
        if len(deck) == 0:
            if not numberOfTimesDeckHasRunOut == 2:
                if numberOfTimesDeckHasRunOut == 0:
                    print(playerBoldedColoursANSI[5] + "The deck has now run out for the first time")
                else:
                    print(playerBoldedColoursANSI[5] + "The deck has now run out for the second time")
                deck = shuffleAndCreateDeck()
            else:
                numberOfTimesDeckHasRunOut += 1
                endTheGame()
        playerHands[playerTurn].append(deck.pop(0))
    showHandOfPlayer(playerTurn)
    if playerTurn < numberOfPlayers - 1:
        playerTurn += 1
    else:
        playerTurn = 0
    print("")
