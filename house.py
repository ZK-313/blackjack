import random
#from player import player
#player = player()
class house:
  def __init__(self):
    house.deck = {}
    house.imgCards = {}
    house.cardValues = []
    house.dealerValues = []
    #self.dealerSum = dealerSum
  def initializeDeck(self):
    cardCount = 2
    house.cardValues = []
    house.dealerValues = []
    sign = ['\u2663','\u2660','\u2666','\u2665']
    #range 0-12 = \u2663
    #range 13-25 = \u2660
    #range 26-38 = \u2666
    #range 39-51 = \u2665
    x = 0
    currentSign = sign[x]
    for i in range(52):
      if cardCount == 15:
        cardCount=2
        x = x+1
        #currentSign = sign[x]
      house.deck[i] = str(cardCount)
      cardCount+=1
    cardCount = 2
    imgCards = house.imgCards
    for i in range(52):
      if cardCount == 15:
        cardCount=2
      if house.deck[i] == '11': #checks through the deck for which number corresponds with the correct suit for 11, which is ace
        if i == 9:
          imgCards[i] = ("cards/ace_of_clubs.png")
        elif i == 22:
          imgCards[i] = ("cards/ace_of_spades.png")
        elif i == 35:
          imgCards[i] = ("cards/ace_of_diamonds.png")
        elif i == 48:
          imgCards[i] = ("cards/ace_of_hearts.png")
      elif house.deck[i] == '12': #jack
        if i == 10:
          imgCards[i] = ("cards/jack_of_clubs.png")
        elif i == 23:
          imgCards[i] = ("cards/jack_of_spades.png")
        elif i == 36:
          imgCards[i] = ("cards/jack_of_diamonds.png")
        elif i == 49:
          imgCards[i] = ("cards/jack_of_hearts.png")
      elif house.deck[i] == '13': #king
        if i == 11:
          imgCards[i] = ("cards/king_of_clubs.png")
        elif i == 24:
          imgCards[i] = ("cards/king_of_spades.png")
        elif i == 37:
          imgCards[i] = ("cards/king_of_diamonds.png")
        elif i == 50:
          imgCards[i] = ("cards/king_of_hearts.png")
      elif house.deck[i] == '14': #queen
        if i == 12:
          imgCards[i] = ("cards/queen_of_clubs.png")
        elif i == 25:
          imgCards[i] = ("cards/queen_of_spades.png")
        elif i == 38:
          imgCards[i] = ("cards/queen_of_diamonds.png")
        elif i == 51:
          imgCards[i] = ("cards/queen_of_hearts.png")
      else:
        if i >= 0 and i <= 12:
          imgCards[i] = ("cards/"+str(cardCount)+"_of_clubs.png")
        elif i >= 13 and i <= 25:
          imgCards[i] = ("cards/"+str(cardCount)+"_of_spades.png")
        elif i >= 26 and i <= 38:
          imgCards[i] = ("cards/"+str(cardCount)+"_of_diamonds.png")
        elif i >= 39 and i <= 51:
          imgCards[i] = ("cards/"+str(cardCount)+"_of_hearts.png")
      cardCount += 1
    return house.deck
  def dealPlayerCard(self):
    card1Num = random.randint(0,51)
    card2Num = random.randint(0,51)

    while card2Num == card1Num:
      card2Num = random.randint(0,51) #while the 2 cards selected are the same, the second card is changed
    if card1Num >= 0 and card1Num<=12:
      suit = '\u2663' #clubs
    elif card1Num >= 13 and card1Num <= 25:
      suit = '\u2660' #spades
    elif card1Num >= 26 and card1Num <= 38:
      suit = '\u2666' #diamonds
    elif card1Num >= 39 and card1Num <=51:
      suit = '\u2665' #hearts
    
    
    if card2Num >= 0 and card2Num<=12:
      suit2 = '\u2663'
    elif card2Num >= 13 and card2Num <= 25:
      suit2 = '\u2660'
    elif card2Num >= 26 and card2Num <= 38:
      suit2 = '\u2666'
    elif card2Num >= 39 and card2Num <=51:
      suit2 = '\u2665'
    house.cards = [house.deck[card1Num],suit,house.deck[card2Num],suit2]
    cardValues = house.cardValues
    if int(house.deck[card1Num])>11 and int(house.deck[card1Num])<=14:
      cardValue1 = 10
    else:
      cardValue1 = int(house.deck[card1Num])
    if int(house.deck[card2Num])>11 and int(house.deck[card2Num])<=14:
      cardValue2 = 10
    else:
      cardValue2 = int(house.deck[card2Num])
    cardValues.append(cardValue1)
    cardValues.append(cardValue2)
    #print(house.deck)
    house.deck[card1Num] = '0'
    house.deck[card2Num] = '0' #once cards have been dealt, their place in the deck is replaced with a 0
    return house.cards
  def dealerCard(self):
    card1Num = random.randint(0,51)
    card2Num = random.randint(0,51)

    while house.deck[card1Num] == '0'or house.deck[card2Num] == '0': #checks if the spot chosen is empty or not, if it is cards will be reshuffled
      card1Num = random.randint(0,51)
      card2Num = random.randint(0,51)

    while card2Num == card1Num:
      card2Num = random.randint(0,51)
    
    if card1Num >= 0 and card1Num<=12:
      suit = '\u2663'
    elif card1Num >= 13 and card1Num <= 25:
      suit = '\u2660'
    elif card1Num >= 26 and card1Num <= 38:
      suit = '\u2666'
    elif card1Num >= 39 and card1Num <=51:
      suit = '\u2665'
    
    
    if card2Num >= 0 and card2Num<=12:
      suit2 = '\u2663'
    elif card2Num >= 13 and card2Num <= 25:
      suit2 = '\u2660'
    elif card2Num >= 26 and card2Num <= 38:
      suit2 = '\u2666'
    elif card2Num >= 39 and card2Num <=51:
      suit2 = '\u2665'
    house.Dealercards = [house.deck[card1Num],suit,house.deck[card2Num],suit2]
    if int(house.deck[card1Num]) == 11:
      cardValue = 11
    elif int(house.deck[card1Num])>11 and int(house.deck[card1Num])<=14:
      cardValue = 10
    else:
      cardValue = int(house.deck[card1Num])
    if int(house.deck[card2Num]) == 11:
      cardValue2 = 11
    elif int(house.deck[card2Num])>11 and int(house.deck[card2Num])<=14:
      cardValue2 = 10
    else:
      cardValue2 = int(house.deck[card2Num])
    dealerValues = house.dealerValues
    dealerValues.append(cardValue)
    dealerValues.append(cardValue2)

    house.deck[card1Num] = '0'
    house.deck[card2Num] = '0'

    return self.Dealercards
  def dealExtraCard(self):
    cardNum = random.randint(0,51)
    while house.deck[cardNum] == '0':
      cardNum = random.randint(0,51)
    
    if cardNum >= 0 and cardNum<=12:
      suit = '\u2663'
    elif cardNum >= 13 and cardNum <= 25:
      suit = '\u2660'
    elif cardNum >= 26 and cardNum <= 38:
      suit = '\u2666'
    elif cardNum >= 39 and cardNum <=51:
      suit = '\u2665'

    DealerCards = house.Dealercards
    DealerCards.append(house.deck[cardNum])
    DealerCards.append(suit)

    if int(house.deck[cardNum]) == 11:
      cardValue = 11
    elif int(house.deck[cardNum])>11 and int(house.deck[cardNum])<=14:
      cardValue = 10
    else:
      cardValue = int(house.deck[cardNum])
    dealerValues = house.dealerValues
    dealerValues.append(cardValue)
    house.deck[cardNum] = '0'

  def retDealerSum(self):
    self.dealerSum = 0
    isEleven = 0
    for i in range(len(house.dealerValues)):
      self.dealerSum += house.dealerValues[i]
      if house.dealerValues[i] == 11:
        isEleven += 1
      if self.dealerSum > 21 and isEleven > 0:
        self.dealerSum -= 10
        isEleven -= 1
    #print(house.cardValues)
    return self.dealerSum