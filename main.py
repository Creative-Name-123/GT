import random
def shuffleAndCreateDeck():  # Shuffles the deck
    makeDeck = [20, 18, 16, 14, 12, 10, 8, 6]
    deck = []
    while max(makeDeck) > 0:
        randomCard = random.randint(1,makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4] + makeDeck[3] + makeDeck[2] +makeDeck[1] + makeDeck[0])
        if randomCard > makeDeck[7]:
            if randomCard > makeDeck[7] + makeDeck[6]:
                if randomCard > makeDeck[7] + makeDeck[6] + makeDeck[5]:
                    if randomCard > makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4]:
                        if randomCard > makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4] + makeDeck[3]:
                            if randomCard > makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4] + makeDeck[3] + makeDeck[2]:
                                if randomCard > makeDeck[7] + makeDeck[6] + makeDeck[5] + makeDeck[4] + makeDeck[3] + makeDeck[2] + makeDeck[1]:
                                    deck.append(20)
                                    makeDeck[0] -= 1
                                else:
                                    deck.append(18)
                                    makeDeck[1] -= 1
                            else:
                                deck.append(16)
                                makeDeck[2] -= 1
                        else:
                            deck.append(14)
                            makeDeck[3] -= 1
                    else:
                        deck.append(12)
                        makeDeck[4] -= 1
                else:
                    deck.append(10)
                    makeDeck[5] -= 1
            else:
                deck.append(8)
                makeDeck[6] -= 1
        else:
            deck.append(6)
            makeDeck[7] -= 1
    return deck
