import random


def shuffleAndCreateDeck():  # Shuffles the deck
    global numberOfTimesDeckHasRunOut
    numberOfTimesDeckHasRunOut += 1
    functionDeck = []
    makeDeck = cardsLeftInDiscardAndPickupPile
    while max(makeDeck) > 0:
        randomCard = random.randint(1,
                                    makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4] + makeDeck[3] + makeDeck[2] +
                                    makeDeck[1] + makeDeck[0])
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
    return functionDeck


def showFieldsOfPlayer(player):
    if player == 5:
        global deck
        global numberOfTimesDeckHasRunOut
        if len(deck) == 0:
            if not numberOfTimesDeckHasRunOut == 2:
                if numberOfTimesDeckHasRunOut == 0:
                    print(playerColoursANSI[6] + "The deck has now run out for the first time")
                else:
                    print(playerColoursANSI[6] + "The deck has now run out for the second time")
                deck = shuffleAndCreateDeck()
            else:
                numberOfTimesDeckHasRunOut += 1
                endTheGame()
        typeOfBeansInFields[5][0] = deck.pop(0)
        if len(deck) == 0:
            if not numberOfTimesDeckHasRunOut == 2:
                if numberOfTimesDeckHasRunOut == 0:
                    print(playerColoursANSI[6] + "The deck has now run out for the first time")
                else:
                    print(playerColoursANSI[6] + "The deck has now run out for the second time")
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
        print(" ______________________      ______________________ ")
        print("/                      \\    /                      \\")
        print("|          1.          |    |          2.          |")
    else:
        field = [0, 0, 0]
        print(playerColoursANSI[player] + "______________________      ______________________      "
                                          "______________________ ")
        print("/                      \\    /                      \\    /                      \\")
        print("|          1.          |    |          2.          |    |          3.          |")
    for k in range(numberOfFieldsInUse):
        if len(str((typeOfBeansInFields[player])[k])) == 1:
            field[k] = "|          0" + str(typeOfBeansInFields[player][k]) + "          |"
        else:
            field[k] = "|          " + str(typeOfBeansInFields[player][k]) + "          |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for k in range(4):
        if numberOfFieldsInUse == 2:
            print("|                      |    |                      |")
        else:
            print("|                      |    |                      |    |                      |")
    for k in range(numberOfFieldsInUse):
        if len(str(quantityOfBeansInFields[player][k])) == 1:
            quantity = "0" + str(quantityOfBeansInFields[player][k])
        else:
            quantity = str(quantityOfBeansInFields[player][k])
        if typeOfBeansInFields[player][k] == 0:
            field[k] = "|                      |"
        elif typeOfBeansInFields[player][k] == 6:
            field[k] = "|  Garden Bean (" + quantity + "x)   |"
        elif typeOfBeansInFields[player][k] == 8:
            field[k] = "|    Red Bean (" + quantity + "x)    |"
        elif typeOfBeansInFields[player][k] == 10:
            field[k] = "|Black-Eyed Bean (" + quantity + "x) |"
        elif typeOfBeansInFields[player][k] == 12:
            field[k] = "|    Soy Bean (" + quantity + "x)    |"
        elif typeOfBeansInFields[player][k] == 14:
            field[k] = "|   Green Bean (" + quantity + "x)   |"
        elif typeOfBeansInFields[player][k] == 16:
            field[k] = "|   Stink Bean (" + quantity + "x)   |"
        elif typeOfBeansInFields[player][k] == 18:
            field[k] = "|   Chili Bean (" + quantity + "x)   |"
        else:
            field[k] = "|   Blue Bean (" + quantity + "x)    |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for k in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][k] == 0:
            field[k] = "|                      |"
        elif typeOfBeansInFields[player][k] == 6:
            field[k] = "|                      |"
        else:
            field[k] = "|                  O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for k in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][k] == 0:
            field[k] = "|                      |"
        elif typeOfBeansInFields[player][k] == 6:
            field[k] = "|             O        |"
        else:
            field[k] = "|             O    O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for k in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][k] == 0:
            field[k] = "|                      |"
        elif typeOfBeansInFields[player][k] == 6:
            field[k] = "|        O    O        |"
        else:
            field[k] = "|        O    O    O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for k in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][k] == 0:
            field[k] = "|                      |"
        elif typeOfBeansInFields[player][k] == 6:
            field[k] = "|        O    O        |"
        else:
            field[k] = "|   O    O    O    O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for k in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][k] == 0:
            field[k] = "|                      |"
        elif typeOfBeansInFields[player][k] == 6:
            field[k] = "|        2    3        |"
        elif typeOfBeansInFields[player][k] == 8:
            field[k] = "|   2    3    4    5   |"
        elif typeOfBeansInFields[player][k] == 10:
            field[k] = "|   2    4    5    6   |"
        elif typeOfBeansInFields[player][k] == 12:
            field[k] = "|   2    4    6    7   |"
        elif typeOfBeansInFields[player][k] == 14:
            field[k] = "|   3    5    6    7   |"
        elif typeOfBeansInFields[player][k] == 16:
            field[k] = "|   3    5    7    8   |"
        elif typeOfBeansInFields[player][k] == 18:
            field[k] = "|   3    6    8    9   |"
        elif typeOfBeansInFields[player][k] == 20:
            field[k] = "|   4    6    8   10   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
        print("\\______________________/    \\______________________/")
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
        print("\\______________________/    \\______________________/    \\______________________/")


