'''
Main script for the game war. You will split the deck in 2. 
If a player wins they then get the cards and place them to the side.
If a tie then draw 3 and add to pile the forth card is flipped and checked for winner. Loop till winner
Once both players go through the original deck then shuffle cards that they won and return to playing until one player has no card
'''
import random
from random import randrange
class Kid_Math:
	"""CardClass - evalueate card and assign a numerical value"""
	def __init__(self,name):
		self.name = name
		#super(CardClass, self).__init__()
		pass
	
	def operator_choice(self,choice):
		global str_operator
		if (choice ==  1):
			str_operator = "adddition"
		elif(choice == 2):
			str_operator = "subtraction"
	
	def game_board(self,inum1,inum2,loop, max,i_type):
		print(f"Question {loop+1} of {max}")
		if(i_type == 1):
			ch_type = "+"
		elif(i_type == 2):
			ch_type = "-"
		else:
			print ("Error this type is not defined")
		print (f"  {inum1} \n {ch_type} {inum2}")
	
	def equation(self,inum1,inum2,guess,i_type):
		global i_result
		if (i_type == 1):
			i_result = inum1+inum2
		elif(i_type == 2):
			i_result = inum1-inum2
		else:
			print ("Error this type is not defined")
		if (i_result == guess):
			return 1
		else:
			return 0

	def __str__(self):
		return f"{self.name} is playing the math game!"
if __name__ == "__main__":
	'''This is the game of war greater card wins if a tie put 3 each in the pot and fight with the 4th card and repeate until there is a winner'''
	b_check = True
	b_char = "N"
	i_score = 0
	i_temp_score = 0
	i_result = 0
	i_temp = False
	i_type = 2
	str_operator =""
	while True:
		try:
			i_loop = int(input("Teacher, How many problembs do you want in each set?\n"))
			break
		except:
			print("Error that is not a number try again")
			continue
	while True:
		try:
			i_max = int(input("Teacher, What is the largest number you want in the equation?\n"))
			break
		except:
			print("Error that is not a number try again")
			continue
	while True:
		try:
			i_type = int(input("What type of equations do you want? 1 - add 2- subtract"))
			break
		except:
			print("Error that was not a nunber!!")
			continue		
	i_total = i_loop
	game = Kid_Math(input("Student, What is your name?\n"))
	game.operator_choice(i_type)
	print (f"We are going to do {i_total} {str_operator} problems!!")
	print(game)
	while b_check:
		for i in range (i_loop):
			i_result = 0
			num1 = random.randrange(1,i_max)
			num2 = random.randrange (0,num1)
			game.game_board(num1,num2,i,i_loop,i_type)
			while True:
				try:
					i_guess = int(input("______\n  "))
					break
				except:
					print("Error that is not a number try again")
					game.game_board(num1,num2,i,i_loop,i_type)
					continue
			i_temp = game.equation(num1,num2,i_guess,i_type)
			if i_temp:
				print("Correct")
			else:
				print (f"Error the correct answer was {i_result}")
			i_score += i_temp
			i_temp_score +=i_temp
		print (f"Good Jobe you got {i_temp_score}/{i_loop} correct")
		b_char = input(f"{i_loop} problems are now complete do you wish to continue y/n?")
		if b_char.upper() == "Y":
			b_check = True
			i_temp_score = 0
			i_total += i_loop
		else:
			b_check	= False
	print (f"You got {i_score}/{i_total} right")
	print (f"Thank you for playing {game.name} exiting game now!")
