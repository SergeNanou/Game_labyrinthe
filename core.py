#####Central program


import pygame
from pygame.locals import *
from functions import *
pygame.init()

#Opening of pygame Window

opening = pygame.display.set_mode((450, 450))
# Title and icone of opening

pygame.display.set_caption("Mac Gyver release !")
title_image = pygame.image.load("MacGyver.png").convert_alpha()
pygame.display.set_icon(title_image)
decoratePNG = pygame.image.load("decorations.png").convert_alpha()
#background image
background = pygame.image.load("ciel-bleu.jpg").convert() 

#Mac Gyver element import
etherPNG = pygame.image.load('ether.png').convert()
seringuePNG = pygame.image.load('seringue.png').convert()
aiguillePNG = pygame.image.load('aiguille.png').convert()

#Instance of support

home = Support()
home.create()

#####Instantiate test variables

etherTest = True
seringueTest = True
aiguilleTest = True 
cpt = 0
loser = False
win = True
##Instance and generate the elements that permit to Mac Gyver to kill the garden of exit

ether = Element(home, etherPNG)
ether.generate(etherPNG,opening)
seringue = Element(home, seringuePNG)
seringue.generate(seringuePNG, opening)
aiguille = Element(home, aiguillePNG)
aiguille.generate(aiguillePNG, opening)


#Creation de Mac Gyver
Mac_Gyver = Maestro(home)
continue_game = 1 

#BOUCLE INFINIE
#continuer = False
continuer_open = True
#continue_intro = False
#intro = True
#jouer = True
while continuer_open:
	continuer_intro = True
	
	while continuer_intro:

		rectScreen = opening.get_rect()
			#police = pygame.font.Font("led.ttf",72)
		police = pygame.font.Font(None,10)
		texte = police.render("THIS GAME CONSISTE TO PERMIT MAC GYVER TO TAKE ANY ELEMENT TO KILL A GARDEN IN A LABYRINTH",True,pygame.Color("#FFFF00"))
		rectTexte = texte.get_rect()
		rectTexte.center = rectScreen.center
		opening.fill(pygame.Color("#FF0000"))
		opening.blit(texte,rectTexte)

		pygame.display.flip()
		
		for event in pygame.event.get(): #function to catch a user action
				
					
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_open = False
				continuer_intro = False
				continuer = False
				
				
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1
				if event.key == K_0:
					continuer_intro = False	#On quitte l'accueil
					continuer = True
	
					
			
	while continuer:


		for event in pygame.event.get(): #function to catch a user action	

			if event.type == KEYDOWN: # catch a keyboard action
					                  
			
						
				#Keys movement of Mac Gyver
				if event.key == K_RIGHT:
					Mac_Gyver.move('right')
					
				if event.key == K_LEFT:
					Mac_Gyver.move('left')
					
				if event.key == K_UP:
					Mac_Gyver.move('top')
					
				if event.key == K_DOWN:
					Mac_Gyver.move('low')
						
				elif event.key == K_ESCAPE:# quit the opening
						continuer = False
					
				
	#Construct a labyrinth

		
	opening.blit((pygame.transform.scale(background, (450, 450))), (0, 0))
	home.poster(opening)

	opening.blit(Mac_Gyver.direct, (Mac_Gyver.x, Mac_Gyver.y)) # post Mac gyver and playing

	# Unit Test to permit at Mac Gyver  to catch element for his liberty

	if etherTest:
		opening.blit((pygame.transform.scale(etherPNG, (30, 30))), (ether.x, ether.y))
	if (Mac_Gyver.x, Mac_Gyver.y) == (ether.x, ether.y):
		etherTest = False
		opening.blit((pygame.transform.scale(etherPNG, (30, 30))), (60, 40))
		

	if seringueTest:
		opening.blit((pygame.transform.scale(seringuePNG, (30, 30))), (seringue.x, seringue.y))
	if (Mac_Gyver.x, Mac_Gyver.y) == (seringue.x, seringue.y):
		seringueTest = False
		opening.blit((pygame.transform.scale(seringuePNG, (30, 30))), (30, 16))
		

	if aiguilleTest:
		opening.blit((pygame.transform.scale(aiguillePNG, (30, 30))), (aiguille.x, aiguille.y))
	if (Mac_Gyver.x, Mac_Gyver.y) == (aiguille.x, aiguille.y):
		aiguilleTest = False
		opening.blit((pygame.transform.scale(aiguillePNG, (30, 30))), (50, 17))
		

	# Mac Gyver take any elements
	if etherTest==False and seringueTest==False and aiguilleTest==False:
		cpt +=1
	if cpt== 0 and home.structure[Mac_Gyver.case_y][Mac_Gyver.case_x] == 'g':

		loser = True
	if loser:
		rectScreen = opening.get_rect()
		#police = pygame.font.Font("led.ttf",72)
		police = pygame.font.Font(None,30)
		texte = police.render("Game Over -ECHAP TO QUIT",True,pygame.Color("#FFFF00"))
		rectTexte = texte.get_rect()
		rectTexte.center = rectScreen.center
		opening.fill(pygame.Color("#FF0000"))
		opening.blit(texte,rectTexte)

		pygame.display.flip()






