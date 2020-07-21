import pygame
from functions import *;


pygame.init()
initial_pos = (10,360)
window_H = 600
window_W = 800
pos_List = [initial_pos,(initial_pos[0]+35,initial_pos[1])]
head = (initial_pos[0]+70,initial_pos[1])

window = pygame.display.set_mode((window_W,window_H))
pygame.display.set_caption("Snake")


#game loop
start_game = True
initaite_window(window)

#images
food = pygame.image.load('Images/food.png')
food = pygame.transform.scale(food,(20,20))

face_right = pygame.image.load('Images/face_right.png')
face_right = pygame.transform.scale(face_right,(30,30))

face_left = pygame.image.load('Images/face_left.png')
face_left = pygame.transform.scale(face_left,(30,30))

face_up = pygame.image.load('Images/face_up.png')
face_up = pygame.transform.scale(face_up,(30,30))

face_down = pygame.image.load('Images/face_down.png')
face_down = pygame.transform.scale(face_down,(30,30))

#starting
initiate_snake(window,face_right,initial_pos)
food_spot = spawn_food(window, food)
x= 0
y= 0
#food


#refresh rate
t=200.0 # ms
previous= 0
while start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game= False
        if event.type == pygame.KEYDOWN:
            print("key pressed")
            #the second one to avoid getting the snake go the the way it came.
            if event.key == pygame.K_LEFT and previous!=pygame.K_RIGHT:
                previous = pygame.K_LEFT
                x = -35
                y = 0
                print("L")
            if event.key == pygame.K_RIGHT  and previous!=pygame.K_LEFT:
                previous = pygame.K_RIGHT
                x = 35
                y = 0
                print("R")
            if event.key == pygame.K_UP and previous!=pygame.K_DOWN:
                previous = pygame.K_UP
                x = 0
                y = -35
                print("U")
            if event.key == pygame.K_DOWN and previous!=pygame.K_UP:
                previous = pygame.K_DOWN
                x = 0
                y = 35
                print("D")

    if (x,y) != (0,0):
        if (x,y) == (-35,0):
            face = face_left
        else:
            if (x, y) == (35, 0):
                face = face_right
            else:
                if (x, y) == (0,-35):
                    face = face_up
                else:
                    face = face_down
        if (head[0]+x,head[1]+y) in pos_List or head[0]+x>780 or head[1]+y>580 or head[0]+x<10 or head[1]+y<10:
            lost = True
            while  lost:

                pygame.draw.rect(window, (0, 100, 190), (head[0], head[1], 30, 30))
                window.blit(face, (head[0], head[1]))
                myfont = pygame.font.SysFont('Comic Sans MS', 30)
                textsurface = myfont.render('you died! Your Score is : '+str(int((len(pos_List)-2)*(200-t))), False, (0, 0, 0))
                restart     = myfont.render('Press space to restart ',False, (0, 0, 0))
                window.blit(textsurface, (220,250))
                window.blit(restart, (250, 450))
                pygame.display.update()
                print("you lost!")
                for event in pygame.event.get():
                    if event.type == \
                            pygame.QUIT:
                        start_game = False
                        lost = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            lost = False
                            pos_List = [initial_pos, (initial_pos[0] + 35, initial_pos[1])]
                            head = (initial_pos[0] + 70, initial_pos[1])
                            initaite_window(window)
                            initiate_snake(window, face_right, initial_pos)
                            pygame.display.update()
                            food_spot = spawn_food(window, food)
                            t=200

        pygame.time.wait(int(t))
        t -= 0.5
        if abs(head[0] - food_spot[0]) <10 and abs(head[1] - food_spot[1]) <10:
            print("YUM!!!")
            food_spot = spawn_food(window, food)
            pos_List=add_one(window, x, y, pos_List, head, face)
        else:
            update_window(window,x,y,pos_List[0],head,face,food_spot)
        pos_List.pop(0)
        pos_List.append((head))
        head = (head[0] + x, head[1] + y)



    #draw rectangle:
    #add(window)
    pygame.display.update()
