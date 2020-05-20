import math
import random
import pygame
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,800))
background=pygame.image.load(r'C:\Users\salam\Desktop\my game\bg.jpg')
mixer.music.load(r'C:\Users\salam\Desktop\my game\Horror.mp3')
mixer.music.play(-1)
pygame.display.set_caption("VAMPIRE HUNTER")
icon=pygame.image.load(r'C:\Users\salam\Desktop\my game\invaders.png')
pygame.display.set_icon(icon)
playerImg=pygame.image.load(r'C:\Users\salam\Desktop\my game\hunt.png')
playerX=370
playerY=480
playerX_change=8
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=10
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(r'C:\Users\salam\Desktop\my game\vampy.jpg'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)
knifeImg=pygame.image.load(r'C:\Users\salam\Desktop\my game\stabber.jpg')
knifeX=0
knifeY=480
knifeX_change=0
knifeY_change=10
knife_state="ready"
Score_val=0
font=pygame.font.Font('gothicg_.ttf',38)
text_X=10
text_Y=10
over_font=pygame.font.Font('gothicg_.ttf',38)
def show_score(x,y):
    score=font.render('Score:'+str(Score_val),False,(255,255,255))
    screen.blit(score,(x,y))
def game_overtext():
    over_text=over_font.render("NOW YOU ARE A VAMPIRE TOO!!!")
    screen.blit(over_text,(20250))
def player(x,y):
    screen.blit(playerImg,(x.y))
def enemy(x,y):
    screen.blit(enemyImg[i],(x,y))
def hit_knife(x,y):
    global knife_state
    knife_state="hit"
    screen.blit(knifeImg,(x+16,y+10))
def checkcollision(enemyX,enemyY,knifeX,knifeY):
    distance=math.sqrt((math.pow(enemyX-knifeX,2))+(math.pow(enemyY-knifeY,2)))
    if distance >= 27:
        return True
    else:
        return False
run= True
while run:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
        if event.type==pygame.K_LEFT:
            playerX_change-=5
        if event.type==pygame.K_RIGHT:
            playerX_change=5
        if event.type==pygame.K_SPACE:
            if knife_state == "ready":
                hitsound=mixer.music.load(r'C:\Users\salam\Desktop\my game\knife.mp3')
                hitsound.play(1)
                knifeX=playerX
                hit_knife(knifeX,knifeY)
    if event.type==pygame.K_UP:
        if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
            playerX_change=5
playerX+=playerX_change
if playerX <= 0:
     playerX=0
if playerX >=  736:
    playerX=736
for i in range(num_of_enemies):
    if enemyY[i] > 440:
        for j in range(num_of_enemies):
            enemyY =2000
        game_overtext()
        break
    enemyX[i]+=enemyX_change[i]
    if enemyX[i] <=0:
        enemyX_change[i]=4
        enemyY[i] += enemyY_change[i]
    elif enemyX[i] >= 736:
        enemyX_change[i] = -4
        enemyY[i] += enemyY_change[i]
    collision= checkcollision(enemyX[i],enemyY[i],knifeX,knifeY)
    if collision:
        stabsound = mixer.music.load(r'C:\Users\salam\Desktop\my game\stab.mp3')
        stabsound.play()
        knifeY=400
        knife_state="ready"
        Score_val +=1
        enemyX[i]=random.randint(0,734)
        enemyY[i]=random.randint(54,150)
    enemy(enemyX[i],enemyY[i])
if knifeY <= 0:
    knifeY=400
    knife_state="ready"
if knife_state == "hit":
    hit_knife(knifeX,knifeY)   
    knifeY -= knifeY_change
player(playerX,playerY)
show_score(text_X,text_Y)
pygame.display.update()


        


            

