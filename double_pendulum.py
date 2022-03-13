import math
import pygame
#setup
width, hight = 1200, 800
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption('double pendulum')
clock = pygame.time.Clock()
fps = 60
#color
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
#constants
a1 = 0
a2 = 0
r1 = 200
r2 = 200
m1 = 20
m2 = 20
x0 = 600
y0 = 200
vel1 = 0.0
vel2 = 0.0
aq1 = 0
aq2 = 0
g = 1
m = []

def aq1_aq2(a1, a2, m1, m2, vel1, vel2, r1, r2):
    num1 = g * (2 * m1 + m2) * math.sin(a1)
    num2 = m2 * g * math.sin(a1 - 2 * a2)
    num3 = 2 * math.sin(a1 - a2) * m2 * ((vel2 ** 2) * r2 + (vel1 ** 2) * r1 * math.cos(a1 - a2))
    top1 = - num1 - num2 - num3
    aq1 = top1 / (r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2)))
    num4 = 2 * math.sin(a1 - a2)
    num5 = (vel1 ** 2) * r1 * (m1 + m2) + g * (m1 + m2) * math.cos(a1) + (vel2 ** 2) * r2 * m2 * math.cos(a1 - a2)

    top2 = num4 * num5
    aq2 = top2 / (r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2)))
    return (aq1, aq2)

def vertex_search(x2, y2, r1, r2, x0, y0):
    d = math.sqrt((x0 - x2)**2 + (y0 - y2)**2)
    a = (r1**2 - r2 **2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    x3 = x0 + (a / d) * (x2 - x0)
    y3 = y0 + (a / d) * (y2 - y0)

    y4 = y3 + (h / d) * (x2 - x0)
    x4 = x3 - (h / d) * (y2 - y0)
    return (x4, y4)

flag = False
#main
run = True
while(run):
    screen.fill(black)
    aq1 = aq1_aq2(a1, a2, m1, m2, vel1, vel2, r1, r2)[0]
    aq2 = aq1_aq2(a1, a2, m1, m2, vel1, vel2, r1, r2)[1]
    vel1 += aq1
    vel2 += aq2
    vel1 *= 0.9998 #friquency AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    vel2 *= 0.9998
    a1 += vel1
    a2 += vel2
    x1 = r1 * math.sin(a1) + x0
    y1 = r1 * math.cos(a1) + y0
    x2 = r2 * math.sin(a2) + x1
    y2 = r2 * math.cos(a2) + y1
    m.append((int(x2), int(y2)))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
        elif events.type == pygame.MOUSEBUTTONDOWN:
            flag = True
        elif events.type == pygame.MOUSEBUTTONUP:
            flag = False
    if flag:
        aq1 = 0
        aq2 = 0
        vel1 = 0
        vel2 = 0
        if r1 + r2 >= math.sqrt((x0 - events.pos[0])**2 + (y0 - events.pos[1])**2):
            x2 = events.pos[0]
            y2 = events.pos[1]
            x1 = vertex_search(x2, y2, r1, r2, x0, y0)[0]
            y1 = vertex_search(x2, y2, r1, r2, x0, y0)[1]
            if x2 >= x1 and x1 > x0:
                a1 = math.acos((y1 - y0) / r1)
                a2 = math.acos((y2 - y1) / r2)
            elif x1 >= x0:
                a1 = math.acos((y1 - y0) / r1)
                a2 =  - math.acos((y2 - y1) / r2)
            elif x2 <= x1:
                a1 =  - math.acos((y1 - y0) / r1)
                a2 =  - math.acos((y2 - y1) / r2)
            elif x1 < x0 and x2 > x1:
                a1 = - math.acos((y1 - y0) / r1)
                a2 =  math.acos((y2 - y1) / r2)
        else:
            pass
        m = []
    tail_go = int(len(m) / 4)######################################
    for i in range(1, len(m)):#tail_go from 0
        pygame.draw.line(screen, green, m[i], m[i - 1], 2)
    pygame.draw.line(screen, white, (int(x0), int(y0)), (int(x1), int(y1)), 4)
    pygame.draw.line(screen, white, (int(x1), int(y1)), (int(x2), int(y2)), 4)
    pygame.draw.circle(screen, red, (int(x1), int(y1)), int(m1 * 0.6))
    pygame.draw.circle(screen, red, (int(x2), int(y2)), int(m2 * 0.6))
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