def showFieldsOfPlayer(player):
    if player==5:
        typeOfBeansInFields[5][0]=deck.pop(0)
        typeOfBeansInFields[5][1]=deck.pop(0)
        tradingCards[0]=typeOfBeansInFields[5][0]
        tradingCards[1]=typeOfBeansInFields[5][1]
    else:
        print(playerNames[player] + "'s fields:")
    if numberOfPlayers > 3 or player==5:
        field = [0, 0]  #fields are 22 spaces wide with 4 spaces in between
        print(" ______________________      ______________________ ")
        print("/                      \\    /                      \\")
        print("|          1.          |    |          2.          |")
    else:
        field = [0, 0, 0]
        print(" ______________________      ______________________      ______________________ ")
        print("/                      \\    /                      \\    /                      \\")
        print("|          1.          |    |          2.          |    |          3.          |")
    for i in range(numberOfFieldsInUse):
        if len(str((typeOfBeansInFields[player])[i])) == 1:
            field[i] = "|          0" + str(typeOfBeansInFields[player][i]) + "          |"
        else:
            field[i] = "|          " + str(typeOfBeansInFields[player][i]) + "          |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for i in range(4):
        if numberOfFieldsInUse == 2:
            print("|                      |    |                      |")
        else:
            print("|                      |    |                      |    |                      |")
    for i in range(numberOfFieldsInUse):
        if len(str(quantityOfBeansInFields[player][i])) == 1:
            quantity = "0" + str(quantityOfBeansInFields[player][i])
        else:
            quantity = str(quantityOfBeansInFields[player][i])
        if typeOfBeansInFields[player][i] == 0:
            field[i] = "|                      |"
        elif typeOfBeansInFields[player][i] == 6:
            field[i] = "|  Garden Bean (" + quantity + "x)   |"
        elif typeOfBeansInFields[player][i] == 8:
            field[i] = "|    Red Bean (" + quantity + "x)    |"
        elif typeOfBeansInFields[player][i] == 10:
            field[i] = "|Black-Eyed Bean (" + quantity + "x) |"
        elif typeOfBeansInFields[player][i] == 12:
            field[i] = "|    Soy Bean (" + quantity + "x)    |"
        elif typeOfBeansInFields[player][i] == 14:
            field[i] = "|   Green Bean (" + quantity + "x)   |"
        elif typeOfBeansInFields[player][i] == 16:
            field[i] = "|   Stink Bean (" + quantity + "x)   |"
        elif typeOfBeansInFields[player][i] == 18:
            field[i] = "|   Chili Bean (" + quantity + "x)   |"
        else:
            field[i] = "|   Blue Bean (" + quantity + "x)    |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for i in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][i] == 0:
            field[i] = "|                      |"
        elif typeOfBeansInFields[player][i] == 6:
            field[i] = "|                      |"
        else:
            field[i] = "|                  O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for i in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][i] == 0:
            field[i] = "|                      |"
        elif typeOfBeansInFields[player][i] == 6:
            field[i] = "|             O        |"
        else:
            field[i] = "|             O    O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for i in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][i] == 0:
            field[i] = "|                      |"
        elif typeOfBeansInFields[player][i] == 6:
            field[i] = "|        O    O        |"
        else:
            field[i] = "|        O    O    O   |"
    if numberOfFieldsInUse == 2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for i in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][i] == 0:
            field[i] = "|                      |"
        elif typeOfBeansInFields[player][i] == 6:
            field[i] = "|        O    O        |"
        else:
            field[i] = "|   O    O    O    O   |"
    if numberOfFieldsInUse==2:
        print(str(field[0]) + "    " + str(field[1]))
    else:
        print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
    for i in range(numberOfFieldsInUse):
        if typeOfBeansInFields[player][i] == 0:
            field[i] = "|                      |"
        elif typeOfBeansInFields[player][i] == 6:
            field[i] = "|        2    3        |"
        elif typeOfBeansInFields[player][i] == 8:
            field[i] = "|   2    3    4    5   |"
        elif typeOfBeansInFields[player][i] == 10:
            field[i] = "|   2    4    5    6   |"
        elif typeOfBeansInFields[player][i] == 12:
            field[i] = "|   2    4    6    7   |"
        elif typeOfBeansInFields[player][i] == 14:
            field[i] = "|   3    5    6    7   |"
        elif typeOfBeansInFields[player][i] == 16:
            field[i] = "|   3    5    7    8   |"
        elif typeOfBeansInFields[player][i] == 18:
            field[i] = "|   3    6    8    9   |"
        elif typeOfBeansInFields[player][i] == 20:
            field[i] = "|   4    6    8   10   |"
    if numberOfFieldsInUse==2:
        print(str(field[0]) + "    " + str(field[1]))
        print("\\______________________/    \\______________________/")
    else:
       print(str(field[0]) + "    " + str(field[1]) + "    " + str(field[2]))
       print("\\______________________/    \\______________________/    \\______________________/")
def showHandOfPlayer(player):
    for i in range(len(playerHands[player])):
        if playerHands[player][i] == 6:
            print(str(i + 1) + ". Garden Bean (6)")
        elif playerHands[player][i] == 8:
            print(str(i + 1) + ". Red Bean (8)")
        elif playerHands[player][i] == 10:
            print(str(i + 1) + ". Black-Eyed Bean (10)")
        elif playerHands[player][i] == 12:
            print(str(i + 1) + ". Soy Bean (12)")
        elif playerHands[player][i] == 14:
            print(str(i + 1) + ". Green Bean (14)")
        elif playerHands[player][i] == 16:
            print(str(i + 1) + ". Stink Bean (16)")
        elif playerHands[player][i] == 18:
            print(str(i + 1) + ". Chili Bean (18)")
        elif playerHands[player][i] == 20:
            print(str(i + 1) + ". Blue Bean (20)")
