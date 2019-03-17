import random


class Card:
  def __init__(self,value,suit,name, typeOfCard):
  	self.value = value
  	self.suit = suit
  	self.name = name
  	self.typeOfCard = typeOfCard

  def getValue(self):
  	return self.value

  def getSuit(self):
  	return self.suit

  def getName(self):
  	return self.name

def reloadCards():
	hearts2 = Card(2,"hearts", "2 of hearts", "Two")
	diamonds2 = Card(2, "diamonds", '2 of diamonds', 'Two')
	spades2 = Card(2, "spades", '2 of spades', 'Two')
	clubs2 = Card(2, "clubs",'2 of clubs', 'Two')
	hearts3 = Card(3, "hearts", '3 of hearts', 'Three')
	diamonds3 = Card(3, "diamonds",'3 of diamonds', 'Three')
	spades3 = Card(3, "spades", '3 of spades', 'Three')
	clubs3 = Card(3, "clubs", '3 of clubs', 'Three')
	hearts4 = Card(4, "hearts",'4 of hearts','Four')
	diamonds4 = Card(4, "diamonds",'4 of diamonds', 'Four')
	spades4 = Card(4, "spades", '4 of spades', 'Four')
	clubs4 = Card(4, "clubs",'4 of clubs', 'Four')
	hearts5 = Card(5, "hearts",'5 of hearts', 'Five')
	diamonds5 = Card(5, "diamonds",'5 of diamonds', 'Five')
	spades5 = Card(5, "spades",'5 of spades', 'Five')
	clubs5 = Card(5, "clubs", '5 of clubs', 'Five')
	hearts6 = Card(6, "hearts",'6 of hearts', 'Six')
	diamonds6 = Card(6, "diamonds",'6 of diamonds', ' Six')
	spades6 = Card(6, "spades",'6 of spades', 'Six')
	clubs6 = Card(6, "clubs",'6 of clubs', 'Six')
	hearts7 = Card(7, "hearts",'7 of hearts', 'Seven')
	diamonds7 = Card(7, "diamonds",'7 of diamonds', 'Seven')
	spades7 = Card(7, "spades", '7 of spades', 'Seven')
	clubs7 = Card(7, "clubs",'7 of clubs', 'Seven')
	hearts8 = Card(8, "hearts",'8 of hearts', "Eight")
	diamonds8 = Card(8, "diamonds",'8 of diamonds', 'Eight')
	spades8 = Card(8, "spades",'8 of spades', 'Eight')
	clubs8 = Card(8, "clubs",'8 of clubs', 'Eight')
	hearts9 = Card(9, "hearts",'9 of hearts', 'Nine')
	diamonds9 = Card(9, "diamonds",'9 of diamonds', 'Nine')
	spades9 = Card(9, "spades",'9 of spades', 'Nine')
	clubs9 = Card(9, "clubs",'9 of clubs', 'Nine')
	hearts10 = Card(10, "hearts",'10 of hearts', 'Ten')
	diamonds10 = Card(10, "diamonds",'10 of diamonds', 'Ten')
	spades10 = Card(10, "spades",'10 of spades', 'Ten')
	clubs10 = Card(10, "clubs",'10 of clubs', 'Ten')
	Jackhearts = Card(10, "hearts",'Jack of hearts', 'Jack')
	Jackdiamonds = Card(10, "diamonds",'Jack of diamonds', 'Jack')
	Jackspades = Card(10, "spades",'Jack of spades', 'Jack')
	Jackclubs = Card(10, "clubs",'Jack of clubs', 'Jack')
	Queenhearts = Card(10, "hearts",'Queen of hearts', 'Queen')
	Queendiamonds = Card(10, "diamonds",'Queen of diamonds', 'Queen')
	Queenspades = Card(10, "spades",'Queen of spades', 'Queen')
	Queenclubs = Card(10, "clubs",'Queen of clubs', 'Queen')
	Kinghearts = Card(10, "hearts",'King of hearts', 'King')
	Kingdiamonds = Card(10, "diamonds",'King of diamonds', 'King')
	Kingspades = Card(10, "spades",'King of spades', 'King')
	Kingclubs = Card(10, "clubs",'King of clubs', 'King')
	Acehearts = Card(11, "hearts",'Ace of hearts', 'Ace')
	Acediamonds = Card(11, "diamonds",'Ace of diamonds', 'Ace')
	Acespades = Card(11, "spades",'Ace of spades', 'Ace')
	Aceclubs = Card(11, "clubs",'Ace of clubs', 'Ace')
	deck = [hearts2,diamonds2,spades2,clubs2,hearts3,diamonds3,spades3,clubs3,hearts4,diamonds4,spades4,clubs4,hearts5,diamonds5,
	spades5,clubs5,hearts6,diamonds6,spades6,clubs6,hearts7,diamonds7,spades7,clubs7,hearts8,diamonds8,
	spades8,clubs8,hearts9,diamonds9,spades9,clubs9,hearts10,diamonds10,spades10,clubs10,Jackhearts,
	Jackdiamonds,Jackspades,Jackclubs,Queenhearts,Queendiamonds,Queenspades,Queenclubs,Kinghearts,
	Kingdiamonds,Kingspades,Kingclubs,Acehearts,Acediamonds,Acespades,Aceclubs]
	return deck