def showHandOfPlayer(player):
    for k in range(len(playerHands[player])):
        if playerHands[player][k] == 6:
            print(playerColoursANSI[player] + str(k + 1) + ". Garden Bean (6)")
        elif playerHands[player][k] == 8:
            print(playerColoursANSI[player] + str(k + 1) + ". Red Bean (8)")
        elif playerHands[player][k] == 10:
            print(playerColoursANSI[player] + str(k + 1) + ". Black-Eyed Bean (10)")
        elif playerHands[player][k] == 12:
            print(playerColoursANSI[player] + str(k + 1) + ". Soy Bean (12)")
        elif playerHands[player][k] == 14:
            print(playerColoursANSI[player] + str(k + 1) + ". Green Bean (14)")
        elif playerHands[player][k] == 16:
            print(playerColoursANSI[player] + str(k + 1) + ". Stink Bean (16)")
        elif playerHands[player][k] == 18:
            print(playerColoursANSI[player] + str(k + 1) + ". Chili Bean (18)")
        elif playerHands[player][k] == 20:
            print(playerColoursANSI[player] + str(k + 1) + ". Blue Bean (20)")


def harvestBeans(player, field):
    if typeOfBeansInFields[player][field] == 6:
        if quantityOfBeansInFields[player][field] == 1:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Garden Bean")
        else:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Garden Beans")
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
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Black-Eyed Bean")
        else:
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Black-Eyed Beans")
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
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Green Beans")
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
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Stink Beans")
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
            print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Chili Beans")
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
    quantityOfBeansInFields[player][field] = 0
    typeOfBeansInFields[player][field] = 0


def endTheGame():
    global forcedEnd
    coinsInOrder = []
    positionsInReverseOrder = []
    for k in range(numberOfPlayers):
        coinsInOrder.append(min(coins))
        positionsInReverseOrder.append(int(coins.index(min(coins))))
        coins[coins.index(min(coins))] += 9999999999999999999999
    if forcedEnd == 1:
        print(playerColoursANSI[5] + "The game has now been ended.")
    else:
        print("The deck has now run out for the third and final time. The game is now over.")
    print("Press enter to go through the results")
    input()
    if numberOfPlayers >= 5:
        print("In fifth place...")
        input()
        print("is " + playerNames[positionsInReverseOrder[0]] + " with a total of " + str(coinsInOrder[0]) + "coins!")
        input()
    if numberOfPlayers >= 4:
        print("In fourth place...")
        input()
        print("is " + playerNames[positionsInReverseOrder[numberOfPlayers-4]] + " with a total of " + str(
            coinsInOrder[numberOfPlayers-4]) + " coins!")
        input()
    print("In third place...")
    input()
    print("is " + playerNames[positionsInReverseOrder[numberOfPlayers-3]] + " with a total of " + str(
        coinsInOrder[numberOfPlayers-3]) + " coins!")
    print("In second place...")
    input()
    print("is " + playerNames[positionsInReverseOrder[numberOfPlayers-2]] + " with a total of " + str(
        coinsInOrder[numberOfPlayers-2]) + " coins!")
    input()
    print("That means that " + playerNames[positionsInReverseOrder[numberOfPlayers-1]] + " won!")
    print(playerNames[positionsInReverseOrder[numberOfPlayers-1]] + " won with a total of " + str(
        coinsInOrder[numberOfPlayers-2]) + "coins!")
    if "Evan" in playerNames:
        print("I\'m kidding :)")
        coins[playerNames.index("Evan")] -= 1000
        coinsInOrder = []
        positionsInReverseOrder = []
        for k in range(numberOfPlayers):
            coinsInOrder.append(min(coins))
            positionsInReverseOrder.append(int(coins.index(min(coins))))
            coins.remove(min(coins))
        input()
        print("Here are the real results:")
        if numberOfPlayers >= 5:
            print("5. " + playerNames[positionsInReverseOrder[numberOfPlayers - 5]] + " with " + str(
                coinsInOrder[numberOfPlayers - 5]) + "coins")
        if numberOfPlayers >= 4:
            print("4. " + playerNames[positionsInReverseOrder[numberOfPlayers - 4]] + " with " + str(
                coinsInOrder[numberOfPlayers - 4]) + "coins")
        print("3. " + playerNames[positionsInReverseOrder[numberOfPlayers-3]] + " with " + str(
            coinsInOrder[numberOfPlayers - 3]) + "coins")
        print("2. " + playerNames[positionsInReverseOrder[numberOfPlayers - 2]] + " with " + str(
            coinsInOrder[numberOfPlayers - 2]) + "coins")
        print("1. " + playerNames[positionsInReverseOrder[numberOfPlayers - 1]] + " with " + str(
            coinsInOrder[numberOfPlayers - 1]) + "coins")
    exit()