def harvestBeans(player, field):
   if typeOfBeansInFields[player][field] == 6:
       print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Garden Beans")
       if quantityOfBeansInFields[player][field] >= 2:
           if quantityOfBeansInFields[player][field] >= 3:
               coins[player] += 3
               print(playerNames[player] + " earned 3 coins!")
           else:
               coins[player] += 2
               print(playerNames[player] + " earned 2 coins!")
   elif typeOfBeansInFields[player][field] == 8:
       print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Red Beans")
       if quantityOfBeansInFields[player][field] >= 2:
           if quantityOfBeansInFields[player][field] >= 3:
               if quantityOfBeansInFields[player][field] >= 4:
                   if quantityOfBeansInFields[player][field] >= 5:
                       coins[player] += 4
                       print(playerNames[player] + " earned 4 coins!")
                   else:
                       coins[player] += 3
                       print(playerNames[player] + " earned 3 coins!")
               else:
                   coins[player] += 2
                   print(playerNames[player] + " earned 2 coins!")
           else:
               coins[player] += 1
               print(playerNames[player] + " earned 1 coin!")
   elif typeOfBeansInFields[player][field] == 10:
       print(playerNames[player] + "is harvesting " + str(quantityOfBeansInFields[player][field]) + " Black-eyed Beans")
       if quantityOfBeansInFields[player][field] >= 2:
           if quantityOfBeansInFields[player][field] >= 4:
               if quantityOfBeansInFields[player][field] >= 5:
                   if quantityOfBeansInFields[player][field] >= 6:
                       coins[player] += 4
                       print(playerNames[player] + " earned 4 coins!")
                   else:
                       coins[player] += 3
                       print(playerNames[player] + " earned 3 coins!")
               else:
                   coins[player] += 2
                   print(playerNames[player] + " earned 2 coins!")
           else:
               coins[player] += 1
               print(playerNames[player] + " earned 1 coins!")
   elif typeOfBeansInFields[player][field] == 12:
       print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Soy Beans")
       if quantityOfBeansInFields[player][field] >= 2:
           if quantityOfBeansInFields[player][field] >= 4:
               if quantityOfBeansInFields[player][field] >= 6:
                   if quantityOfBeansInFields[player][field] >= 7:
                       coins[player] += 4
                       print(playerNames[player] + " earned 4 coins!")
                   else:
                       coins[player] += 3
                       print(playerNames[player] + " earned 3 coins!")
               else:
                   coins[player] += 2
                   print(playerNames[player] + " earned 2 coins!")
           else:
               coins[player] += 1
               print(playerNames[player] + " earned 1 coin!")
   elif typeOfBeansInFields[player][field] == 14:
       print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Green Beans")
       if quantityOfBeansInFields[player][field] >= 3:
           if quantityOfBeansInFields[player][field] >= 5:
               if quantityOfBeansInFields[player][field] >= 6:
                   if quantityOfBeansInFields[player][field] >= 7:
                       coins[player] += 4
                       print(playerNames[player] + " earned 4 coins!")
                   else:
                       coins[player] += 3
                       print(playerNames[player] + " earned 3 coins!")
               else:
                   coins[player] += 2
                   print(playerNames[player] + " earned 2 coins!")
           else:
               coins[player] += 1
               print(playerNames[player] + " earned 1 coin!")
   elif typeOfBeansInFields[player][field] == 16:
       print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Stink Beans")
       if quantityOfBeansInFields[player][field] >= 3:
           if quantityOfBeansInFields[player][field] >= 5:
               if quantityOfBeansInFields[player][field] >= 7:
                   if quantityOfBeansInFields[player][field] >= 8:
                       coins[player] += 4
                       print(playerNames[player] + " earned 4 coins!")
                   else:
                       coins[player] += 3
                       print(playerNames[player] + " earned 3 coins!")
               else:
                   coins[player] += 2
                   print(playerNames[player] + " earned 2 coins!")
           else:
               coins[player] += 1
               print(playerNames[player] + " earned 1 coin!")
   elif typeOfBeansInFields[player][field] == 18:
       print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Chili Beans")
       if quantityOfBeansInFields[player][field] >= 3:
           if quantityOfBeansInFields[player][field] >= 6:
               if quantityOfBeansInFields[player][field] >= 8:
                   if quantityOfBeansInFields[player][field] >= 9:
                       coins[player] += 4
                       print(playerNames[player] + " earned 4 coins!")
                   else:
                       coins[player] += 3
                       print(playerNames[player] + " earned 3 coins!")
               else:
                   coins[player] += 2
                   print(playerNames[player] + " earned 2 coins!")
           else:
               coins[player] += 1
               print(playerNames[player] + " earned 1 coin!")
   elif typeOfBeansInFields[player][field] == 20:
       print(playerNames[player] + " is harvesting " + str(quantityOfBeansInFields[player][field]) + " Blue Beans")
       if quantityOfBeansInFields[player][field] >= 4:
           if quantityOfBeansInFields[player][field] >= 6:
               if quantityOfBeansInFields[player][field] >= 8:
                   if quantityOfBeansInFields[player][field] >= 10:
                       coins[player] += 4
                       print(playerNames[player] + " earned 4 coins!")
                   else:
                       coins[player] += 3
                       print(playerNames[player] + " earned 3 coins!")
               else:
                   coins[player] += 2
                   print(playerNames[player] + " earned 2 coins!")
           else:
               coins[player] += 1
               print(playerNames[player] + " earned 1 coin!")
   quantityOfBeansInFields[player][field] = 0
   typeOfBeansInFields[player][field] = 0
