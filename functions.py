import pygame
from pygame.locals import * 
import random


class Support:
	""""Create a structure" class"""
	def __init__(self):
		self.structure = 0


	def  create(self):

		""""function to create the struct"""

		with open('structures.txt', "r") as fichier:
			support_n = []
			for row in fichier:  # w walk through each row of a structure
	 			row_n = []
	 			for sprite in row: #  walk through each element of row of structure
	 				if sprite != '\n':
	 					row_n.append(sprite) #stock element of row in a list
 				support_n.append(row_n) #stock row of element in a list for giving a array 2D
 			#We save a structure
			self.structure = support_n


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
				x = num_case * tail_sprite
				y = num_row * tail_sprite
				if sprite == '1':		   #w = Wall(built Wall)
					opening.blit(pygame.transform.scale(wall,(30, 30)),(x,y))
				
				elif sprite == 'g':		   #g = goal(built goal)
					opening.blit(pygame.transform.scale(goal,(30, 30)), (x,y))
		
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

			
			self.case_x = random.randint(0,14) # generate randomly a number
			self.case_y = random.randint(0,14) #generate randomly a number
			position_create = self.home.structure[self.case_x][self.case_y] #value to know if we have a wall or no
		
			if position_create == '0' :
				self.y = self.case_y * 30  # We define/accept the position for the object
				self.x = self.case_x * 30
				self.possible = False  # We construct the element once 
				


	

class Maestro:
	""""Create Mac Gyver class to define his attributs and his methods"""
		
	def __init__(self,home):	#constructor class

		self.direct = pygame.transform.scale((pygame.image.load('MacGyver.png').convert()),(30,30))

		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		self.home = home
		#self.e = e
		self.cpt = 0
		
		
	
		

	def move(self,directory):
		""""Create Mac Gyver method to permit Mac Gyver to moving"""

		tail_sprite = 30
		nombre_sprite_cote = 15

		#move to right
		if directory == 'right':
			#For don't go out
			if self.case_x < (nombre_sprite_cote - 1):
				#We verify if they don't have Wall
				if self.home.structure[self.case_y][self.case_x+1] != '1':
					#move to one hut
					self.case_x += 1
					#Calculate real position Mac Gyver position
					self.x = self.case_x * tail_sprite
			

		#move to left
		if directory == 'left':
			if self.case_x > 0:
				if self.home.structure[self.case_y][self.case_x-1] != '1':
					self.case_x -= 1
					self.x = self.case_x * tail_sprite
			
		
		#move to top
		if directory == 'top':
			if self.case_y > 0:
				if self.home.structure[self.case_y-1][self.case_x] != '1':
					self.case_y -= 1
					self.y = self.case_y * tail_sprite
			
		#move to low
		if directory == 'low':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.home.structure[self.case_y+1][self.case_x] != '1':
					self.case_y += 1
					self.y = self.case_y * tail_sprite

	

