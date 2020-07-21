import pygame

pygame.init()

window_H = 600
window_W = 800


black =(0,0,0)
blue  =(0,100,190)

window = pygame.display.set_mode((window_W,window_H))
pygame.display.set_caption("Snake")


#game loop
start_game = True
while start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game= False

    #draw rectangle:
    pygame.draw.rect(window, blue, (10, 10, 780, 580))
    pygame.display.update()
