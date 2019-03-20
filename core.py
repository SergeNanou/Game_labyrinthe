#####Central program


import pygame
from pygame.locals import *
from functions import *
pygame.init()

#Opening of pygame Window

opening = pygame.display.set_mode((450, 450))

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

##Instance and generate the elements that permit to Mac Gyver to kill the garden of exit

ether = Element(home, etherPNG)
ether.generate(etherPNG,opening)
seringue = Element(home, seringuePNG)
seringue.generate(seringuePNG, opening)
aiguille = Element(home, aiguillePNG)
aiguille.generate(aiguillePNG, opening)


#Creation de Mac Gyver
Mac_Gyver = Maestro(home)


#BOUCLE INFINIE
continuer = 1
while continuer :
	
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
					
			elif event.key == K_ESCAPE:
					continuer = 0
			
				
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

	pygame.display.flip()