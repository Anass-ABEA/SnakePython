import pygame
import random

from past.builtins import execfile


def initiate_snake(window,face_right,pos):
    pygame.draw.rect(window, (0,190,100), (pos[0], pos[1], 30, 30))
    pygame.draw.rect(window, (0, 190, 100), (pos[0]+5+30, pos[1], 30, 30))
    window.blit(face_right,(pos[0]+(5+30)*2, pos[1]))

def initaite_window(window):
    pygame.draw.rect(window, (0, 0, 0), (0, 0, 800, 600))
    pygame.draw.rect(window, (0,100,190), (10, 10, 780, 580))


def update_window(window,x,y,tail,head,face,food):
    pygame.draw.rect(window, (0,100,190), (tail[0], tail[1], 30, 30))
    pygame.draw.rect(window, (0, 190, 100), (head[0], head[1], 30, 30))
    window.blit(face,(head[0]+x, head[1]+y))

def spawn_food(window,food):
    a= random.randint(1,20)
    a = a*35 + 15
    b= random.randint(1,15)
    b = b*35 + 15
    window.blit(food, (a,b))
    return a,b


def add_one(window, x, y, pos_List, head, face):
    pygame.draw.rect(window, (0, 190, 100), (head[0], head[1], 30, 30))
    window.blit(face, (head[0] + x, head[1] + y))
    return [pos_List[0]]+pos_List
