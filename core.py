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
seringuePNG = pygame.image.load('seingue_2.png').convert()
aiguillePNG = pygame.image.load('aiguille.png').convert()
tubePNG = pygame.image.load('tube_plastique.png').convert()
image_acceilPNG =  pygame.image.load('acceuil_3.png').convert()
gainPNG = pygame.image.load('Gain.png').convert()
#goal = pygame.image.load('Gardien.png').convert()
#image

#Instance of support

home = Support()
home.create()

tail_sprite = 30
#we walk through each line of a structure

				
#####Instantiate test variables
acceuilTest = True
etherTest = True
seringueTest = True
aiguilleTest = True 
tubeTest = True
gainTest = True
loser = True
win = True
cpt = 0
##Instance and generate the elements that permit to Mac Gyver to kill the garden of exit

ether = Element(home, etherPNG)
ether.generate(etherPNG,opening)
tube = Element(home, tubePNG)
tube.generate(seringuePNG, opening)
aiguille = Element(home, aiguillePNG)
aiguille.generate(aiguillePNG, opening)


#Creation de Mac Gyver
Mac_Gyver = Maestro(home)
#continue_game = 1 

#BOUCLE INFINIE
#continuer = False
continuer = True
#continue_intro = False
#intro = True
#jouer = True

	
#direct = pygame.transform.scale((pygame.image.load('MacGyver.png').convert()),(30, 30))					
			
while continuer:

	while acceuilTest :

			opening.blit((pygame.transform.scale(image_acceilPNG, (450, 450))), (0, 0))
			for event in pygame.event.get(): #function to catch a user action	

				if event.type == KEYDOWN: # catch a keyboard action
						                  		
					#Keys movement of Mac Gyver
					if event.key == K_ESCAPE:
						acceuilTest = False

			pygame.display.flip()


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

	#opening.blit(pygame.transform.scale(goal,(30, 30)), (420,420))
		
	home.poster(opening)

	opening.blit (Mac_Gyver.direct,(Mac_Gyver.x, Mac_Gyver.y))
	#pygame.display.flip() # post Mac gyver and playing

	# Unit Test to permit at Mac Gyver  to catch element for his liberty

	if etherTest:
		opening.blit((pygame.transform.scale(etherPNG, (30, 30))), (ether.x, ether.y))
	if (Mac_Gyver.x, Mac_Gyver.y) == (ether.x, ether.y):
		etherTest = False
		opening.blit((pygame.transform.scale(etherPNG, (30, 30))), (800, 800))
		

	if tubeTest:
		opening.blit((pygame.transform.scale(tubePNG, (30, 30))), (tube.x, tube.y))
	if (Mac_Gyver.x, Mac_Gyver.y) == (tube.x, tube.y):
		tubeTest = False
		opening.blit((pygame.transform.scale(tubePNG, (30, 30))), (800, 800))
		

	if aiguilleTest:
		opening.blit((pygame.transform.scale(aiguillePNG, (30, 30))), (aiguille.x, aiguille.y))
	if (Mac_Gyver.x, Mac_Gyver.y) == (aiguille.x, aiguille.y):
		aiguilleTest = False
		opening.blit((pygame.transform.scale(aiguillePNG, (30, 30))), (800, 800))
		
	pygame.display.flip()

	# Mac Gyver take any elements
	if etherTest==False and tubeTest == False and aiguilleTest == False:
		cpt = 1
	if cpt == 1 :

		while seringueTest :

			opening.blit((pygame.transform.scale(seringuePNG, (450, 450))), (0, 0))
			for event in pygame.event.get(): #function to catch a user action	

				if event.type == KEYDOWN: # catch a keyboard action
						                  		
					#Keys movement of Mac Gyver
					if event.key == K_ESCAPE:
						seringueTest = False

			pygame.display.flip()

	if cpt == 0  and home.structure[Mac_Gyver.case_y][Mac_Gyver.case_x] == 3:

		while loser :
			rectScreen = opening.get_rect()
			#police = pygame.font.Font("led.ttf",72)
			police = pygame.font.Font(None,30)
			texte = police.render("Game Over - ECHAP TO QUIT",True,pygame.Color("#FFFF00"))
			rectTexte = texte.get_rect()
			rectTexte.center = rectScreen.center
			opening.fill(pygame.Color("#FF0000"))
			opening.blit(texte,rectTexte)
			for event in pygame.event.get(): #function to catch a user action	

					if event.type == KEYDOWN: # catch a keyboard action
							                  		
						#Keys movement of Mac Gyver
						if event.key == K_ESCAPE:
							loser = False
							continuer = False
			pygame.display.flip()
	

	if cpt == 1 and home.structure[Mac_Gyver.case_y][Mac_Gyver.case_x] == 3:

		while gainTest :
			# rectScreen = opening.get_rect()
			# opening.fill(pygame.Color("#FF0000"))
			opening.blit((pygame.transform.scale(gainPNG, (450, 450))), (0, 0))
			for event in pygame.event.get(): #function to catch a user action	

				if event.type == KEYDOWN: # catch a keyboard action
						                  		
					#Keys movement of Mac Gyver
					if event.key == K_ESCAPE:
						gainTest = False
						continuer = False
			pygame.display.flip()

	pygame.display.flip()






