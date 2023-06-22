import pygame,math
from pygame.locals import *
from random import randrange

pygame.init()
sc = pygame.display.set_mode((800,600))
bg = pygame.image.load("earth.png")

pygame.display.set_caption("UFO GAURD")
icon = pygame.image.load("ufo.png")

img= pygame.image.load("fighter-jet.png")
pygame.display.set_icon(icon)
x_coor = 400
y_coor = 495
x_change = 0

def place(x,y):
    sc.blit(img,(x,y))

e_img  = []
ex_coor = []
ey_coor = []
ex_change = []
ey_change = []

for i in range(6):
    e_img.append(pygame.image.load("enemy.png"))
    ex_coor.append(randrange(0,736))
    ey_coor.append(randrange(50,151))
    ex_change.append(3)
    ey_change.append(50)

def e_place(x,y,i):
    sc.blit(e_img[i],(x,y))

m_img  = pygame.image.load("missile.png")
mx_coor = 0
my_coor = 495
my_change = 10
m_state = False

def fire_missile(x,y):
    global m_state
    m_state = True
    sc.blit(m_img,(x+16,y+16))

def collission(x,y,mx,my):
    val = math.sqrt((math.pow(x-mx,2))+(math.pow(y-my,2)))
    if val<27:
        return True
    return False

font = pygame.font.Font("freesansbold.ttf",32)
final_font = pygame.font.Font("freesansbold.ttf",64)

running = True
score =0
score_x = 10
score_y = 10
def display_score(x,y):
    score_data = font.render(f"score : {score}",True,(0,0,0))
    sc.blit(score_data,(x,y))
def end():
    score_data = final_font.render("GAME OVER",True,(0,0,0))
    sc.blit(score_data,(200,250))
while running:
    sc.fill((255,255,255))
    sc.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                x_change=3.5
            if event.key ==pygame.K_LEFT:
                x_change=-3.5
            if event.key==pygame.K_SPACE:
                    mx_coor = x_coor
                    fire_missile(mx_coor,my_coor)
        if event.type==KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_change=0
    x_coor+=x_change
    if x_coor>=736:
        x_coor=736
    if x_coor<=0:
        x_coor=0
    if my_coor<=0:
        my_coor = 480
        m_state = False
    if m_state==True:
        fire_missile(mx_coor,my_coor)
        my_coor-=my_change

    for i in range(6):
        if ey_coor[i]>440:
            for j in range(6):
                ey_coor[j]=2000
            end()
            break
        ex_coor[i]+=ex_change[i]
        if ex_coor[i]>=736:
            ex_change[i]=-3
            ey_coor[i]+=ey_change[i]
        if ex_coor[i]<=0:
            ex_change[i]=3
            ey_coor[i]+=ey_change[i]
        collide = collission(ex_coor[i],ey_coor[i],mx_coor,my_coor)
        if collide:
            my_coor = 480
            m_state = False
            score+=1
            ex_coor[i] = randrange(0,736)
            ey_coor[i] = randrange(50,151)
        e_place(ex_coor[i],ey_coor[i],i)
    place(x_coor,y_coor)
    display_score(score_x,score_y)
    pygame.display.update()
pygame.quit()