def checkForHacks(command):
    if command.isdigit():
        if not responseExpected == "int" or int(command) > responseMax or int(command) < responseMin:
            checkForHacksBodyCode(command)
    elif (responseExpected == "name" and command not in playerNames) or (responseExpected == "y/n" and not command.lower() == "yes" and not command.lower() == "no") or responseExpected == "int":
        checkForHacksBodyCode(command)


def checkForHacksBodyCode(command):
    global response
    global forcedEnd
    if command == "/help":
        print("type \"/checkStats\" to see some of the game's current stats")
        print("type \"/endGame\" to end the game")
    elif command.lower() == "/endgame":
        forcedEnd = 1
        endTheGame()
    elif command.lower() == "/checkstats":
        print("Starting player: " + playerNames[startingPlayer])
        print("Coins of players:")
        print(playerNames[0] + ": " + str(coins[0]))
        print(playerNames[1] + ": " + str(coins[1]))
        print(playerNames[2] + ": " + str(coins[2]))
        if numberOfPlayers >= 4:
            print(playerNames[3] + ": " + str(coins[3]))
        if numberOfPlayers >= 5:
            print(playerNames[4] + ": " + str(coins[4]))
        print("Number of times deck has run out: " + str(numberOfTimesDeckHasRunOut))
    response = input()
    checkForHacks(response)


forcedEnd = 0
numberOfTimesDeckHasRunOut = -1
playerColourNames = ["red", "blue", "green", "yellow", "purple", "white", "black"]
playerColoursANSI = ["\033[1;31;40m", "\033[1;34;40m", "\033[1;32;40m", "\033[1;33;40m", "\033[1;35;40m", "\033["
                     "1;37;40m", "\033[1;30;47m"]
cardsLeftInDiscardAndPickupPile = [20, 18, 16, 14, 12, 10, 8, 6]
cardNames = [0, 1, 2, 3, 4, 5, "Garden Bean", 7, "Red Bean", 9, "Black-eyed Bean", 11, "Soy Bean", 13, "Green Bean", 15,
             "Stink Bean", 17, "Chili Bean", 19, "Blue Bean"]
coins = [10, 20, 30, 40, 50]
typeOfBeansInFields = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0], [0, 0], [0, 0]]
quantityOfBeansInFields = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0], [0, 0], [1, 1]]
deck = shuffleAndCreateDeck()
tradingCards = [0, 0]
responseCantBe = []
print(playerColoursANSI[5] + "Welcome to Bohnanza!")
print("How many players are there? There must be between 3 and 5 players.")
numberOfPlayers = int(input())
playerNames = []
lowerCasePlayerNames = []
if numberOfPlayers == 3:
    numberOfFieldsInUse = 3
else:
    numberOfFieldsInUse = 2
