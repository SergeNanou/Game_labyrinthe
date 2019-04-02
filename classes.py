# Package import
import pygame
from pygame.locals import *
import random

# Class creation


class Game_environnement:

    """"Create a game environnement """
    def __init__(self):
        self.structure = 0

    def create(self):
        """"Create a maze with a exhaustive exploration """

        # number of boxes not walled
        taille_Max = 7
        #  direction we take to break a wall in width
        move_X = {'N': 0, 'S': 0, 'E': 1, 'O': -1}
        # diretion we take to break a wall in height
        move_Y = {'N': 1, 'S': -1, 'E': 0, 'O': 0}
        # matrix of the state of boxes(0 not seen or 1 seen)
        dejavu = [[0 for x in range(taille_Max)] for y in range(taille_Max)]

        # we create a labyrinth with a wall enter the boxes of maze
        # (the goal is to break this wall
        # to unite all the boxes of the maze)

        # we init the all values of maze at zero
        laby = [[0 for x in range(2*taille_Max+1)] for y in range(2*taille_Max+1)]

        # we put a boxes  of maze enter the wall symbolizing
        # by 1 = boxes and 0 = walls in matrix maze
        # we  traverse each row of matrix maze
        for y in range(len(laby)-1):
            # we traverse each cells of row
            for x in range(len(laby[y])-1):
                if x % 2 != 0 and y % 2 != 0:
                    laby[y][x] = 1

        # we choice in random one cell in dejavu matrix
        # for begining the union of maze cell
        Cell_rand = ((random.randrange(taille_Max)), (random.randrange(taille_Max)))
        lastCell = [(Cell_rand)]

        # we make a while loop to visit all boxes of maze for the union.
        while lastCell != []:
            (x, y) = lastCell[-1]  # we take the last element of the pile
            dejavu[y][x] = 1
            lNeighboors = []
            for move in ['N', 'S', 'O', 'E']:
                # the width of the cell we use to make a union
                x_1 = x + move_X[move]
                # the width of the cell we use to make a union
                y_1 = y + move_Y[move]
                if x_1 >= 0 and x_1 < taille_Max and y_1 >= 0 and y_1 < taille_Max:
                    # we check if a boxe are not visited
                    if dejavu[y_1][x_1] == 0:

                        lNeighboors.append(move)

            if len(lNeighboors) > 0:
                # we choice randomly a neighboors boxe to make a union
                var = random.choice(lNeighboors)
                # In the maze this position are((2x+1,2y+1),(2x_1+1,2y_1+1),
                # middle of the two cells(wall) = (x +x_1+1,y,y_1+1),
                # the method is to break this wall to unit the two boxes of maze
                laby[x+x+move_X[var]+1][y+y+move_Y[var]+1] = 1
                # we udpate the position of boxes to continue the maze boxes union
                x, y = x + move_X[var], y + move_Y[var]

                lastCell.append((x, y))
            else:
                lastCell.pop()
        # start maze position
        laby[1][1] = 2
        # end maze position
        laby[2*taille_Max-1][2*taille_Max-1] = 3
        self.structure = laby

    def poster(self, opening):

        """"function to post the struct"""

        wall = pygame.image.load('Images\\floor-tiles-20x20.png').convert()  # import a Wall Image
        goal = pygame.image.load('Images\\Gardien.png').convert()  # import Garden goal Image
        tail_sprite = 30
        # we walk through each line of a structure
        num_row = 0
        for row in self.structure:
            # we walk through each element of row
            num_case = 0
            for sprite in row:
                # we calcul the elemnent tail in pixels
                x = num_case * tail_sprite
                y = num_row * tail_sprite
                if sprite == 0:  # w = Wall(built Wall)
                    opening.blit(pygame.transform.scale(wall, (30, 30)), (x, y))
                elif sprite == 3:  # g = goal(freedom)
                    opening.blit(pygame.transform.scale(goal, (30, 30)), (x, y))
                num_case += 1
            num_row += 1


class Element:
    """"Create a element class for kill a garden """

    def __init__(self, home, image):  # constructor of Element class
        self.home = home
        self.image = image
        self.x = 0
        self.y = 0
        sprite_dim = 30
        self.possible = True

    def generate(self, image, home):
        """"Create a methode  to generate this element """
        while self.possible:
            self.case_x = random.randint(0, 14)  # generate randomly a number
            self.case_y = random.randint(0, 14)  # generate randomly a number
            # value to know if we have a wall or no
            position_create = self.home.structure[self.case_y][self.case_x]
            if position_create == 1:
                # We define/accept the position for the object
                self.y = self.case_y * 30
                self.x = self.case_x * 30
                self.possible = False  # We construct the element once


class Maestro:
    """"Create Mac Gyver class to define his attributs and his methods"""

    def __init__(self, home):  # constructor class

        self.case_x = 1
        self.case_y = 1
        self.x = 30
        self.y = 30
        self.home = home
        self.direct = pygame.transform.scale((pygame.image.load('Images\MacGyver.png').convert()), (30, 30))

    def move(self, directory):
        """"Create Mac Gyver method to permit Mac Gyver to moving"""

        tail_sprite = 30
        nombre_sprite_cote = 15
        # move to right
        if directory == 'right':
            # For don't go out
            if self.case_x < (nombre_sprite_cote - 1):
                # We verify if they don't have Wall
                if self.home.structure[self.case_y][self.case_x+1] != 0:
                    # move to one hut
                    self.case_x += 1
                    # Calculate real position Mac Gyver position
                    self.x = self.case_x * tail_sprite

        # move to left
        if directory == 'left':
            if self.case_x > 0:
                if self.home.structure[self.case_y][self.case_x-1] != 0:
                    self.case_x -= 1
                    self.x = self.case_x * tail_sprite

        # move to top
        if directory == 'top':
            if self.case_y > 0:
                if self.home.structure[self.case_y-1][self.case_x] != 0:
                    self.case_y -= 1
                    self.y = self.case_y * tail_sprite
        # move to low
        if directory == 'low':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.home.structure[self.case_y+1][self.case_x] != 0:
                    self.case_y += 1
                    self.y = self.case_y * tail_sprite
