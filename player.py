from house import house
import random

dealer = house()

class player:
    def __init__(self):
        self.deck = dealer.deck
        self.PlayerSum = 0
        #house.cardValues = []
    def hit(self):
        card1Num = random.randint(0,51)
        while dealer.deck[card1Num] == '0':
            card1Num = random.randint(0,51)
        if card1Num >= 0 and card1Num<=12:
            suit = '\u2663'
        elif card1Num >= 13 and card1Num <= 25:
            suit = '\u2660'
        elif card1Num >= 26 and card1Num <= 38:
            suit = '\u2666'
        elif card1Num >= 39 and card1Num <=51:
            suit = '\u2665'
        playerCards = dealer.cards
        playerCards.append(dealer.deck[card1Num])
        playerCards.append(suit)
        if int(dealer.deck[card1Num]) == 11:
          cardValue = 11
        elif int(dealer.deck[card1Num])>11 and int(dealer.deck[card1Num])<=14:
          cardValue = 10
        else:
          cardValue = int(dealer.deck[card1Num])
        cardValues = house.cardValues
        cardValues.append(cardValue)
        dealer.deck[card1Num] = '0'
    def retPlayerSum(self):
        self.PlayerSum = 0
        isEleven = 0
        for i in range(len(house.cardValues)):
          self.PlayerSum += house.cardValues[i]
          if house.cardValues[i] == 11:
            isEleven += 1
          if self.PlayerSum > 21 and isEleven > 0:
            self.PlayerSum -= 10
            isEleven -= 1
        #print(house.cardValues)
        return self.PlayerSum