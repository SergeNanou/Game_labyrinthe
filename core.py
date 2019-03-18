import pygame
from pygame.locals import *
from functions import *
pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((450, 450))
fond = pygame.image.load("ciel-bleu.jpg").convert()

fenetre.blit((pygame.transform.scale(fond, (450, 450))), (0, 0))
#Rafraîchissement de l'écran
Struc = Structure()
Struc.create()
Struc.poster(fenetre)




pygame.display.flip()
#BOUCLE INFINIE
continuer = 1
while continuer:
	continue