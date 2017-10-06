from random import randint
from pygame.locals import *
import pygame
import sys
pygame.init()

key = pygame.key.get_pressed()
CLOCK = pygame.time.Clock()
WIDTH = 800
HEIGHT = WIDTH // 2
COUNT = 20
W = WIDTH // COUNT
H = HEIGHT // COUNT
cells = []

class Mouse:
    def __init__(self,x=0,y=0,w=W,h=H):
        self.rect = pygame.Rect((x,y,w,h))

    def move(self):
        key = pygame.key.get_pressed()
        if (key[K_DOWN] or key[K_s]) and self.rect.bottom != HEIGHT:
            self.rect.y += H
        if (key[K_UP] or key[K_w]) and self.rect.top != 0:
            self.rect.y += -H
        if (key[K_LEFT] or key[K_a]) and self.rect.left != 0:
            self.rect.x += -W
        if (key[K_RIGHT] or key[K_d]) and self.rect.right != WIDTH:
            self.rect.x += W
        pygame.time.wait(50)

    def draw(self):
        pygame.draw.rect(DISPLAY, MOUSE_COLOR, self.rect)

class Cells:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x*W, y*H,W,H)
        self.visit = False

    def visited(self):
        key = pygame.key.get_pressed()
        if self.rect.center == mouse.rect.center and key[K_LSHIFT] != True:
            self.visit = True
        if key[K_r]:
            self.visit = False
        if key[K_z] and self.rect.center == mouse.rect.center:
            self.visit = False

    def draw(self):
        if self.visit:
            pygame.draw.rect(DISPLAY, CELLS_COLOR_2, self.rect)
        else:
            pygame.draw.rect(DISPLAY, CELLS_COLOR, self.rect, 1)

def group():
    for y in range(H):
        for x in range(W):
            cells.append(Cells(x,y))

def change_color():
    global DISPLAY_COLOR, CELLS_COLOR, CELLS_COLOR_2, MOUSE_COLOR
    DISPLAY_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
    CELLS_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
    CELLS_COLOR_2 = (randint(0, 255), randint(0, 255), randint(0, 255))
    MOUSE_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))

change_color()
mouse = Mouse()
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cell Painter")
group()

def disp():
    DISPLAY.fill(DISPLAY_COLOR)
    for cell in cells:
        cell.visit = False
        cell.draw()
    mouse.draw()

def main():
    DISPLAY.fill(DISPLAY_COLOR)
    for cell in cells:
        cell.visited()
        cell.draw()
    mouse.move()
    mouse.draw()
    pygame.display.update()


while True:
    key = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        if key[K_c]:
            change_color()
    main()