cardNames=[0,1,2,3,4,5,"Garden Bean",7,"Red Bean",9,"Black-eyed Bean",11,"Soy Bean",13,"Green Bean",15,"Stink Bean",17,"Chili Bean",19,"Blue Bean"]
coins = [0, 0, 0, 0, 0]
typeOfBeansInFields = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0], [0, 0], [0, 0]]
quantityOfBeansInFields = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0], [0, 0], [1, 1]]
deck = shuffleAndCreateDeck()
tradingCards=[0,0]
print("How many players are there? There must be between 3 and 5 players.")
numberOfPlayers = int(input())
playerNames = []
lowercaseplayernames = []
if numberOfPlayers == 3:
    numberOfFieldsInUse = 3
else:
    numberOfFieldsInUse = 2
playerHands = [0, 0, 0, 0, 0]
for i in range(numberOfPlayers):
    print("What is player " + str(i) + "\'s name?")
    playerHands[i] = [deck.pop(0), deck.pop(1), deck.pop(2), deck.pop(3), deck.pop(4)]
    response = input()
    playerNames.append(response)
    lowercaseplayernames.append(response.lower())
print("Who most recently ate beans?")
startingPlayerName = input()
startingPlayer = playerNames.index(startingPlayerName)
playerTurn = startingPlayer
numberOfTimesDeckHasRunOut = 0
while True:
    print("It is now player " + playerNames[startingPlayer] + "'s turn")
    showFieldsOfPlayer(playerTurn)
    showHandOfPlayer(playerTurn)
    print("Where would you like to plant the first card in your hand (enter a number between 1 and "+str(numberOfFieldsInUse)+")?")
    response = int(input())
    if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][response - 1] == playerHands:
        harvestBeans(playerTurn, response - 1)
    quantityOfBeansInFields[playerTurn][response - 1] += 1
    typeOfBeansInFields[playerTurn][response - 1] = playerHands[playerTurn].pop(0)
    showFieldsOfPlayer(playerTurn)
    showHandOfPlayer(playerTurn)
    print("Would you like to plant the next card in your hand (enter \"yes\" or \"no\")?")
    response = input()
    if response.lower() == "yes":
        print("Where would you like to plant the first card in your hand (enter a number between 1 and "+str(numberOfFieldsInUse)+")?")
        response = int(input())
        if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][response - 1] == playerHands[playerTurn][0]:
            harvestBeans(playerTurn, response - 1)
        quantityOfBeansInFields[playerTurn][response - 1] += 1
        typeOfBeansInFields[playerTurn][response - 1] = playerHands[playerTurn][0]
    print("Here are the top two cards from the deck. "+playerNames[playerTurn]+" must decide whether to keep these cards or trade them.")
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
    for i in range(2):  #Trading stage (loop of range(2) because two cards are flipped over)
        if i == 0:
            print("Would anyone like to trade for the first card?")
        else:
            print("Would anyone like to trade for the second card?")
        print("If "+playerNames[playerTurn]+" would like this card (or no one else wants it), enter \"no\".")
        print("Otherwise, the non-active players should give offers to "+playerNames[playerTurn]+" and they should enter \"yes\"")
        response=input()
        if response.lower()=="no":
            print("Where would you like to plant this card (enter a number between 1 and "+str(numberOfFieldsInUse)+")?")
            response=int(input())
            if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][response - 1] == tradingCards[i]:
                harvestBeans(playerTurn, response - 1)
            quantityOfBeansInFields[playerTurn][response - 1] += 1
            typeOfBeansInFields[playerTurn][response - 1] = tradingCards[i]
        else:
            print("After "+playerNames[playerTurn]+" has decided on who to trade with, enter the name of that person.")
            tradingPlayer=lowercaseplayernames.index(input().lower())
            showFieldsOfPlayer(tradingPlayer)
            print("Where would "+playerNames[tradingPlayer]+" like to plant this card?")
            response = int(input())
            if not quantityOfBeansInFields[tradingPlayer][response - 1] == 0 and not typeOfBeansInFields[tradingPlayer][response - 1] == tradingCards[i]:
                harvestBeans(tradingPlayer, response - 1)
            quantityOfBeansInFields[tradingPlayer][response - 1] += 1
            typeOfBeansInFields[tradingPlayer][response - 1] = tradingCards[i]
            print("How many cards would "+playerNames[tradingPlayer]+" like to trade for this card? Enter a number between 0 and "+str(len(playerHands[tradingPlayer])))
            response = int(input())
            showHandOfPlayer(tradingPlayer)
            for j in range(response):
                if response != 1:
                    if str(j)[-1] == "0":
                        print("Enter the placement of the "+str(j+1)+"st card you want to trade with. Enter a number between 1 and "+str(len(playerHands[tradingPlayer])))
                    elif str(j)[-1] == "1":
                        print("Enter the placement of the "+str(j+1)+"nd card you want to trade with. Enter a number between 1 and "+str(len(playerHands[tradingPlayer])))
                    elif str(j)[-1] == "2":
                        print("Enter the placement of the "+str(j+1)+"rd card you want to trade with. Enter a number between 1 and "+str(len(playerHands[tradingPlayer])))
                    else:
                        print("Enter the placement of the "+str(j+1)+"th card you want to trade with. Enter a number between 1 and "+str(len(playerHands[tradingPlayer])))
                else:
                    print("Enter the placement of the card you want to trade with. Enter a number between 1 and "+str(len(playerHands[tradingPlayer])))
                tradingCardsOfOtherPlayer[j].append=input()
                playerHands[tradingPlayer][tradingCardsOfOtherPlayer[j][-1]] = 0
                showHandOfPlayer(tradingPlayer)
            showFieldsOfPlayer(tradingPlayer)
            print(playerNames[tradingPlayer]+", where would you like to plant your new "+cardNames[tradingCards[i]]+"?")
            response = int(input())
            if not quantityOfBeansInFields[tradingPlayer][response - 1] == 0 and not typeOfBeansInFields[tradingPlayer][response - 1] == tradingCards[i]:
                harvestBeans(tradingPlayer, response - 1)
            quantityOfBeansInFields[tradingPlayer][response - 1] += 1
            typeOfBeansInFields[tradingPlayer][response - 1] = tradingCards[i]
    for i in tradingCardsOfOtherPlayer:  #active player now plants the cards they got in trading
        print("Where would "+playerNames[playerTurn]+" like to plant their new "+cardNames[i]+"?")
        response = int(input())
        if not quantityOfBeansInFields[playerTurn][response - 1] == 0 and not typeOfBeansInFields[playerTurn][response - 1] == i:
            harvestBeans(playerTurn, response - 1)
        quantityOfBeansInFields[playerTurn][response - 1] += 1
        typeOfBeansInFields[playerTurn][response - 1] = i
    print(playerNames[playerTurn]+"now picks up three cards")
    for i in range(3):
        playerHands[playerTurn].append(deck.pop(0))
    showHandOfPlayer(playerTurn)
    if playerTurn != numberOfPlayers:
        playerTurn += 1
    else:
        playerTurn = 0










