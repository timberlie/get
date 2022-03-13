import pygame
import math

#color setup
white = (255, 255, 255)
black = (0, 0, 0)
gray = (125, 125, 125)
blue = (64, 128, 255)
green = (0, 200, 64)
yellow = (225, 225, 0)
pink = (230, 50, 230)
red = (250, 0, 0)

#screen setup
width = 2000
hight = 1600
screen = pygame.display.set_mode((width, hight))
clock = pygame.time.Clock()# creat a clock to draw screen by fps
pygame.display.set_caption('multyplication timetable')
fps = 120

#function of distribution points and lines
def equal_distance_separation(number, radius, iterator, coffie, c1, c2, c3):
    alfa = 2 * math.pi / number * iterator #angel in polar system
    radius -= radius * 0.005 #colhoz)
    pygame.draw.circle(screen, yellow, (int(radius * math.cos(alfa)) + 500, int(radius * math.sin(alfa)) + 400), 2)
    if iterator * coffie / number > 1: # if circle is end, we go again
        next_alfa = 2 * math.pi / number * iterator * coffie - 2 * math.pi
    else:
        next_alfa = 2 * math.pi / number * iterator * coffie
    x = radius * math.sin(next_alfa) + 500 #draw lines with prev and next points
    y = radius * math.cos(next_alfa) + 400
    pygame.draw.line(screen, (c1, c2, c3), (int(radius * math.cos(alfa)) + 500, int(radius * math.sin(alfa)) + 400), (int(x), int(y)))

#constant setup
coffie = 490 #defolt 490
time = 0
c1, c2, c3 = 255, 0, 0
flag = 1

#first prime draw
pygame.draw.circle(screen, red, (500, 400), 300, 5)
for i in range(100):
    equal_distance_separation(100, 300, i, coffie, c1, c2 , c3)

pygame.display.update()

run = True #infinite mainloop
while run:
    if time % 1 == 0: #clean the screen
        screen.fill(black)
    for events in pygame.event.get(): #if 'alt + f4' then quit
        if events.type == pygame.QUIT:
            run = False

    pygame.draw.circle(screen, red, (500, 400), 300, 5) # draw every sinle time
    for i in range(500):
        equal_distance_separation(500, 300, i, coffie, c1, c2 , c3)
    coffie += 0.005
    time += 1

    if flag == 1: #color change
        if c1 == 15:
            flag = 2
        c1 -= 1
        c3 += 1
    if flag == 2:
        if c2 == 254:
            flag = 3
        c2 += 1
    if flag == 3:
        if c3 == 15:
            flag = 4
        c3 -= 1
    if flag == 4:
        if c1 == 254:
            flag = 5
        c1 += 1
    if flag == 5:
        if c2 == 15:
            flag = 1
        c2 -= 1

    pygame.display.set_caption(str(coffie)) #writing the constant
    pygame.display.update()

    clock.tick(fps)

pygame.quit() #end.
