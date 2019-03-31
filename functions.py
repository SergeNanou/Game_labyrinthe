import pygame
from pygame.locals import * 

import random


class Support:
	""""Create a structure" class"""
	def __init__(self):
		self.structure = 0
		

	def  create(self):
      
		""""Create a maze with a exhaustive exploration """

		#xMax = 7 # number of boxes  not walled 
		taille_Max = 7 # number of boxes not walled

		move_X = {'N':0,'S':0,'E':1,'O':-1} #  direction we take to break a wall in width
		move_Y = {'N':1,'S':-1,'E':0,'O':0} # diretion we take to break a wall in height

		# we create a matrix to stock if the state of cell of  maze  (visited or not)(0 and 1)
		# we init all values at 0
		# dejavu = []
		# for y in range(taille_Max):
		# 	for x in range(taille_Max):
		# 		dejavu[y][x] = 0

		dejavu = [[0 for x in range(taille_Max)] for y in range(taille_Max)]

		#we create a labyrinth with a wall enter the boxes of maze(the goal is to break this wall 
		#to unite all the boxes of the maze)

		# we init the all values of mare at zero
		laby = [[0 for x in range(2*taille_Max+1)] for y in range(2*taille_Max+1)]

		#we put a boxes  of maze enter the wall symbolizing  by 1 = boxes and 0 = walls in matrix maze

		for y in range(len(laby)-1):             #we  traverse each row of matrix maze
			for x in range(len(laby[y])-1):       #we traverse each cells of row
				if x % 2 != 0 and y % 2 != 0:
					laby[y][x] = 1

    	# we choice in random one cell in dejavu matrix   for begining the union of maze cell

		randCell = ((random.randrange(taille_Max)), (random.randrange(taille_Max)))
		lastCell = [(randCell)]

		#we make a while loop to visit all boxes of maze for the union.
		while lastCell != []:
			(x, y) = lastCell[-1] # we take the last element of the pile
			dejavu[y][x] = 1 
			lNeighboors = []
			for move in ['N','S','O','E']:
				x_1 = x + move_X[move] #the width of the cell we use to make a union
				y_1 = y + move_Y[move] #the height of the cell we use to make a union


				if x_1 >= 0 and x_1 < taille_Max and y_1 >= 0 and y_1 < taille_Max:
					
					if dejavu[y_1][x_1] == 0: #we check if a boxe are not visited 

						lNeighboors.append(move)


			if len(lNeighboors) > 0:
				var = random.choice(lNeighboors) # we choice randomly a neighboors boxe to make a union 

	            #In the maze this position are((2x+1,2y+1),(2x_1+1,2y_1+1), middle of the two cells(wall) = (x +x_1+1,y,y_1+1),
	            #the method is to break this wall to unit the two boxes of maze
				laby[x+x+move_X[var]+1][y+y+move_Y[var]+1] = 1
	            # we udpate the position of boxes to continue the maze boxes union
				x, y = x + move_X[var], y + move_Y[var]	

				lastCell.append((x, y))
			else:
				lastCell.pop()
		laby[1][1] = 2
		laby[2*taille_Max-1][2*taille_Max-1] = 3
		self.structure = laby




		# """"function to create the struct"""

		# with open('structures.txt', "r") as fichier:
		# 	support_n = []
		# 	for row in fichier:  # w walk through each row of a structure
	 # 			row_n = []
	 # 			for sprite in row: #  walk through each element of row of structure
	 # 				if sprite != '\n':
	 # 					row_n.append(sprite) #stock element of row in a list
 	# 			support_n.append(row_n) #stock row of element in a list for giving a array 2D
 	# 		#We save a structure
		# #self.structure = support_n



	def poster(self, opening):

		""""function to post the struct"""

		wall = pygame.image.load('floor-tiles-20x20.png').convert()#import a Wall Image
		goal = pygame.image.load('Gardien.png').convert() # import Garden goal Image
		tail_sprite = 30
		#we walk through each line of a structure
		num_row = 0
		for row in self.structure:
		#we walk through each element of row
			num_case = 0
			for sprite in row:
			#we calcul the elemnent tail in pixels
				#begin = []
				x = num_case * tail_sprite
				y = num_row * tail_sprite
				if sprite == 0:		   #w = Wall(built Wall)
					opening.blit(pygame.transform.scale(wall,(30, 30)),(x,y))
				
				elif sprite == 3:		   #g = goal(built goal)
					opening.blit(pygame.transform.scale(goal,(30, 30)), (x,y))
				#elif sprite == 2:		   #g = goal(built goal)
					#opening.blit(pygame.transform.scale((pygame.image.load('MacGyver.png').convert()),(30, 30)), (x,y))
				num_case += 1
			num_row += 1
			

class Element:	
	""""Create a element clas for kill a garden """

	def __init__(self,home,image): #constructor of Element class
		self.home = home
		self.image = image
		self.x = 0
		self.y = 0
		
		sprite_dim = 30
		self.possible = True
		
		
	def generate(self,image,home):
		""""Create a methode  to generate this element """
		
		while self.possible:

			
			self.case_x = random.randint(0,9) # generate randomly a number
			self.case_y = random.randint(0,9) #generate randomly a number
			position_create = self.home.structure[self.case_y][self.case_x] #value to know if we have a wall or no
		
			if position_create == 1:
				self.y = self.case_y * 30  # We define/accept the position for the object
				self.x = self.case_x * 30
				self.possible = False  # We construct the element once 
				


	

class Maestro:
	""""Create Mac Gyver class to define his attributs and his methods"""
		
	def __init__(self,home):	#constructor class

		
		self.case_x = 1
		self.case_y = 1
		self.x = 30
		self.y = 30
		self.home = home
		#self.e = e
		#self.cpt = 0
		self.direct = pygame.transform.scale((pygame.image.load('MacGyver.png').convert()),(30, 30))
		#self.directory = self.direct
		#self.direct = self.home.indic #pygame.transform.scale((pygame.image.load('MacGyver.png').convert()),(30,30))

	
		

	def move(self,directory):
		""""Create Mac Gyver method to permit Mac Gyver to moving"""

		tail_sprite = 30
		nombre_sprite_cote = 15
		
		

		#move to right
		if directory == 'right':
			#For don't go out
			if self.case_x < (nombre_sprite_cote - 1):
				#We verify if they don't have Wall
				if self.home.structure[self.case_y][self.case_x+1] != 0:
					#move to one hut
					self.case_x += 1
					#Calculate real position Mac Gyver position
					self.x = self.case_x * tail_sprite
			#self.directory = sdirect
		#move to left
		if directory == 'left':
			if self.case_x > 0:
				if self.home.structure[self.case_y][self.case_x-1] != 0:
					self.case_x -= 1
					self.x = self.case_x * tail_sprite
			#self.directory = pygame.transform.scale((pygame.image.load('MacGyver.png').convert()),(30, 30))
		
		#move to top
		if directory == 'top':
			if self.case_y > 0:
				if self.home.structure[self.case_y-1][self.case_x] != 0:
					self.case_y -= 1
					self.y = self.case_y * tail_sprite
			#self.directory = self.direct
		#move to low
		if directory == 'low':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.home.structure[self.case_y+1][self.case_x] != 0:
					self.case_y += 1
					self.y = self.case_y * tail_sprite
			#self.directory = pygame.transform.scale((pygame.image.load('MacGyver.png').convert()),(30, 30))

	

