import pygame
import numpy as np
import random
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1000, 600))
table = pygame.display.set_mode((1000,600))
point=0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (40, 0, 0))
screen.blit(textsurface,(0,0))
A, X, X1, Y, Y1, R, Color, Color1, V, V1, U, U1, W, H = [], [], [], [], [], [], [], [], [], [], [], [], [], []
num1=4
num2=3
def new_ball():
    '''рисует новый шарик '''
    x = randint(100, 900)
    y = randint(100, 500)
    r = randint(30, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    v=random.randint(-5,5)
    u=random.randint(-5,5)
    return x,y,r,color, v, u

def ball(x, y, r, color):
    circle(screen, color, (x, y), r)

def balls_in_one_place(num1):
    for i in range(num1):
        for j in range(i+1, num1):
            if (X[i] - X[j])**2 + (Y[i] - Y[j])**2 <= (R[i] + R[j] + 5)**2:
                while (X[i] - X[j])**2 + (Y[i] - Y[j])**2 <= (R[i] + R[j] + 5)**2:
                    X[j], Y[j], R[j], Color[j], V[j], U[j] = new_ball()
                    X[i], Y[i], R[i], Color[i], V[i], U[i] = new_ball()
                balls_in_one_place(num1)

def new_rectangle():
    x = randint(0, 900)
    y = randint(0, 500)
    w = randint(20, 80)
    h= randint(20, 80)
    color = COLORS[randint(0, 5)]
    v=random.randint(3,5)
    u=random.randint(3,5)
    rect(screen, color, (x, y, w, h))
    return x,y,w,h,color,v,u

def rectangle(x, y, w, h, color):
    rect(screen, color, (x, y, w, h))

def rect_in_one_place(num2):
    for i in range(num2):
        for j in range(i+1, num2):
            if (X1[i] - X1[j])**2 + (Y1[i] - Y1[j])**2 <= ((W[i] - W[j])/2)**2+((H[i] - H[j])/2)**2:
                while (X1[i] - X1[j])**2 + (Y1[i] - Y1[j])**2 <= ((W[i] - W[j])/2)**2+((H[i] - H[j])/2)**2:
                    X1[j], Y1[j], W[j], H[j], Color1[j], V1[j], U1[j] = new_rectangle()
                    X1[i], Y1[i], W[i], H[j], Color1[i], V1[i], U1[i] = new_rectangle()
                rect_in_one_place(num2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

pygame.time.set_timer(pygame.USEREVENT+1, 10)
pygame.time.set_timer(pygame.USEREVENT+2, 5000)
pygame.time.set_timer(pygame.USEREVENT+3, 10)
pygame.time.set_timer(pygame.USEREVENT+4, 10)
for i in range(num1):
    x, y, r, color, v, u = new_ball()
    X.append(x)
    Y.append(y)
    R.append(r)
    Color.append(color)
    V.append(v)
    U.append(u)
balls_in_one_place(num1)

for i in range(num2):
    x, y, w, h, color, v, u = new_rectangle()
    X1.append(x)
    Y1.append(y)
    W.append(w)
    H.append(h)
    Color1.append(color)
    V1.append(v)
    U1.append(u)
rect_in_one_place(num2)
while not finished:
    clock.tick(FPS)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Score:'+str(point), False, (255, 255, 255))
    screen.blit(textsurface,(0,0))
    for i in range(num1):
        ball(X[i], Y[i], R[i], Color[i])
    for i in range(num2):
        rectangle(X1[i], Y1[i], W[i], H[i], Color1[i])
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT+2:
            for i in range(num1):
                X[i], Y[i], R[i], Color[i], V[i], U[i] = new_ball()
            balls_in_one_place(num1)
            for i in range(num2):
                X1[i], Y1[i], W[i], H[i], Color1[i], V1[i], U1[i] = new_rectangle()
            rect_in_one_place(num2)  
        elif event.type == pygame.USEREVENT+1:
            for i in range(num1):
                if X[i]+R[i]>1000 or X[i]-R[i]<0:
                    V[i]=-V[i]
                if Y[i]+R[i]>600 or Y[i]-R[i]<0:
                    U[i]=-U[i]
                X[i], Y[i] = X[i]+V[i], Y[i]+U[i]
            for i in range(num2):
                if X1[i]+W[i]>1000 or X1[i]<0:
                    V1[i]=-V1[i]
                if Y1[i]+H[i]>600 or Y1[i]<0:
                    U1[i]=-U1[i]
                if X1[i]<500 and Y1[i]<300:                    
                    X1[i], Y1[i] = X1[i]+V1[i], Y1[i]+U1[i]/5+5*np.sin(X1[i]*2)
                elif X1[i]>500 and Y1[i]<300:
                    X1[i], Y1[i] = X1[i]+V1[i]/5+5*np.sin(Y1[i]*2), Y1[i]+U1[i]
                elif X1[i]<500 and Y1[i]>300:
                    X1[i], Y1[i] = X1[i]+V1[i]/5+5*np.sin(Y1[i]*2), Y1[i]+U1[i]
                else:
                    X1[i], Y1[i] = X1[i]+V1[i], Y1[i]+U1[i]/5+5*np.sin(X1[i]*2)
        elif event.type == pygame.USEREVENT+3:
            for j in range(num1):
                for k in range(j+1,num1):
                    if np.sqrt((X[k]-X[j])**2+(Y[k]-Y[j])**2) <= (R[k]+R[j]+2) : 
                        if V[k]*V[j]>0:
                            if abs(V[k])>abs(V[j]):
                                V[k]=-V[k]
                            else:
                                V[j]=-V[j]
                        else:
                            V[k]=-V[k]
                            V[j]=-V[j]
                        if U[k]*U[j]>0:
                            if abs(U[k])>abs(U[j]):
                                U[k]=-U[k]
                            else:
                                U[j]=-U[j]
                        else:
                            U[k]=-U[k]
                            U[j]=-U[j]
        elif event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            A=event.pos
            for i in range(num1):
                if abs(A[0]-X[i])<R[i] and abs(A[1]-Y[i])<R[i]:
                    point += int(200/R[i])
                    X[i],Y[i],R[i],V[i],U[i] = i, i, 1, 0, 0
            for i in range(num2):
                if abs(A[0]-X1[i]-W[i]/2)<W[i]/2 and abs(A[1]-Y1[i]-H[i]/2)<H[i]/2:
                    point += 50
                    X1[i], Y1[i], W[i], H[i], V1[i], U1[i] = i, i, 0, 0, 0, 0
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
