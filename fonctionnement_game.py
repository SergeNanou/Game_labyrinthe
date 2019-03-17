import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((450, 450))
fond = pygame.image.load("ciel-bleu.jpg").convert()

fenetre.blit((pygame.transform.scale(fond, (450, 450))), (0, 0))
#Rafraîchissement de l'écran

mur = pygame.image.load('floor-tiles-20x20.png').convert()
depart = pygame.image.load('MacGyver.png').convert()
arrivee = pygame.image.load('Gardien.png').convert()



with open('structures.txt', "r") as fichier:
	structure_niveau = []
	for ligne in fichier:
	 	ligne_niveau = []
	 	for sprite in ligne:
	 		if sprite != '\n':
	 			ligne_niveau.append(sprite)
 		structure_niveau.append(ligne_niveau)	
		
	print(structure_niveau)
		
    
taille_sprite = 30
#On parcourt la liste du niveau
num_ligne = 0
for ligne in structure_niveau:
		#On parcourt les listes de lignes
	num_case = 0
	for sprite in ligne:
		#On calcule la position réelle en pixels
		x = num_case * taille_sprite
		y = num_ligne * taille_sprite
		if sprite == '1':		   #m = Mur
			fenetre.blit(pygame.transform.scale(mur,(30, 30)),(x,y))
		elif sprite == 'd':		   #d = Départ
			fenetre.blit(pygame.transform.scale(depart,(30, 30)), (x,y))
		elif sprite == 'g':		   #a = Arrivée
			fenetre.blit(pygame.transform.scale(arrivee,(30, 30)), (x,y))
		
		num_case += 1
	num_ligne += 1
pygame.display.flip()
#BOUCLE INFINIE
continuer = 1
while continuer:
	continue