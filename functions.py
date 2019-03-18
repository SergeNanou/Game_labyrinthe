import pygame
from pygame.locals import * 

class Structure:
	"""Classe permettant de créer une structure"""
	def __init__(self):
		self.structure = 0


	def  create(self):

		with open('structures.txt', "r") as fichier:
			structure_n = []
			for ligne in fichier:
	 			ligne_n = []
	 			for sprite in ligne:
	 				if sprite != '\n':
	 					ligne_n.append(sprite)
 				structure_n.append(ligne_n)
 			#On sauvegarde cette structure
			self.structure = structure_n


	def poster(self, fenetre):

		mur = pygame.image.load('floor-tiles-20x20.png').convert()
		depart = pygame.image.load('MacGyver.png').convert()
		arrivee = pygame.image.load('Gardien.png').convert()
		tail_sprite = 30
		#On parcourt la liste du niveau
		num_row = 0
		for row in self.structure:
		#On parcourt les listes de lignes
			num_case = 0
			for sprite in row:
			#On calcule la position réelle en pixels
				x = num_case * tail_sprite
				y = num_row * tail_sprite
				if sprite == '1':		   #m = Mur
					fenetre.blit(pygame.transform.scale(mur,(30, 30)),(x,y))
				elif sprite == 'd':		   #d = Départ
					fenetre.blit(pygame.transform.scale(depart,(30, 30)), (x,y))
				elif sprite == 'g':		   #a = Arrivée
					fenetre.blit(pygame.transform.scale(arrivee,(30, 30)), (x,y))
		
				num_case += 1
			num_row += 1	
		
		