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
d_values = {"Two":2,"Three":3,"Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10,"Ace":11}
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
	def create(self):
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
		self.bank = 10000
		self.hand_total = 0
		self.ace_count = 0
		self.soft_hand = False	 	
	def receive_card(self,game_cards):
		"""This will update a players deck and receive cards in the form of a single card or a list"""
		self.playercards.append(game_cards)
	def withdraw (self,amount):
		""""""
		self.bank -= amount
	def bet(self,amount,min_bet):
		while True:
			try:
				amount = float(amount)
				if (amount > self.bank):
					amount = self.bank
				elif (amount <= min_bet):
					print("Minimum bet is $5 raising bet to $5")
					amount = 5.0
				self.bank -=amount
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
	def game_board(self):
		"""Display current game board"""
		global npc
		global dealer
		global player_1
		global bet
		print ("\n"*50)
		if  npc:
			print (f"Player 1 : bet - {bet} hand_total - {player_1.hand_total}")
			for i in range (len(player_1)):
				print (f"Card {i} : {player_1.playercards[i].str_rank} of {player_1.playercards[i].str_suit}")
			print(f"Dealer: hand_total - {dealer.hand_total}")
			for i in range (len(dealer)):
				print (f"{dealer.playercards[i].str_rank} of {dealer.playercards[i].str_suit}")		
		else:
			print (f"Player 1 : bet - {bet} hand_total - {player_1.hand_total}")
			for i in range (len(player_1)):
				print (f"Card {i} : {player_1.playercards[i].str_rank} of {player_1.playercards[i].str_suit}")
			try:	
				print(f"Dealer:\n Card 1: {dealer.playercards[1].str_rank} of {dealer.playercards[1].str_suit}")
			except:
				pass
	def next_turn(self,game_deck):
		global npc
		global npc
		global dealer
		global player_1
		if len(gamedeck) < 52:
			self.game_board()
		if npc:
			if dealer.hand_total < 17:
				dealer.receive_card(game_deck.deal())
			else:
				return False
		elif (len(player_1) < 2 or len(dealer) < 2):
			player_1.receive_card(game_deck.deal())
			dealer.receive_card(game_deck.deal())
		else:
			s_hit =(input (f"Your total hand value is {player_1.hand_total} \nDo you want to hit?"))
			if (s_hit.upper() == "Y" or s_hit.upper() == "YES"):
				player_1.receive_card(game_deck.deal())
			else:
				npc = True
	def hand_amount(self):
		global dealer
		global player_1
		global npc
		if npc:
			dealer.hand_total = 0
			for i in range (len(dealer)):
				dealer.hand_total += dealer.playercards[i].value
				print (f"Card {i} : {dealer.playercards[i].str_rank} of {dealer.playercards[i].str_suit} - value {dealer.playercards[i].value}")
		if not npc:
			player_1.hand_total = 0
			for i in range (len(player_1)):
				player_1.hand_total += player_1.playercards[i].value
				print (f"Card {i} : {player_1.playercards[i].str_rank} of {player_1.playercards[i].str_suit} - value {player_1.playercards[i].value}")
		if dealer.ace_count > 0:
			dealer.soft_hand = True
		if (dealer.hand_total > 21 and dealer.ace_count > 0):
			dealer.ace_count -= 1
			dealer.hand_total -=10
		if (player_1.hand_total > 21 and dealer.ace_count > 0):
			player_1.ace_count -= 1
			player_1.hand_total -=10	
	def game_check(self):
		global player_1
		global dealer
		global npc
		if (player_1.hand_total == 21 and dealer.hand_total == 21):
			return "Push"
		elif player_1.hand_total > 21:
			return "Dealer"
		elif dealer.hand_total > 21:
			return "Player 1"
		elif (dealer.hand_total >= 17 and dealer.hand_total > player_1.hand_total and npc):
			return "Dealer"
		elif (dealer.hand_total >= 17 and dealer.hand_total < player_1.hand_total and npc):
			return "Player 1"
		else: 
			return False
	def setup(self):
		global game
		global player_1
		global dealer
		global bet
		global result
		result = ""
		game.pot = 0
		player_1.hand_total = 0
		dealer.hand_total = 0
		player_1.playercards = []
		dealer.playercards = []
		player_1.ace_count = 0
		dealer.ace_count = 0
		game.pot = bet*2

if __name__ == "__main__":
	'''This is the game of war greater card wins if a tie put 3 each in the pot and fight with the 4th card and repeat until there is a winner'''
	gamedeck = DeckClass ()
	game = GameLogic() # used for game logic determining if their is a winner and updating the pot list
	round_count = 1 
	npc = False # this is to determine if it is the npc (computer player) or human players turn 1 = computer
	dealer = PlayerClass("dealer")
	player_1 = PlayerClass(input ("What is your name player 1?"))
	b_continue = True
	min_bet = 5.0
	while True:
		gamedeck.cards = []
		gamedeck.create()
		gamedeck.shuffle()
		print (f" Game deck size: {len(gamedeck)}")
		if player_1.bank < min_bet:
			print (f"You are out of funds to continue the minimum bet is ${min_bet}")
			break
		print(f"Player 1 ({player_1.name})your bank account is ${player_1.bank}")
		t_bet = input("How much would you like to bet on this hand?")
		bet = player_1.bet(t_bet,min_bet)
		game.setup()
		b_continue = False
		while True:
			b_continue = game.next_turn(gamedeck)
			game.hand_amount()
			result = game.game_check()
			if result == "Push":
				player_1.deposit(bet)
				print ("This round is a push!")
				break	
			if npc:
				if result == "Dealer":
					print (f"Dealer has won this round you lost ${bet}")
					break
				elif result == "Player 1":
					print (f"You won this round you receive ${game.pot}")
					player_1.deposit(game.pot)
					break
			else:
				if result == "Dealer":
					print (f"BUST! you lost ${bet}")
					break
			if b_continue:
				break
		round_count +=1
	print ("The game is done exiting program")		
# Put scenario to add new deck to back of current deck like cards < 10 create new deck and shuffle
# Check if the logic with As will decrease hand size
# Check if cards total correctly
# Check if game is 21 is correct
# Make sure cards output dealer hand and player hand each round correctly
# Add in double down and split logic to game after above is correct