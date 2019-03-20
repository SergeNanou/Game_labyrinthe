import pygame
from pygame.locals import *
from functions import *
pygame.init()



a = Structure()
a.create()
out = Element(a)
out.indicate()
print(out.book.items())
