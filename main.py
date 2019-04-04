# Main  program

# Packages import


import pygame
from pygame.locals import *
from classes import *

pygame.init()

# Opening of pygame Window

opening = pygame.display.set_mode((450, 450))
# Title and icone of opening

pygame.display.set_caption("Mac Gyver release !")
title_image = pygame.image.load("Images\MacGyver.png").convert_alpha()
pygame.display.set_icon(title_image)
# Game soon
son_intro = pygame.mixer.Sound("musics\\346.wav")
son_play = pygame.mixer.Sound("musics\\627.wav")
son_kill = pygame.mixer.Sound("musics\\620.wav")
son_win = pygame.mixer.Sound("musics\\646.wav")

# background image
background = pygame.image.load("Images\ciel-bleu.jpg").convert()

# Mac Gyver element import
goalPNG = pygame.image.load('Images\\Gardien.png').convert()
etherPNG = pygame.image.load('Images\ether.png').convert()
seringuePNG = pygame.image.load('Images\seingue_2.png').convert()
aiguillePNG = pygame.image.load("Images\\aiguille.png").convert()
tubePNG = pygame.image.load('Images\\tube_plastique.png').convert()
image_acceilPNG = pygame.image.load('Images\\acceuil_3.png').convert()
winPNG = pygame.image.load('Images\Gain.png').convert()
exitPNG = pygame.image.load('Images\\fond.jpg').convert()
riskPNG = pygame.image.load('Images\\risk.png').convert()
# Instance of game_envirronement

home = Game_environnement()
home.create()
tail_sprite = 30
# Instance test variables
acceuilTest = True
etherTest = True
seringueTest = True
aiguilleTest = True
tubeTest = True
gainTest = True
loser = True
win = True
cpt = 0
continuer = True
riskTest = True
# Instance and generate the elements that permit to Mac Gyver
# to kill the garden of exit

ether = Element(home, etherPNG)
ether.generate(etherPNG, opening)
tube = Element(home, tubePNG)
tube.generate(seringuePNG, opening)
aiguille = Element(home, aiguillePNG)
aiguille.generate(aiguillePNG, opening)

# Mac Gyver creation
Mac_Gyver = Maestro(home)

# BOUCLE INFINIE
while continuer:
    # Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)
    son_play.play()
    while acceuilTest:
            opening.blit((pygame.transform.scale(image_acceilPNG, (450, 450))), (0, 0))
            # function to catch a user action
            for event in pygame.event.get():
                # catch a keyboard action
                if event.type == KEYDOWN:
                    # Keys movement of Mac Gyver
                    if event.key == K_ESCAPE:
                        acceuilTest = False
            pygame.display.flip()
    # function to catch a user action
    for event in pygame.event.get():
        # catch a keyboard action
        if event.type == KEYDOWN:
            # Keys movement of Mac Gyver
            if event.key == K_RIGHT:
                Mac_Gyver.move('right')
            if event.key == K_LEFT:
                Mac_Gyver.move('left')
            if event.key == K_UP:
                Mac_Gyver.move('top')
            if event.key == K_DOWN:
                Mac_Gyver.move('low')
            # quit the opening
            elif event.key == K_ESCAPE:
                    continuer = False
# Construct a maze
    opening.blit((pygame.transform.scale(background, (450, 450))), (0, 0))
    opening.blit((pygame.transform.scale(goalPNG, (30, 30))), (420,420))
    # opening.blit(pygame.transform.scale(goal,(30, 30)), (420,420))
    home.poster(opening)
    # post Mac gyver and his moving
    opening.blit(Mac_Gyver.direct, (Mac_Gyver.x, Mac_Gyver.y))
    # Unit Test to permit at Mac Gyver  to catch element for his freedom

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
    if etherTest == False and tubeTest == False and aiguilleTest == False:
        cpt = 1
    if cpt == 1:

        while seringueTest:

            opening.blit((pygame.transform.scale(seringuePNG, (450, 450))), (0, 0))
            # function to catch a user action
            for event in pygame.event.get():
                # catch a keyboard action
                if event.type == KEYDOWN:           
                    # Keys movement of Mac Gyver
                    if event.key == K_ESCAPE:
                        seringueTest = False

            pygame.display.flip()

    if cpt == 0 and (Mac_Gyver.x, Mac_Gyver.y) == (420, 420):
        # we cut game session if a player losing
        while loser:
            son_kill.play()
            rectScreen = opening.get_rect()
            # police = pygame.font.Font("led.ttf",72)
            police = pygame.font.Font(None, 30)
            texte = police.render("Ah MAC GYVER DIED!!! - ECHAP TO QUIT", True, pygame.Color("#FFFF00"))
            rectTexte = texte.get_rect()
            rectTexte.center = rectScreen.center
            opening.fill(pygame.Color("#FF0000"))
            opening.blit(texte, rectTexte)
            for event in pygame.event.get():

                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            loser = False
                            continuer = False
            pygame.display.flip()
    if cpt == 1 and (Mac_Gyver.x, Mac_Gyver.y) == (420, 420):
        # we cut a game session if a player winning
        while gainTest:
            son_win.play()
            opening.blit((pygame.transform.scale(winPNG, (450, 450))), (0, 0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        gainTest = False
                        continuer = False
            pygame.display.flip()

    if riskTest:
        # we post a risk image around the garden
        opening.blit((pygame.transform.scale(riskPNG, (30, 30))), (360, 420))
        opening.blit((pygame.transform.scale(riskPNG, (30, 30))), (390, 420))
        opening.blit((pygame.transform.scale(riskPNG, (30, 30))), (420, 360))
        opening.blit((pygame.transform.scale(riskPNG, (30, 30))), (420, 390))
        if (Mac_Gyver.x, Mac_Gyver.y) == (360, 390) or (Mac_Gyver.x, Mac_Gyver.y) == (390, 360) :
            riskTest = False
        # pygame.display.flip()
    opening.blit((pygame.transform.scale(goalPNG, (30, 30))), (420, 420))
    pygame.display.flip()







