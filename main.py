# 11/15/2022 BlackJack by Zulfiqar Ali Khan Note: Bets may not be realistic, all bets return double the amount of
# won, and triple of won by blackjack eg: bet = 50, win will add 50 to the player's balance, and a win by blackjack
# will add 100 to the player's balance, while a loss would remove 50 from the player's balance. code fore readjusting
# aces is within the retDealerSum/retPlayerSum function
#

from tkinter import *
from PIL import ImageTk, Image
from hold import hold
from background import background
from house import house
from player import player


def findSuit(x):  # finding suit
    if x == '\u2663':
        suit1 = "clubs"
    elif x == '\u2660':
        suit1 = "spades"
    elif x == '\u2666':
        suit1 = "diamonds"
    elif x == '\u2665':
        suit1 = "hearts"
    return suit1


def blackJack():  # checking for blackjack
    global credits  # credits and bet global variables
    global bet
    global hit
    global hold
    sum = player.retPlayerSum()
    if sum == 21:  # since a player can only have 21 on his first hand if it is a blackjack, this function is only
      # run after the first hand has been dealt, and before the player can press hit or hold
        hit.grid_forget()
        hold.grid_forget()
        dealerSum = dealer.retDealerSum()
        while dealerSum < 17:
            dealer.dealExtraCard()
            dealerSum = dealer.retDealerSum()
        printedDealerSum = Label(root, text="Dealer Total:\n" + str(dealerSum), font=('Verdana', 9), borderwidth=2,
                                 relief="solid").grid(row=2, column=2, columnspan=3)
        global dealerImgs  # image list must be global for tkinter to recognize it
        dealerImgs = []
        randomNum1 = 0  # used as a number that goes up by 1 in a for loop, as "i" in the for loop increments by 2
        printNum1 = 0  # also used as a number that goes up by 1, but is used specifically for the column where the
      # image will be placed
        dealerCardVal = []
        dealerSuits = []

        for i in range(0, len(dealer.Dealercards), 2):
            dealerCardVal.append(int(dealer.Dealercards[
                                         i]))  # adds card values to a list; dealer.Dealercards and dealer.cards have
            # the first element as the card value, and second as suit, continuing with this pattern
            dealerSuits.append(findSuit(dealer.Dealercards[i + 1]))
            # print(cardVal)
            # print(suits)
            #print(dealer.Dealercards)
            #print(dealerCardVal)
            #print("CARD VAL = " + str(dealerCardVal[randomNum1]))
            if dealerCardVal[randomNum1] >= 2 and dealerCardVal[randomNum1] <= 10:
                dealerImgs.append(ImageTk.PhotoImage((Image.open(
                    "cards/" + str(dealerCardVal[randomNum1]) + "_of_" + dealerSuits[randomNum1] + ".png")).resize(
                    (80, 120))))
            elif dealerCardVal[randomNum1] == 11:
                dealerImgs.append(ImageTk.PhotoImage(
                    (Image.open("cards/ace_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
            elif dealerCardVal[randomNum1] == 12:
                dealerImgs.append(ImageTk.PhotoImage(
                    (Image.open("cards/jack_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
            elif dealerCardVal[randomNum1] == 13:
                dealerImgs.append(ImageTk.PhotoImage(
                    (Image.open("cards/king_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
            elif dealerCardVal[randomNum1] == 14:
                dealerImgs.append(ImageTk.PhotoImage(
                    (Image.open("cards/queen_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
            #print(randomNum1)
            #print(dealerImgs)
            Label(root, image=dealerImgs[randomNum1], borderwidth=1, relief="solid").grid(row=1, column=printNum1)
            printNum1 += 1
            if printNum1 > 10:
                break
            randomNum1 += 1
        randomNum1 = 0
        printNum1 = 2
        if len(dealer.cards) <= 4:  # checks if the dealer's 21 was on their first hand or not
            if dealerSum == 21:  # if it was on their first hand, checks for blackjack
                if ((dealerCardVal[1] == 10 or dealerCardVal[1] == 12 or dealerCardVal[1] == 13 or dealerCardVal[
                    1] == 14) or dealerCardVal[1] == 11) and ((dealerCardVal[0] == 10 or dealerCardVal[0] == 12 or
                                                               dealerCardVal[0] == 13 or dealerCardVal[0] == 14) or
                                                              dealerCardVal[0] == 11):
                    Label(root, text="You both win! Bets stay the same.", font=('Verdana', 9), borderwidth=2,
                          relief="solid").grid(row=2, column=0, columnspan=3)
                    root.after(1000, showPlayWin)  # waits 1 second before displaying the play window
                else:
                    Label(root, text="Blackjack! You win!", font=('Verdana', 9), borderwidth=2, relief="solid").grid(
                        row=2, column=0, columnspan=3)
                    if bet != '':  # if bet is a number, since the bet field can be chosen to be left empty by the player
                        credits += int(bet) * 2
                    root.after(1000, showPlayWin)
            else:
                Label(root, text="Blackjack! You win!", font=('Verdana', 9), borderwidth=2, relief="solid").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 columnspan=3)
                if bet != '':
                    credits += int(bet) * 2
                root.after(1000, showPlayWin)
        else:
            Label(root, text="Blackjack! You win!", font=('Verdana', 9), borderwidth=2, relief="solid").grid(row=2,
                                                                                                             column=0,
                                                                                                             columnspan=3)
            if bet != '':
                credits += int(bet) * 2
            root.after(1000, showPlayWin)


def showPlayWin():  # function used to show the play window (the window with the bet info and play button)
    printCredits = credits + 500  # credits variable is 0, and your balance is always credits+500 (used this to debug
    # adding and subtracting errors and was too lazy to change it back once they were fixed)
    money = Label(playWindow, text="Your credits: " + str(printCredits), font=('Verdana bold', 9))
    money.place(anchor=CENTER, relx=.5, rely=.25, width=350)  # places your balance on the play window
    # lockIn.place(anchor = CENTER, relx = .25, rely = .7)
    return playWindow.deiconify()  # shows play window


def hideRootWin():
    return root.withdraw()  # hides root window (used at the start of the game before the player has clicked play)


def exitAll():  # used to exit all windows and shut down the program
    root.destroy()  # as long as root is destroyed, the whole program will close


def onButton():  # used to gather bet information from the entry field
    global bet
    bet = betButton.get()


def runPlaying():  # used for the play button so that it can both run the game, and gather bet info
    money.place_forget()
    onButton()
    playing()  # everything in the game is within the playing function


def rules():  # function for the rules page
    rulesBut.place_forget()  # hides rules button since the rules can only be read once
    rulesWindow.deiconify()  # shows rules window
    exitRules = Button(rulesWindow, text="EXIT", font=("Verdana", 9), command=rulesClose, bg='red', fg='white',
                       borderwidth=2, relief="solid")
    exitRules.place(anchor=CENTER, relx=.9, rely=.05)
    Label(rulesWindow, text="RULES", font=("Helvetica bold", 20), borderwidth=1, relief='solid').place(anchor=CENTER,
                                                                                                       relx=.5,
                                                                                                       rely=.15)
    Label(rulesWindow,
          text="- Each player is dealt a hand to begin the game\n - Card values:\n    A = 11 or 1\n    J, K, "
               "Q = 10\n    All other cards are worth their number\n - Aces readjust themselves to stay under 21\n - "
               "One of the dealer’s cards starts face down\n - The player can choose to hit or hold\n - Hitting adds "
               "a card to the player’s hand\n - If the sum of the player’s cards goes over 21, you lose!\n - Holding "
               "lets you see if you beat the dealer\n - If your sum is more than the dealer’s\n   or his sum is over "
               "21, you win!\n - If the dealer has a higher sum than you,You lose!\n - The dealer must hit if his "
               "original hand\n   does not add up to at least 17\n - If either party receives an ace and a card worth "
               "10,\n    it is a blackjack, meaning they win,\n    unless the other party also has one!\n - Bets: "
               "return double unless you win by blackjack\n    which returns triple!",
          justify=LEFT, borderwidth=1, relief='solid').place(anchor=CENTER, relx=.5, rely=.55)  # rules


def rulesClose():  # used for the rules closing warning so that players dont accidentally close the rules
    def closedarules():
        rulesWindow.destroy()
        closeWin.destroy()

    def dontclosedarules():
        closeWin.destroy()

    closeWin = Toplevel(rulesWindow)
    closeWin.geometry("300x150")
    Label(closeWin, text="Are you sure you want to close?\nYou will NOT be able to return to the rules.").place(
        anchor=CENTER, relx=.5, rely=.2)
    yes = Button(closeWin, text="YES", font=("Verdana", 9), command=closedarules, bg='green', fg='white')
    yes.place(anchor=CENTER, relx=.65, rely=.6)
    no = Button(closeWin, text='NO', font=("Verdana", 9), command=dontclosedarules, bg='red', fg='white')
    no.place(anchor=CENTER, relx=.35, rely=.6)


credits = 0  # defines our credits
root = Tk()  # root
dealer = house()  # house class
player = player()  # player class
playWindow = Toplevel(root)  # creates play window
rulesWindow = Toplevel(playWindow)  # creates rules window
# playWindow.configure(bg='gray2')
rulesWindow.geometry("400x500")  # sets size of rules window
rulesWindow.configure(bg='#22b14c')  # sets background of rules window
playWindow.geometry("350x150")  # sets size of play window
rulesWindow.withdraw()
root.withdraw()  # hides root window until the play button is pressed


def playing():  # the whole game is within this function
    global credits
    global bet
    global hit
    global hold
    # play.grid_forget()
    playWindow.withdraw()  # hides play window while the game is ongoing
    root.deiconify()  # shows root window to start game
    table = background(root)  # creates background/canvas
    dealer.initializeDeck()  # creates a new deck everytime it is run
    dealer.dealPlayerCard()  # deals the player cards
    dealer.dealerCard()  # deals the dealer cards

    cardVal = []  # hold the values of player cards

    dealerSuit1 = findSuit(dealer.Dealercards[1])  # holds dealer suits
    dealerSuit2 = findSuit(dealer.Dealercards[3])

    global card1  # all cards must be global for tkinter to recognize them
    global card2
    global dealerCard1
    global dealerCard2
    if int(dealer.Dealercards[0]) >= 2 and int(dealer.Dealercards[0]) <= 10:  # checks for special cards
        dealerCard1 = Image.open("cards/" + dealer.Dealercards[0] + "_of_" + dealerSuit1 + ".png")
    elif dealer.Dealercards[0] == '11':
        dealerCard1 = Image.open("cards/ace_of_" + dealerSuit1 + ".png")
    elif dealer.Dealercards[0] == '12':
        dealerCard1 = Image.open("cards/jack_of_" + dealerSuit1 + ".png")
    elif dealer.Dealercards[0] == '13':
        dealerCard1 = Image.open("cards/king_of_" + dealerSuit1 + ".png")
    elif dealer.Dealercards[0] == '14':
        dealerCard1 = Image.open("cards/queen_of_" + dealerSuit1 + ".png")

    dealerCard1 = dealerCard1.resize((80, 120))
    dealerCard1 = ImageTk.PhotoImage(dealerCard1)

    dealerCard2 = Image.open("cards/cardback.png")
    dealerCard2 = dealerCard2.resize((80, 120))
    dealerCard2 = ImageTk.PhotoImage(dealerCard2)

    Label(root, image=dealerCard1, borderwidth=1, relief="solid").grid(row=1,
                                                                       column=0)  # displays dealer's cards on the screen
    Label(root, image=dealerCard2, borderwidth=1, relief="solid").grid(row=1, column=1)

    suit1 = findSuit(dealer.cards[1])
    if int(dealer.cards[0]) >= 2 and int(dealer.cards[0]) <= 10:
        card1 = Image.open("cards/" + dealer.cards[0] + "_of_" + suit1 + ".png")
    elif dealer.cards[0] == '11':
        card1 = Image.open("cards/ace_of_" + suit1 + ".png")
    elif dealer.cards[0] == '12':
        card1 = Image.open("cards/jack_of_" + suit1 + ".png")
    elif dealer.cards[0] == '13':
        card1 = Image.open("cards/king_of_" + suit1 + ".png")
    elif dealer.cards[0] == '14':
        card1 = Image.open("cards/queen_of_" + suit1 + ".png")
    card1 = card1.resize((80, 120))
    card1 = ImageTk.PhotoImage(card1)
    # cardVal.append(int(dealer.cards[0]))

    # cardDumb = (ImageTk.PhotoImage((Image.open("cards/ace_of_diamonds.png")).resize((80,120))))

    # Label(root,image = cardDumb).grid(row=3,column=0)

    suit2 = findSuit(dealer.cards[3])
    if int(dealer.cards[2]) >= 2 and int(dealer.cards[2]) <= 10:
        card2 = Image.open("cards/" + dealer.cards[2] + "_of_" + suit2 + ".png")
    elif dealer.cards[2] == '11':
        card2 = Image.open("cards/ace_of_" + suit2 + ".png")
    elif dealer.cards[2] == '12':
        card2 = Image.open("cards/jack_of_" + suit2 + ".png")
    elif dealer.cards[2] == '13':
        card2 = Image.open("cards/king_of_" + suit2 + ".png")
    elif dealer.cards[2] == '14':
        card2 = Image.open("cards/queen_of_" + suit2 + ".png")
    card2 = card2.resize((80, 120))
    card2 = ImageTk.PhotoImage(card2)
    # cardVal.append(int(dealer.cards[2]))

    Label(root, image=card1, borderwidth=1, relief="solid").grid(row=3, column=0)  # displays player's cards
    Label(root, image=card2, borderwidth=1, relief="solid").grid(row=3, column=1)
    sum = player.retPlayerSum()
    Label(root, text="Total: " + str(sum), font=('Verdana', 9), borderwidth=2, relief="solid").grid(row=4, column=2,
                                                                                                    columnspan=3)  # displays the player's total score

    root.after(500, blackJack)  # after 0.5 seconds, checks for blackjack before the player has time to hit or hold

    def hitting():  # run when player presses hit button
        global credits
        global bet
        player.hit()  # runs hit function in player class, which distributes a card to their hand
        sum = player.retPlayerSum()  # updates player sum
        sumText = Label(root, text="Your Total: \n" + str(sum), borderwidth=2, relief="solid", font=('Verdana', 9))
        sumText.grid(row=4, column=2, columnspan=3)  # shows updated player sum
        # print(dealer.cards)
        randomNum = 0  # all variables called randomNum and printNum or randomNum1 and printNum1 are used for the same purpose; to serve as a number incrementing by 1 for either adding cards to an array, or change the column for images to be printed to the screen, since my for loops increment by 2 to make it easier to read from my hand
        printNum = 0
        suits = []
        global imgs
        imgs = []
        cardVal = []

        for i in range(0, len(dealer.cards), 2):
            cardVal.append(int(dealer.cards[i]))  # adds player card values to array
            suits.append(findSuit(dealer.cards[i + 1]))  # adds corresponding suits to array
            # print(cardVal)
            # print(suits)
            # print("CARD VAL = "+str(cardVal[randomNum]))
            if cardVal[randomNum] >= 2 and cardVal[randomNum] <= 10:
                imgs.append(ImageTk.PhotoImage(
                    (Image.open("cards/" + str(cardVal[randomNum]) + "_of_" + suits[randomNum] + ".png")).resize(
                        (80, 120))))
            elif cardVal[randomNum] == 11:
                imgs.append(
                    ImageTk.PhotoImage((Image.open("cards/ace_of_" + suits[randomNum] + ".png")).resize((80, 120))))
            elif cardVal[randomNum] == 12:
                imgs.append(
                    ImageTk.PhotoImage((Image.open("cards/jack_of_" + suits[randomNum] + ".png")).resize((80, 120))))
            elif cardVal[randomNum] == 13:
                imgs.append(
                    ImageTk.PhotoImage((Image.open("cards/king_of_" + suits[randomNum] + ".png")).resize((80, 120))))
            elif cardVal[randomNum] == 14:
                imgs.append(
                    ImageTk.PhotoImage((Image.open("cards/queen_of_" + suits[randomNum] + ".png")).resize((80, 120))))
            #print(imgs[randomNum])
            Label(root, image=imgs[randomNum], borderwidth=1, relief="solid").grid(row=3, column=printNum)
            printNum += 1
            if printNum > 10:
                break
            randomNum += 1

        randomNum = 0
        printNum = 2

        if sum > 21:  # checks if player has gone over 21
            hit.grid_forget()  # removes hit and hold button from screen so that player cannot hit hold again
            hold.grid_forget()
            dealerSum = dealer.retDealerSum()  # counts dealer's sum
            # while dealerSum < 17:
            # dealer.dealExtraCard()
            # dealerSum = dealer.retDealerSum()
            printedDealerSum = Label(root, text="Dealer Total:\n" + str(dealerSum), font=('Verdana', 9), borderwidth=2,
                                     relief="solid").grid(row=2, column=2,
                                                          columnspan=3)  # displays dealer's sum on the screen
            global dealerImgs
            dealerImgs = []
            randomNum1 = 0
            printNum1 = 0
            dealerCardVal = []
            dealerSuits = []

            for i in range(0, len(dealer.Dealercards), 2):
                dealerCardVal.append(int(dealer.Dealercards[i]))  # adds dealer card values to an array
                dealerSuits.append(
                    findSuit(dealer.Dealercards[i + 1]))  # adds corresponding dealer card suits to an array
                # print(cardVal)
                # print(suits)
                #print(dealer.Dealercards)
                #print(dealerCardVal)
                #print("CARD VAL = " + str(dealerCardVal[randomNum1]))
                if dealerCardVal[randomNum1] >= 2 and dealerCardVal[
                    randomNum1] <= 10:  # checks card value and adds corresponding image to an array for displaying
                    dealerImgs.append(ImageTk.PhotoImage((Image.open(
                        "cards/" + str(dealerCardVal[randomNum1]) + "_of_" + dealerSuits[randomNum1] + ".png")).resize(
                        (80, 120))))
                elif dealerCardVal[randomNum1] == 11:
                    dealerImgs.append(ImageTk.PhotoImage(
                        (Image.open("cards/ace_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
                elif dealerCardVal[randomNum1] == 12:
                    dealerImgs.append(ImageTk.PhotoImage(
                        (Image.open("cards/jack_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
                elif dealerCardVal[randomNum1] == 13:
                    dealerImgs.append(ImageTk.PhotoImage(
                        (Image.open("cards/king_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
                elif dealerCardVal[randomNum1] == 14:
                    dealerImgs.append(ImageTk.PhotoImage(
                        (Image.open("cards/queen_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
                #print(randomNum1)
                #print(dealerImgs)
                Label(root, image=dealerImgs[randomNum1], borderwidth=1, relief="solid").grid(row=1,
                                                                                              column=printNum1)  # updates dealer's cards on the screen
                printNum1 += 1
                if printNum > 10:
                    break
                randomNum1 += 1
            randomNum1 = 0
            printNum1 = 2
            # if dealerSum <= 21:
            Label(root, text="You went over 21, you lose!", font=('Verdana', 9), borderwidth=2, relief="solid").grid(
                row=2, column=0, columnspan=3)
            # showWin = playWindow.deiconify()
            if bet != '':
                credits -= int(bet)  # subtracts the bet from user's balance
            root.after(1000, showPlayWin)  # allows play window to reappear so that the player can play again

    def holding():  # runs when player presses hold button
        global credits
        global bet
        hit.grid_forget()  # gets rid of hit and hold button so that player cannot hit or hold again
        hold.grid_forget()
        dealerSum = dealer.retDealerSum()  # counts dealer's sum
        while dealerSum < 17:  # while the dealers sum is less than 17, they will hit
            dealer.dealExtraCard()  # function within house class which hits a card to the dealer's hand
            dealerSum = dealer.retDealerSum()  # updates dealer sum
        printedDealerSum = Label(root, text="Dealer Total:\n" + str(dealerSum), font=('Verdana', 9), borderwidth=2,
                                 relief="solid").grid(row=2, column=2,
                                                      columnspan=3)  # displays dealer total on the screen
        global dealerImgs
        dealerImgs = []
        randomNum1 = 0
        printNum1 = 0
        dealerCardVal = []
        dealerSuits = []

        for i in range(0, len(dealer.Dealercards), 2):
            dealerCardVal.append(int(dealer.Dealercards[i]))
            dealerSuits.append(findSuit(dealer.Dealercards[i + 1]))
            # print(cardVal)
            # print(suits)
            #print(dealer.Dealercards)
            #print(dealerCardVal)
            #print("CARD VAL = " + str(dealerCardVal[randomNum1]))
            if dealerCardVal[randomNum1] >= 2 and dealerCardVal[randomNum1] <= 10:
                dealerImgs.append(ImageTk.PhotoImage((Image.open(
                    "cards/" + str(dealerCardVal[randomNum1]) + "_of_" + dealerSuits[randomNum1] + ".png")).resize(
                    (80, 120))))
            elif dealerCardVal[randomNum1] == 11:
                dealerImgs.append(ImageTk.PhotoImage(
                    (Image.open("cards/ace_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
            elif dealerCardVal[randomNum1] == 12:
                dealerImgs.append(ImageTk.PhotoImage(
                    (Image.open("cards/jack_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
            elif dealerCardVal[randomNum1] == 13:
                dealerImgs.append(ImageTk.PhotoImage(
                    (Image.open("cards/king_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
            elif dealerCardVal[randomNum1] == 14:
                dealerImgs.append(ImageTk.PhotoImage(
                    (Image.open("cards/queen_of_" + dealerSuits[randomNum1] + ".png")).resize((80, 120))))
            #print(randomNum1)
            #print(dealerImgs)
            Label(root, image=dealerImgs[randomNum1], borderwidth=1, relief="solid").grid(row=1, column=printNum1)
            printNum1 += 1
            randomNum1 += 1
        randomNum1 = 0
        printNum1 = 2
        sum = player.retPlayerSum()  # updates player sum for hold function
        if dealerSum == 21:  # checks if dealer has 21
            if ((dealerCardVal[1] == 10 or dealerCardVal[1] == 12 or dealerCardVal[1] == 13 or dealerCardVal[
                1] == 14) or dealerCardVal[1] == 11) and ((dealerCardVal[0] == 10 or dealerCardVal[0] == 12 or
                                                           dealerCardVal[0] == 13 or dealerCardVal[0] == 14) or
                                                          dealerCardVal[
                                                              0] == 11):  # checks if dealer's first 2 cards were a blackjack or not
                Label(root, text="Dealer BlackJack! Dealer wins!", font=('Verdana', 9), borderwidth=2,
                      relief="solid").grid(row=2, column=0, columnspan=3)
                if bet != '':
                    credits -= int(bet)
                root.after(1000, showPlayWin)
                return False  # breaks out of hold function
            # if not a blackjack, dealer having 21 is handled later on

        if dealerSum > 21:
            Label(root, text="Dealer went over 21\n you WIN!", font=('Verdana', 9), borderwidth=2, relief="solid").grid(
                row=2, column=0, columnspan=3)
            if bet != '':
                credits += int(
                    bet)  # adds what the player bet onto their balance (my code does not update the bet right away, only when the player has won or lost)
            root.after(1000, showPlayWin)
            # root.after(5000,hideRootWin)
        elif sum > dealerSum:  # checks if player's sum is above dealer's sum
            Label(root, text="You beat the dealer!", font=('Verdana', 9), borderwidth=2, relief="solid").grid(row=2,
                                                                                                              column=0,
                                                                                                              columnspan=3)
            if bet != '':
                credits += int(bet)
            root.after(1000, showPlayWin)
            # root.after(5000,hideRootWin)
        elif dealerSum > sum:  # checks if dealer's sum is above player sum
            Label(root, text="Dealer beat you!", font=('Verdana', 9), borderwidth=2, relief="solid").grid(row=2,
                                                                                                          column=0,
                                                                                                          columnspan=3)
            if bet != '':
                credits -= int(bet)
            root.after(1000, showPlayWin)
            # root.after(5000,hideRootWin)
        elif dealerSum == sum:  # a tie or push
            Label(root, text="It's a tie!", font=('Verdana', 9), borderwidth=2, relief="solid").grid(row=2, column=0,
                                                                                                     columnspan=3)
            root.after(1000, showPlayWin)
            # root.after(5000,hideRootWin)
        hit.grid_forget()
        hold.grid_forget()
        # play.grid(row=0,column=0)

    hit = Button(root, text="HIT", font=('Verdana', 9), command=hitting, borderwidth=2, relief="solid",
                 bg='green')  # creates hit button (Created inside playing function so that they show after the background is made)
    hit.grid(row=0, column=2)

    hold = Button(root, text="HOLD", font=('Verdana', 9), command=holding, borderwidth=2, relief="solid", bg='#E1CF38')
    hold.grid(row=0, column=3)

    exit2 = Button(root, text="EXIT", font=("Verdana", 9), command=exitAll, bg='red', fg='black', borderwidth=2,
                   relief="solid")
    exit2.grid(row=0, column=4)


# creates buttons
play = Button(playWindow, text="PLAY", font=('Verdana', 9), command=runPlaying, bg='green', fg='white', borderwidth=2,
              relief="solid")
rulesBut = Button(playWindow, text="RULES", font=('Verdana', 9), command=rules, bg='black', fg='white', borderwidth=2,
                  relief="solid")
exit = Button(playWindow, text="EXIT", font=("Verdana", 9), command=exitAll, bg='red', fg='white', borderwidth=2,
              relief="solid")
printCredits = credits + 500
money = Label(playWindow, text="Your credits: " + str(printCredits), font=('Verdana bold', 9))
betStatement = Label(playWindow, text="BET: (Leave empty to play for fun!)", font=('Verdana', 9))
betButton = Entry(playWindow, width=35, borderwidth=5)

# places buttons on the screen
money.place(anchor=CENTER, relx=.5, rely=.25)
betStatement.place(anchor=CENTER, relx=.5, rely=.1)
exit.place(anchor=CENTER, relx=.93, rely=.1)
betButton.place(anchor=CENTER, relx=.5, rely=.45)
rulesBut.place(anchor=CENTER, relx=.25, rely=.7)
play.place(anchor=CENTER, relx=.5, rely=.7)

betButton.bind('<FocusIn>', lambda x: betButton.selection_range(0,
                                                                END))  # if anything was inserted to the bet field before the player clicked it, it would automatically highlight to be removed as soon as the player clicked the field (was experimenting with this)
global bet
bet = 0
bet = (betButton.get())  # used to get the bet for the first game
#print(bet)
# play.grid(row=1,column=1)

playWindow.protocol("WM_DELETE_WINDOW",
                    exitAll)  # if the x button is pressed on the play button window, the while program is closed
# playWindow.bind('<Return>', enterPlaying)
rulesWindow.protocol("WM_DELETE_WINDOW",
                     rulesClose)  # if the x button is pressed on the rules window, it runs the rulesClose function which was shown above
root.mainloop()
