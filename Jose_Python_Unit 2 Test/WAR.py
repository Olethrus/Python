'''
Main script for the game war. You will split the deck in 2. 
If a player wins they then get the cards and place them to the side.
If a tie then draw 3 and add to pile the forth card is flipped and checked for winner. Loop until the war is a winner
In the event one or both players do not have enough card to discard the discard amount will be reduced to play out the war
If this is not desired change the logic setting an i_max and declare the winner from there
Once both players go through the original deck then shuffle cards that they won and return to playing until one player has no card
'''
import random
from random import shuffle

t_suits = ("Hearts", "Diamonds", "Spades", "Clubs")
t_ranks = ("Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King")
d_values = {"Two":2,"Three":3,"Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13,"Ace":14}
i_draw = 26
i_turncount = 0

class CardClass:
	"""CardClass - evalueate card and assign a numerical value"""
	def __init__(self, str_suit, str_rank):
		try:
			self.str_suit = str(str_suit) # heart,club, etc
			self.str_rank = (str(str_rank)).capitalize()# numerical or word 7,8,9,J,Q,K, etc
			self.value = d_values[self.str_rank] # Value of card to be used in determining winner of war
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

	def play_card(self):
		"""This will play the top card of a players deck"""
		return self.playercards.pop(0)
	def receive_card(self,game_cards):
		"""This will update a players deck and receive cards in the form of a single card or a list"""
		if (type(game_cards) == type([])):
			self.playercards.extend(game_cards)
		else:
			self.playercards.append(game_cards)
	def shuffle (self):
		"""This will shuffle the full deck"""
		random.shuffle(self.playercards)
	def __len__(self):
		return len(self.playercards)
	def __str__(self):
		return (f"{self.name} has {len(self.playercards)} cards")
class GameLogic:
	"""This will determine who won the round/game """
	def __init__(self):
		pass
	def game_board(self,player_1,player_2):
		"""Display current game board"""
		#print ("\n"*50) used to clear the screen after every round if desired
		print (f"Player 1({player_1.name}) : {player_1.playercards[0].str_rank} of {player_1.playercards[0].str_suit}")
		print (f"Player 2({player_2.name}) : {player_2.playercards[0].str_rank} of {player_2.playercards[0].str_suit}")
	def war(self,player_1,player_2):
		self.game_board(player_1,player_2)
		i = 0
		i_max = 0
		if (len(player_1) > len(player_2)):
			i_max = len(player_2) - 1
		else:
			i_max = len(player_1) - 1
		while True:
			if (i == i_max):
				break
			elif (player_1.playercards[i].value == player_2.playercards[i].value):
				i += 4
				print ("WAR! Game is a tie add 3 cards to the pot and play another card!")
				self.game_board(player_1,player_2)
				if (i > i_max):
					i = i_max
				continue
			else:
				break
		print(f"{i+1} were lost in this war!")
		if (player_1.playercards[i].value > player_2.playercards[i].value):
			print (f"Player 1({player_1.name}) wins this round")
			return [1,i]
		elif (player_2.playercards[i].value > player_1.playercards[i].value):
			print (f"Player 2({player_2.name}) wins this round")
			return [2,i]
		else:
			print ("There was no winner this round reshuffle decks and try again!")
			return 999				
	def game_check(self,player_1,player_2):
		'''Check if the game needs to continue'''		
		if (len(player_1) == 0):
			return "Player 2 is the winner!!"
		elif (len(player_2) == 0):
			return "Player 1 is the winner!!"
		else:	
			return "True"
if __name__ == "__main__":
	'''This is the game of war greater card wins if a tie put 3 each in the pot and fight with the 4th card and repeate until there is a winner'''
	fulldeck = DeckClass()
	fulldeck.shuffle()
	game = GameLogic() # used for game logic determining if their is a winner and updating the pot list
	game_result = "True"
	card_pot = []
	round_count = 0
	round_result = [0,999] # used to determine how many cards of each player gets added to the list player,cards
	player_1 = PlayerClass(input ("What is your name player 1?"))
	player_2 = PlayerClass(input ("What is your name player 2?"))
	for i in range(i_draw):
		player_1.receive_card(fulldeck.deal()) 
		player_2.receive_card(fulldeck.deal())
	while game_result == "True":
		print (f"Round {round_count} start!")
		round_result = game.war(player_1,player_2)
		# place the cards in the pot based on card count
		for i in range(round_result[1]+1):
			card_pot.append(player_1.play_card())
			card_pot.append(player_2.play_card())
		# Update players deck and clear out card pot
		if (round_result[0] == 1):
			player_1.receive_card(card_pot)
		elif (round_result[0] == 2):
			player_2.receive_card(card_pot)
		elif (round_result[0] == 999):
			player_1.shuffle()
			player_2.shuffle()
		game_result = (game.game_check(player_1,player_2))
		card_pot = []
		round_count +=1
		# for a long game break out and call a draw since no side won the war
		if round_count > 2000:
			break
	print ("This war was a draw game over!")
	if game_result != "True":
		print (game_result)
	print ("The game is done exiting program")		
