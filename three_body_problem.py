import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import math
import pygame

#setup
width, hight = 1200, 800
screen = pygame.display.set_mode((width, hight)) # основные настройки для работы с pygame
pygame.display.set_caption('three body task')
clock = pygame.time.Clock()
fps = 60
#color
white = (255, 255, 255) #настройка цветов для отрисовки
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

x0, y0 = 600, 400 # задание центра экрана

#0.01141625
angel = 0 # угол вращения подвижной системы отсчета
m1 = 2 # массы объектов
m2 = 10
r = 200 # радиус между массивными телами
g = 100 # коэффициент для задания потенциальной энергии

w = math.sqrt(g * (m1 + m2) / r) / 195.86

x = r / 2 - r * m2 / (m1 + m2) # начальное положение спутника
y = 170 #170

v_x = 0
 # начальная скорость
v_y = 0

d_v_x = 0 #начальное ускорение
d_v_y = 0

m = [] #массив для хранения пройденного пути

def W_derive_x(x,y): # расчет производной потенциала по х
    s1 = (-1) * m1 * ( (x + (m2*r)/(m1+m2)) / (((x + (m2*r)/(m1 + m2))**2 + y**2)**(1.5)) )
    s2 = (-1) * m2 * ( (x - (m1*r)/(m1+m2)) / (((x - (m1*r)/(m1 + m2))**2 + y**2)**(1.5)) )
    return (s1 + s2) * g

def W_derive_y(x,y): # расчет производной потенциала по у
    s1 = (-1) * m1 * ((((x + m2*r/(m1 + m2))**2 + y**2)**(-1.5))*y)
    s2 = (-1) * m2 * ((((x - m1*r/(m1 + m2))**2 + y**2)**(-1.5))*y)
    return (s1 + s2) * g

run = True
flag = False
while(run):
    d_v_x = 2*w*v_y + x*w**2 + W_derive_x(x,y) # уравнения движения
    d_v_y = (-2)*w*v_x + y*w**2 + W_derive_y(x,y)
    if abs(d_v_x) > 6 or abs(d_v_y) > 6:
        break
    
    v_x += d_v_x / math.exp(abs(d_v_x) / 100)
    v_y += d_v_y / math.exp(abs(d_v_y) / 100)

    x += v_x
    y += v_y

    
    angel += w
    print(x, v_x, d_v_x)
    m.append((int(x*math.cos(angel) + y*math.sin(angel)),int(- x*math.sin(angel) + y*math.cos(angel)))) #добавляем в историю пути координаты в неподвижной системе отсчета
    screen.fill(black)
    for events in pygame.event.get(): # закрытие окна
        if events.type == pygame.QUIT:
            run = False
    pygame.draw.circle(screen, red, (int(x0 - r*m2/(m1+m2) * math.cos(angel)), int(y0 + r*m2/(m1+m2)*math.sin(angel))), int(m1 * 2)) # отрисовка планет
    pygame.draw.circle(screen, red, (int(x0 + r*m1/(m1+m2) * math.cos(angel)), int(y0 - r*m1/(m1+m2)*math.sin(angel))), int(m2 * 2))
    pygame.draw.circle(screen, green, (int(m[len(m) - 1][0])+x0,int(m[len(m) - 1][1])+y0), 4) # отрисовка спутника
    for i in range(1, len(m)):#tail_go from 0
        pygame.draw.line(screen, green, (int(m[i][0])+x0,int(m[i][1])+y0), (int(m[i-1][0]) + x0 ,int(m[i-1][1]) + y0), 2) #отрисовка пути 
    pygame.display.update()
    clock.tick(fps)
pygame.quit()

X_0 = []
Y_0 = [] # отрисовка пути как графика
for i in m:
    X_0.append(i[0])
    Y_0.append(i[1])
X = np.array(X_0, float)
Y = np.array(Y_0, float)
# plt.scatter(X, Y)
plt.plot(X, Y)
plt.legend(loc='best')
plt.grid(True)
plt.show()