def keepPlaying(deposit):
	keepPlaying = input("Would you like to keep playing? ")
	if (keepPlaying == 'yes'):
		if (deposit == 0):
			deposit = input("How much would you like to deposit? ")
			deposit = int(deposit)
		print("Your total money is {}".format(deposit))
		play(deposit)
	elif (keepPlaying == 'no'):
		print("Thanks for playing!!")
		print("Your withdrawl is {}".format(deposit))
		return

def dealerPlay(dealerTotal, wager, deposit):
	while (dealerTotal <= 16):
		nextDealerCard = random.choice(deck)
		deck.remove(nextDealerCard)
		dealerTotal = dealerTotal + nextDealerCard.value
		print("The dealers next card was {} and the new total is {}".format(nextDealerCard.name, dealerTotal))
		if (dealerTotal > 21):
			print("Dealer busts, you Win!!")
			wager = int(wager) * 2
			deposit = deposit + (int(wager))
			print("Your total amount of money is now {}".format(deposit))
			keepPlaying(deposit)
	return dealerTotal

def ifCardIsAce(deposit, total, deck, numberOfCards):
	command = input("Would you like to stay or hit? ")
	if (numberOfCards == 2):
		totalWithAce = total - 10
	else:
		total = total + 10
		totalWithAce = total + 1
	while (command == 'hit'):
		newCard = random.choice(deck)
		deck.remove(newCard)
		totalWithAce = totalWithAce + newCard.value
		total = total + newCard.value
		print("Your card is {} and your new total is {} or {}".format(newCard.name, total, totalWithAce))
		if ((total > 21) and (totalWithAce > 21)):
			print ("Oops, you busted, the dealer wins")
			keepPlaying(deposit)
		else:
			command = input("Would you like to stay or hit? ")
	if ((total > 21) and (totalWithAce < 21)):
		return totalWithAce
	else:
		return total

def blackJack(deposit):
	print("You have Blackjack!!")
	wager = int(wager) * 2.5
	deposit = deposit + int(wager)
	print("Your total amount of money is now {}".format(deposit))
	keepPlaying(deposit)

def result(total, dealerTotal, deposit, wager):
	if (total > dealerTotal):
		print("You Win!!")
		deposit = (int(wager) * 2) + deposit
		print("Your new total is {}".format(deposit))
		keepPlaying(deposit)
	if (total == dealerTotal):
		print("It's a push")
		deposit = deposit + int(wager)
		keepPlaying(deposit)
	if ((total < dealerTotal) and (dealerTotal <= 21)):
		print("You lose, good luck next time")
		print("Your new total is {}".format(deposit))
		keepPlaying(deposit)


def play(deposit):
	total = 0
	dealerTotal = 0
	numberOfCards = 2
	if (int(deposit == 0)):
		deposit = input("How much would you like to deposit? ")
		deposit = int(deposit)
	deck = reloadCards()
	dealerCard1 = random.choice(deck)
	deck.remove(dealerCard1)
	playerCard1 = random.choice(deck)
	deck.remove(playerCard1)
	dealerCard2 = random.choice(deck)
	deck.remove(dealerCard2)
	playerCard2 = random.choice(deck)
	deck.remove(playerCard2)
	
	total = int(playerCard1.value) + int(playerCard2.value)
	wager = input("How much would you like to wager? ")
	while(int(wager) > deposit):
		print("Wager too big")
		wager = input("Please enter new wager ")
	deposit = deposit-(int(wager))
	if ((playerCard1.typeOfCard == 'Ace') or (playerCard2.typeOfCard == 'Ace')):
		if ((playerCard1.value == 10) or (playerCard2.value == 10)):
			blackJack(deposit)
		else:
			print("Your cards are {}, and {} and the total value is {} or {}".format(playerCard1.name, playerCard2.name, total, (total -10)))
			print('The dealer is showing {}'.format(dealerCard2.name))
			total = ifCardIsAce(deposit, total, deck)
			dealerTotal = dealerPlay(dealerTotal, wager, deposit)
			result(total, dealerTotal, deposit, wager)

	if (total != 21):
		if ((playerCard1.typeOfCard != 'Ace') and (playerCard2.typeOfCard != 'Ace')):
			print("Your cards are {}, and {} and the total value is {}".format(playerCard1.name, playerCard2.name, total))
			print('The dealer is showing {}'.format(dealerCard2.name))

		command = input('Would you like to stay or hit? ')
		while (command == 'hit'):
			newCard = random.choice(deck)
			deck.remove(newCard)
			numberOfCards = numberOfCards + 1
			if (newCard.typeOfCard == 'Ace'):
				total = ifCardIsAce(deposit, total, deck, numberOfCards)
			else:
				total = total + newCard.value
			print("Your card is {} and your new total is {}".format(newCard.name, total))
			if (total > 21):
				print ("Oops, you busted, the dealer wins")
				keepPlaying(deposit)
			else:
				command = input("Would you like to stay or hit? ")
		dealerTotal = dealerCard2.value+dealerCard1.value
		print("The dealers second card is {} giving a total of {}".format(dealerCard1.name, dealerTotal))
		while (dealerTotal <= 16):
			nextDealerCard = random.choice(deck)
			deck.remove(nextDealerCard)
			dealerTotal = dealerTotal + nextDealerCard.value
			print("The dealers next card was {} and the new total is {}".format(nextDealerCard.name, dealerTotal))
			if (dealerTotal > 21):
				print("Dealer busts, you Win!!")
				wager = int(wager) * 2
				deposit = deposit + (int(wager))
				print("Your total amount of money is now {}".format(deposit))
				keepPlaying(deposit)

		result(total, dealerTotal, deposit, wager)






play(0)




