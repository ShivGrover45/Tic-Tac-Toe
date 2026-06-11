import pygame
from pygame.locals import *

pygame.init()

#Screen variables
screen_height = 300
screen_width = 300
markers=[]
clicked = False
pos=[]
player1=1


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

def grid():
    bg=(255, 255, 200)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, (20, 0, 0), (x*100, 0), (x*100, 300), 3)  
        for y in range(1,3):
            pygame.draw.line(screen, (20, 0, 0), (0, y*100), (300, y*100), 3)
for x in range(3):
    row = [0] * 3
    markers.append(row)

run = True
while run:
    grid()
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type==pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked=True
        if event.type==pygame.MOUSEBUTTONUP and clicked == True:
            clicked=False
            pos=pygame.mouse.get_pos()
            cell_x=pos[0]
            cell_y=pos[1]
            if markers[cell_x//100][cell_y//100]==0:
                markers[cell_x//100][cell_y//100]=player1
                player1*=-1



    
    pygame.display.update()


pygame.quit()