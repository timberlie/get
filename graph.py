import math
import pygame

white = (200, 200, 200)
red = (255, 0, 0)
blue = (50, 0, 255)
black = (0, 0, 0)

width = 1400
hight = 800
screen = pygame.display.set_mode((width, hight))
clock = pygame.time.Clock()
pygame.display.set_caption('furie')
fps = 60

angel = 0
angel2 = 0
angel3 = 0
angel4 = 0
iterator = 0
m = []
time = 0

radius1 = 100
radius2 = 40
radius3 = 20
radius4 = 10

velosity1 = 1
velosity2 = 3
velosity3 = 5
velosity4 = 7

run = True
while (run):
    if time % 1 == 0:
        screen.fill(black)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
    pygame.draw.circle(screen, white, (200, 400), radius1, 2)
    pygame.draw.circle(screen, red, (int(math.cos(angel) * radius1) + 200, int(math.sin(angel) * radius1) + 400), 3)
    pygame.draw.line(screen, blue, (200, 400),  (int(math.cos(angel) * radius1) + 200, int(math.sin(angel) * radius1) + 400), 4)
    pygame.draw.circle(screen, white, (int(math.cos(angel) * radius1) + 200, int(math.sin(angel) * radius1) + 400), radius2, 2)
    pygame.draw.circle(screen, red, (int(math.cos(angel2) * radius2)  + int(math.cos(angel) * radius1) + 200, int(math.sin(angel2) * radius2)  + int(math.sin(angel) * radius1) + 400), 3)
    x = int(math.cos(angel2) * radius2)  + int(math.cos(angel) * radius1) + 200
    y = int(math.sin(angel2) * radius2)  + int(math.sin(angel) * radius1) + 400
    pygame.draw.line(screen, blue, (x, y),  (int(math.cos(angel) * radius1) + 200, int(math.sin(angel) * radius1) + 400), 4)
    pygame.draw.circle(screen, white, (x, y), radius3, 2)
    pygame.draw.circle(screen, red, (int(math.cos(angel3) * radius3) + x, int(math.sin(angel3) * radius3) + y), 3)
    x2 = int(math.cos(angel3) * radius3) + x
    y2 = int(math.sin(angel3) * radius3) + y
    pygame.draw.line(screen, blue, (x, y),  (x2, y2), 4)
    pygame.draw.circle(screen, white, (x2, y2), radius4, 2)
    pygame.draw.circle(screen, red, (int(math.cos(angel4) * radius4) + x2, int(math.sin(angel4) * radius4) + y2), 3)
    pygame.draw.line(screen, blue, (x2, y2),  (int(math.cos(angel4) * radius4) + x2, int(math.sin(angel4) * radius4) + y2), 4)
    m.append((int(math.cos(angel4) * radius4) + x2, int(math.sin(angel4) * radius4) + y2, time))
    for i in range(len(m)):
        pygame.draw.circle(screen, blue, (400 - m[i][2] + time , m[i][1]), 2)
    pygame.draw.line(screen, blue, (400 - m[len(m) - 1][2] + time , m[len(m) - 1][1]), (int(math.cos(angel4) * radius4) + x2, int(math.sin(angel4) * radius4) + y2), 4)

    angel += math.pi / 360 * velosity1
    angel2 += math.pi / 360 * velosity2
    angel3 += math.pi / 360 * velosity3
    angel4 += math.pi / 360 * velosity4
    time += 1
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
