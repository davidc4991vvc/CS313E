#  File:                Blackjack.py
#  Description:         A game that is to be played between a human and the computer. Each is dealt two cards
#                       and the goal is to get as close to 21 without going over.
#  Student's Name:      Nicolas Key
#  Student's UT EID:    nak724
#  Course Name:         CS 313E 
#  Unique Number:       51915
#
#  Date Created:        2/17/2017
#  Date Last Modified:  2/24/2017

import random

class Deck:
    
    def __init__(self):
        suit = ["C", "D", "H", "S"]
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        self.cardList = []
        for i in range(0,4):
            for j in range(0,13):
                self.cardList.append(Card(suit[i], rank[j], value[j]))

    def __str__(self):
        myStr = ""
        for i in range(0, len(self.cardList)):
            
            if i == 13 or i == 26 or i == 39:
                myStr = myStr + "\n"
                
            myStr += " "
            if self.cardList[i].rank != "10":       #To make the columns line up
                myStr += " "
                
            myStr = myStr + str(self.cardList[i])            
        return myStr
                
    def shuffle(self):
        #random.seed(50)
        random.shuffle(self.cardList)

    def dealOne(self, player):
        nextCard = self.cardList.pop(0)
        player.hand.append(nextCard)
        player.handtotal += nextCard.value
        

class Card:

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return self.rank + self.suit

class Player:

    def __init__(self):
        self.hand = []
        self.handtotal = 0
        self.blackjack = False      #use to break blackjack tie. If opponent and dealer are dealt a blackjack,
                                    #dealer wins. Dealer doesn't get to hit if opponent is dealt a blackjack

    def __str__(self):              #Will return the list of cards in hand beginning and ending with " " (space)
        myStr = " "
        for i in self.hand:
            myStr = myStr + str(i) + " "
        return myStr



def showHands(opponent, dealer):
    print ("Dealer shows " + str(dealer.hand[1]) + " faceup.")
    print ("You show " + str(opponent.hand[1]) + " faceup.")




def opponentTurn(cardDeck, dealer, opponent):
    print("You go first")
    haveHighAce = False     #will never have more than one high ace

    if(opponent.hand[0].rank == "A" and opponent.hand[1].rank == "A"):
        print("You were dealt 2 aces. One will count as 11, the other as 1, for now.")
        opponent.handtotal = 12
        haveHighAce = True
    elif(opponent.hand[0].rank == "A" or opponent.hand[1].rank == "A"):
        print("You were dealt an ace. It will count as 11, for now.")
        haveHighAce = True

    if(opponent.handtotal == 21):
        print("Blackjack!")
        self.blackjack = True
        return

    while(1):
        if(opponent.handtotal == 21):
            print("21! My turn...\n\n")
            return
        if(opponent.handtotal > 21):
            print("Bust! You lose.\n\n")
            return

        print("You hold" + str(opponent) + "for a total of " + str(opponent.handtotal) + " points.")
        
        hit_stay = input("1 (hit) or 2 (stay)? ")
        if(hit_stay == "2"):
            print("You finished with a total of %d points.\n\n" % (opponent.handtotal))
            return
        elif(hit_stay == "1"):
            cardDeck.dealOne(opponent)
            print("Card dealt: " + str(opponent.hand[-1]))
            if(opponent.hand[-1].rank == "A"):
                if(opponent.handtotal > 10):
                    opponent.handtotal -= 10
                else:
                    haveHighAce = True
            if(haveHighAce and opponent.handtotal > 21):
                print("Switching ace from to be value 1")
                opponent.handtotal -= 10
                haveHighAce = False           
        else:
            print("That's not a valid input. Only enter a 1 or 2")
        


    
def dealerTurn(cardDeck, dealer, opponent):
    if(opponent.handtotal > 21):
        return
    if(opponent.blackjack):
        if(dealer.handtotal == 21):
            print("But dealer also has blackjack. Though luck. You lose.\nDealer wins.")
            return
        else:
            print("You win!")
            return
    print("Dealer's turn.")
    print("Your hand:" + str(opponent) + "for a total of " + str(opponent.handtotal) + " points")
    print("Dealer's hand:" + str(dealer) + "for a total of " + str(dealer.handtotal) + " points\n")

    haveHighAce = False
    if(dealer.hand[0].rank == "A" and dealer.hand[1].rank == "A"):
        haveHighAce = True
        dealer.handtotal = 12
    elif(dealer.hand[0].rank == "A" or dealer.hand[1].rank == "A"):
        haveHighAce = True

    while(1):                       # breaks out when dealer busts or wins
        if(dealer.handtotal > 21):
            print("Dealer busts. You win!")
            return
        if(dealer.handtotal >= opponent.handtotal):
            print("Dealer wins.")
            return

        cardDeck.dealOne(dealer)
        print("Dealer hits:", dealer.hand[-1])

        if(dealer.hand[-1].rank == "A"):
            if(dealer.handtotal > 21):
                print("Changing ace to 1 point")
                dealer.handtotal -= 10
            else:
                haveHighAce = True
                return

        if(haveHighAce == True and dealer.handtotal > 21):
            dealer.handtotal -= 10
            print("Changing ace to 1 point")
            haveHighAce = False
        print("Dealer points:", dealer.handtotal, "\n")
    

def main():
    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print(cardDeck, "\n")           # print the deck so we can see that you built it correctly
    
    random.seed(50)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print(cardDeck, " \n")          # print the deck so we can see that your shuffle worked
    
    dealer = Player()               # create the player:  you play for this Player
    opponent = Player()             # create the dealer:  the computer plays for this Player
    
    cardDeck.dealOne(opponent)      # face up
    cardDeck.dealOne(dealer)        # face down (the "hole" card)
    cardDeck.dealOne(opponent)      # face up
    cardDeck.dealOne(dealer)        # face up
    
    showHands(opponent,dealer)      # remember not to show face down cards
    
    opponentTurn(cardDeck,dealer,opponent)     # this is where half of the hard stuff is done
    dealerTurn(cardDeck,dealer,opponent)       # this is where the other half of the hard stuff is done
    
    print ("Game over.")
    print ("Final hands:")
    print ("   Dealer:   ", dealer)
    print ("   Opponent: ", opponent)
    

main()
