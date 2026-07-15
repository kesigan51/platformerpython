import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Platformer")
fps = pygame.time.Clock()

#bg
bg = pygame.image.load("bg/BG.png")
bg = pygame.transform.scale(bg,(800,600))

#land1
land1 = ["bg/5.png","bg/2.png"]
n1 = pygame.image.load(land1[1])
n1 = pygame.transform.scale(n1,(60,80))
n2 = pygame.image.load(land1[1])
n2 = pygame.transform.scale(n2,(60,80))
n3 = pygame.image.load(land1[1])
n3 = pygame.transform.scale(n3,(60,80))
n4 = pygame.image.load(land1[1])
n4 = pygame.transform.scale(n4,(60,80))

#fly
land2 = ["bg/fle.png","bg/fmi.png","bg/fri.png"]
f1 = pygame.image.load(land2[0])
f1 = pygame.transform.scale(f1,(60,70))
f2 = pygame.image.load(land2[1])
f2 = pygame.transform.scale(f2,(60,70))
f3 = pygame.image.load(land2[2])
f3 = pygame.transform.scale(f3,(60,70))

#player
player = pygame.image.load("player/Idle .png")
player = pygame.transform.scale(player,(60,70))
an = ["player/Jump .png","player/Dead.png","player/2.png","player/4.png","player/Idle .png"]


#data
pspeed = 6
player_x = 20
player_y = 450
jump = False
dead = False
player_vel_y = 0
gravity = 1

n1_rect = pygame.Rect(0,520,60,80)
n2_rect = pygame.Rect(60,520,60,80)
n3_rect = pygame.Rect(120,520,60,80)
n4_rect = pygame.Rect(180,520,60,80)

f1_rect = pygame.Rect(330,400,60,70)
f2_rect = pygame.Rect(390,400,60,70)
f3_rect = pygame.Rect(450,400,60,70)
f1_rect1 = pygame.Rect(530,200,60,70)
f2_rect2 = pygame.Rect(590,200,60,70)
f3_rect3 = pygame.Rect(650,200,60,70)



playing = True
while playing:
    facing_right = True
    fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= pspeed

        
    if keys[pygame.K_RIGHT]:
        player_x += pspeed
        
    
    if keys[pygame.K_UP] and not jump:
        player_vel_y -= 25 
        jump = True
    if jump == True:
        player = pygame.image.load(an[0])
        player = pygame.transform.scale(player,(60,70))
        

    player_vel_y += gravity
    player_y += player_vel_y
    player_rect = pygame.Rect(player_x, player_y, 60, 70)

    if player_rect.colliderect(n1_rect):
        if player_vel_y > 0:
           player_y = n1_rect.top - 70
           jump=False
           player_vel_y=0
           player = pygame.image.load(an[4])
           player = pygame.transform.scale(player,(60,70))
    if player_rect.colliderect(n2_rect):
        if player_vel_y > 0:
           player_y = n2_rect.top - 70
           jump=False
           player_vel_y=0
           player = pygame.image.load(an[4])
           player = pygame.transform.scale(player,(60,70))
    if player_rect.colliderect(n3_rect):
        if player_vel_y > 0:
           player_y = n3_rect.top - 70
           jump=False
           player_vel_y=0
           player = pygame.image.load(an[4])
           player = pygame.transform.scale(player,(60,70))
    if player_rect.colliderect(n4_rect):
        if player_vel_y > 0:
           player_y = n4_rect.top - 70
           jump=False
           player_vel_y=0  
           player = pygame.image.load(an[4])
           player = pygame.transform.scale(player,(60,70))

    if player_rect.colliderect(f1_rect):
        if player_vel_y > 0:
           player_y = f1_rect.top - 70
           jump=False
           player_vel_y=0
           player = pygame.image.load(an[4])
        player = pygame.transform.scale(player,(60,70))
    if player_rect.colliderect(f2_rect):
        if player_vel_y > 0:
           player_y = f2_rect.top - 70
           jump=False
           player_vel_y=0
           player = pygame.image.load(an[4])
        player = pygame.transform.scale(player,(60,70))
    if player_rect.colliderect(f3_rect):
        if player_vel_y > 0:
           player_y = f3_rect.top - 70
           jump=False
           player_vel_y=0
           player = pygame.image.load(an[4])
        player = pygame.transform.scale(player,(60,70))
    if player_rect.colliderect(f1_rect1):
        if player_vel_y > 0:
           player_y = f1_rect1.top - 70
           jump=False
           player_vel_y=0     
           player = pygame.image.load(an[4])
        player = pygame.transform.scale(player,(60,70))
    if player_rect.colliderect(f2_rect2):
        if player_vel_y > 0:
           player_y = f2_rect2.top - 70
           jump=False
           player_vel_y=0  
           player = pygame.image.load(an[4])
        player = pygame.transform.scale(player,(60,70))
    if player_rect.colliderect(f3_rect3):
        if player_vel_y > 0:
           player_y = f3_rect3.top - 70
           jump=False
           player_vel_y=0   
           player = pygame.image.load(an[4])
        player = pygame.transform.scale(player,(60,70))               
    if player_y >=800:
        player_y=10
        player_x=10

       
    if player_x < 0: 
        player_x = 0
    if player_x > 790: 
        player_x = 790   
      
    screen.blit(bg, (0, 0)) 
    screen.blit(n1,(0,520))
    screen.blit(n2,(60,520)) 
    screen.blit(n3,(120,520)) 
    screen.blit(n4,(180,520))
    
    screen.blit(f1,(300,400))
    screen.blit(f2,(360,400)) 
    screen.blit(f3,(420,400))
    screen.blit(f1,(500,200))
    screen.blit(f2,(560,200)) 
    screen.blit(f3,(620,200))

    screen.blit(player,(player_x,player_y))        

    
    pygame.display.flip() 

pygame.quit()
sys.exit()           
