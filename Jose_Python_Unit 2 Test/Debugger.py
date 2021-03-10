"""
Main script for the game of black jack
Main script for the game war. You will split the deck in 2. 
If a player wins they then get the cards and place them to the side.
If a tie then draw 3 and add to pile the forth card is flipped and checked for winner. Loop until the war is a winner
In the event one or both players do not have enough card to discard the discard amount will be reduced to play out the war
If this is not desired change the logic setting an i_max and declare the winner from there
Once both players go through the original deck then shuffle cards that they won and return to playing until one player has no cardA's will favor your hand ex if over 21 reduce all A's to 1 
Double Down ability to double your bet
Split will split the cards and you will be running two hands
The player will start with $2000 and the number will be displayed with the proper ',' and '.'
"""
import random
from random import shuffle

t_suits = ("Hearts", "Diamonds", "Spades", "Clubs")
t_ranks = ("Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King")
d_values = {"Two":2,"Three":3,"Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":12,"Ace":11}
i_turncount = 0

class CardClass:
	"""CardClass - evaluate card and assign a numerical value"""
	def __init__(self, str_suit, str_rank):
		try:
			self.str_suit = str(str_suit) # heart,club, etc
			self.str_rank = (str(str_rank)).capitalize()# numerical or word 7,8,9,J,Q,K, etc
			self.value = d_values[self.str_rank] # Value of card to be used in determining hand total
		except:
			print("There was an error determining the CardClass check supplied input")
	def __str__(self):
		return f"{self.str_rank} of {self.str_suit}"
class  DeckClass:
	"""DeckClass - Create all 52 cards"""
	def __init__(self):
		global t_suits
		global t_ranks
		self.cards = []
		# Loop through the suits and rank to create a deck
		for i in t_suits:
			for j in t_ranks:
				created_card = CardClass(i,j)
				self.cards.append(created_card)
	def __len__(self):
		return len(self.cards)
	def shuffle (self):
		"""This will shuffle the full deck"""
		random.shuffle(self.cards)
	def deal(self):
		"""This will remove the card that is dealt to the player from the deck"""
		return self.cards.pop()
class PlayerClass:
	"""This is the player class it will have a play and receive card function to pass the pot to the winner"""
	def __init__(self, name):
		self.name = name
		self.playercards = []
		self.bank = 10000.00
		self.hand_total = 0		 	
	def receive_card(self,game_cards):
		"""This will update a players deck and receive cards in the form of a single card or a list"""
		self.playercards.append(game_cards)
	def withdraw (self,amount):
		""""""
		self.bank -= amount
	def bet(self,amount):
		while True:
			try:
				amount = float(amount)
				if (amount > self.bank):
					amount = self.bank
				elif (amount <= 1):
					print("Minimum bet is $5 raising bet to $5")
					amount = 5.0
				self.bank -=amount
				print (self.bank)
				return amount
			except:
				amount = input("Error that amount was invalid try again!\n")
	def deposit (self,amount):
		self.bank += amount
	def __len__(self):
		return len(self.playercards)
	def __str__(self):
		return (f"{self.name} has ${self.bank} left")

class GameLogic:
	"""This will determine who won the round/game """
	def __init__(self):
		self.pot = 0
	def game_board(self,dealer,player_1):
		"""Display current game board"""
		global npc
		#print ("\n"*50)
		print(f"Player 1 bank : ${player_1.bank} Current bet: ${self.pot/2}")
		if  npc:
			print ("Player 1 :")
			for i in range (len(player_1)):
				print (f"Card {i} : {player_1.playercards[i].str_rank} of {player_1.playercards[i].str_suit}")
			print("Dealer:")
			for i in range (len(dealer)):
				print (f"{dealer.playercards[i].str_rank} of {dealer.playercards[i].str_suit}")		
		else:
			print ("Player 1 :")
			for i in range (len(player_1)):
				print (f"Card {i} : {player_1.playercards[i].str_rank} of {player_1.playercards[i].str_suit}")		
			print(f"Dealer:\n Card 1: {dealer.playercards[1].str_rank} of {dealer.playercards[1].str_suit}")
	def next_turn(self,dealer,player_1,game_deck):
		self.game_board(dealer,player_1)
		global npc
		if npc:
			if dealer.hand_total < 13:
				dealer.receive_card(game_deck.deal())
			else:
				return True
		else:
			s_hit =(input (f"Your total hand value is {player_1.hand_total} \nDo you want to hit?"))
			if (s_hit.upper() == "Y" or s_hit.upper() == "YES"):
				player_1.receive_card(game_deck.deal())
			else:
				npc = True
	def hand_amount(self,player):
		print (f"Hand total - {player.hand_total}")

		total = player.hand_total + player.playercards[0].value 
		return total
	def game_check(self,player_1,dealer):
		if player_1.hand_total > 21:
			return "Dealer"
		elif (dealer.hand_total > 13 and dealer.hand_total > player_1.hand_total):
			return "Dealer"
		elif (dealer.hand_total > 13 and dealer.hand_total < player_1.hand_total):
			return "Player 1"
		else: 
			return False

if __name__ == "__main__":
	bet = 0
	game = GameLogic()
	game_deck = DeckClass()
	player_1 = PlayerClass("Player 1")
	player_1.receive_card(game_deck.deal())
	print (f" Card 0 - {player_1.playercards[0].value} - {player_1.playercards[0].str_rank} of {player_1.playercards[0].str_suit}")
	result= game.hand_amount(player_1)
	print(result)
	print (f"Player 1 hand total {player_1.hand_total}")
	player_1.receive_card(game_deck.deal())
	print (f" Card 0 - {player_1.playercards[1].value} - {player_1.playercards[1].str_rank} of {player_1.playercards[1].str_suit}")
	print(f" Card 1 - {player_1.playercards[0].value} - {player_1.playercards[0].str_rank} of {player_1.playercards[0].str_suit}")
	result= game.hand_amount(player_1)
	print(result)
	print(player_1.bank)
	t_bet = input("How much would you like to bet on this hand?")
	bet = player_1.bet(t_bet)
	game.pot = bet*2
	print(player_1.bank)