playerHands = [0, 0, 0, 0, 0]
for i in range(numberOfPlayers):
    print(
        playerColoursANSI[i] + "What is player " + str(i + 1) + "\'s name? This player will be " + playerColourNames[i])
    playerHands[i] = [deck.pop(0), deck.pop(1), deck.pop(2), deck.pop(3), deck.pop(4)]
    response = input()
    playerNames.append(response)
    lowerCasePlayerNames.append(response.lower())
    if response == "Evan":
        coins[i] = 1000
print(playerColoursANSI[5] + "Who most recently ate beans?")
startingPlayerName = input()
startingPlayer = playerNames.index(startingPlayerName)
playerTurn = startingPlayer
while True:
    print(playerColoursANSI[playerTurn] + "It is now " + playerNames[playerTurn] + "'s turn")
    showFieldsOfPlayer(playerTurn)
    showHandOfPlayer(playerTurn)
    if len(playerHands[playerTurn]) > 0:
        print("Where would you like to plant the first card in your hand (enter a number between 1 and " + str(
            numberOfFieldsInUse) + ")?")
        response = input()
        responseExpected = "int"
        responseMax = numberOfFieldsInUse
        responseMin = 1
        checkForHacks(response)
        response = int(response)
        if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][
                                                                              response - 1] == playerHands[playerTurn][0]:
            harvestBeans(playerTurn, response - 1)
        quantityOfBeansInFields[playerTurn][response - 1] += 1
        typeOfBeansInFields[playerTurn][response - 1] = playerHands[playerTurn].pop(0)
        showFieldsOfPlayer(playerTurn)
        showHandOfPlayer(playerTurn)
        if len(playerHands[playerTurn]) > 0:
            print("Would you like to plant the next card in your hand (enter \"yes\" or \"no\")?")
            response = input()
            responseExpected = "y/n"
            checkForHacks(response)
            if response.lower() == "yes":
                print("Where would you like to plant the first card in your hand (enter a number between 1 and " + str(
                    numberOfFieldsInUse) + ")?")
                response = input()
                responseExpected = "int"
                responseMax = numberOfFieldsInUse
                responseMin = 1
                checkForHacks(response)
                response = int(response)
                if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][
                   response - 1] == playerHands[playerTurn][0]:
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
            print(playerColoursANSI[5] + "Would anyone like to trade for the first card (a " + cardNames[tradingCards[0]] + ")??")
        else:
            print(playerColoursANSI[5] + "Would anyone like to trade for the second card (a " + cardNames[tradingCards[1]] + ")?")
        print("If " + playerNames[playerTurn] + " would like this card (or no one else wants it), enter \"no\".")
        print("Otherwise, the non-active players should give offers to " + playerNames[
            playerTurn] + " and they should enter \"yes\"")
        response = input()
        responseExpected = "y/n"
        checkForHacks(response)
        if response.lower() == "no":
            print("Where would " + playerNames[playerTurn] + " like to plant this " + cardNames[tradingCards[i]] + " (enter a number between 1 and " +
                  str(numberOfFieldsInUse) + ")?")
            showFieldsOfPlayer(playerTurn)
            response = input()
            responseExpected = "int"
            responseMax = numberOfFieldsInUse
            responseMin = 1
            checkForHacks(response)
            response = int(response)
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
            responseCantBe = [playerNames[playerTurn]]
            checkForHacks(response)
            tradingPlayer = lowerCasePlayerNames.index(response.lower())
            showFieldsOfPlayer(tradingPlayer)
            print(playerNames[tradingPlayer] + ", where would you like to plant your new " + cardNames[
                tradingCards[i]] + "?")
            response = input()
            responseExpected = "int"
            responseMax = numberOfFieldsInUse
            responseMin = 1
            checkForHacks(response)
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
            checkForHacks(response)
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
                checkForHacks(response)
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
        checkForHacks(response)
        response = int(response)
        if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][
                                                           response - 1] == tradingCardsOfOtherPlayer[i]:
            harvestBeans(playerTurn, response - 1)
        quantityOfBeansInFields[playerTurn][response - 1] += 1
        typeOfBeansInFields[playerTurn][response - 1] = tradingCardsOfOtherPlayer[i]
    print(playerColoursANSI[5] + playerNames[playerTurn] + " now picks up three cards to finish their turn")
    for i in range(3):
        if len(deck) == 0:
            if not numberOfTimesDeckHasRunOut == 2:
                if numberOfTimesDeckHasRunOut == 0:
                    print(playerColoursANSI[6] + "The deck has now run out for the first time")
                else:
                    print(playerColoursANSI[6] + "The deck has now run out for the second time")
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
