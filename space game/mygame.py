import sys
import pygame
import math
from random import randint
pygame.init()

def set_text(string, coordx, coordy, fontSize): #Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(255, 255, 255) is white, to make white text
    text = font.render(string, True, (255, 255, 255)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect) 


player = pygame.image.load('player.png')
enemy = pygame.image.load('enemy.png')
enemy1 = pygame.image.load('enemy.png')
bg = pygame.image.load('bg.png')
boss = pygame.image.load('boss.png')
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("mygame")

menu = True
run = True

x = 400
y = 600

bulletx = x 
bullety = y

bulletradius = 0

enemyx = 100
enemyy = 0

enemyx1 = 100
enemyy1= 0

enemy = pygame.transform.rotate(enemy, 180)
enemy1 = pygame.transform.rotate(enemy1, 180)
boss = pygame.transform.rotate(boss, 180)


level = 0
bossx = randint(0, 800)
bossy = 0
health = 2
score = 0

image = pygame.image.load('bg.png')
image = pygame.transform.scale(image, (800, 800))
color = (63, 64, 63)
color2 = (63, 64, 63)

while menu:
    (mousex, mousey) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            menu = False
            run = False
            menu = False
           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
            menu = False  
            run = False
            menu = False    
            
    win.fill((0, 0, 0)) 
           
           
    play = pygame.draw.rect(win, color, pygame.Rect(300, 350, 200, 100),  0)
    quit = pygame.draw.rect(win, color2, pygame.Rect(300, 500, 200, 100),  0)     
    mouse =  pygame.draw.circle(win, (0, 0, 0), (mousex, mousey), 1, 0)   
    totalText1 = set_text( 'Play', 400, 400, 50)
    mouse =  pygame.draw.circle(win, (0, 0, 0), (mousex, mousey), 1, 0)   
    totalText = set_text( 'Quit', 400, 550, 50)
    win.blit(totalText[0], totalText[1])
    win.blit(totalText1[0], totalText1[1])    
    pygame.display.update()
    
    
    if mouse.colliderect(play):
        color = ((50, 50, 50))
    else:
        color = (63, 64, 63)
               
    if mouse.colliderect(quit):
            color2 = ((50, 50, 50))
    else:
        color2 = (63, 64, 63)          
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and mouse.colliderect(play):
            
            menu = False
        if event.type == pygame.MOUSEBUTTONDOWN and mouse.colliderect(quit):
            run = False
            menu = False
            
     
while run:
     
    #we have the main loop
    
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
   (mousex, mousey) = pygame.mouse.get_pos()
    
    
   #this code is going to detect if we press the exit button and will exit the program
            
   bg = pygame.transform.scale(enemy, (800, 800))
   enemy = pygame.transform.scale(enemy, (150, 150))
   enemy1 = pygame.transform.scale(enemy1, (150, 150))
   player = pygame.transform.scale(player, (200, 200))
   boss = pygame.transform.scale(boss, (200, 200))  
   
   #transforming the images so they can be the correct size and pointing in the right way  
             
   win.fill((0, 0, 0))
   
   #filling up the surface with black so we can put the new frame
   
   enemyrec1 = pygame.draw.rect(win, (0, 0, 0), pygame.Rect(enemyx1, enemyy1, 200, 200),  2)
   bossrec = pygame.draw.rect(win, (0, 0, 0), pygame.Rect(bossx, bossy, 200, 200),  2) 
   enemyrec = pygame.draw.rect(win, (0, 0, 0), pygame.Rect(enemyx, enemyy, 200, 200),  2)
   win.blit(image, (0, 0))
   
  
   
   bullet = pygame.draw.circle(win, (255, 0, 0), (bulletx, bullety), bulletradius, 0) 
    
   #drawing the new frame
        
   totalText = set_text( 'score: '+str(score), 730, 30, 30)
   win.blit(totalText[0], totalText[1])
   win.blit(player, (x, y))
   win.blit(enemy, (enemyx,enemyy))
   win.blit(enemy1, (enemyx1,enemyy1))

       
      
       
   #bliting the images to the surface
   if score == 69:
        print("69 NICE!!")
   if score == 106:
        print("106 NICE!!")
   if level >= 3:
        win.blit(boss, (bossx, bossy))     
        bossy += 6
   pygame.display.update()
   bullety -= 24
   enemyy += 1.8
   enemyy1 += 1.8
   
   
   if x >= 700:
        x = 700
   if x <= -100:
        x = -100     
   if pygame.key.get_pressed()[pygame.K_a]:
        x -= 8
   if pygame.key.get_pressed()[pygame.K_d]:
        x += 8
   if pygame.key.get_pressed()[pygame.K_SPACE]:
        bulletradius = 10
        bullety = y
        bulletx = x + 100
   if bullet.colliderect(enemyrec):
        enemyy = 0
        enemyx = randint(0, 725)
        level += 1
        score += 1
   if bullet.colliderect(enemyrec1):
        enemyy1 = 0
        enemyx1 = randint(0, 725)
        score += 1     
   if enemyy >= 800:
        
        run = False
        
   if enemyy1 >= 800:
        
        run = False
        while menu:
             
             
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False
                 menu = False
        (mousex, mousey) = pygame.mouse.get_pos()  
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False  
                 menu = False  
         
        
     
             
            
        
       
       
   
                         
   if x >= 800:
        x -= 2.5
   
   if bullet.colliderect(bossrec):
        health -= 1

   if health == 0:
        health = 2
        level = 0 
        bossy = 0   
        bossx = randint(0, 700)   
        score += 1  
        
menu = True
while menu:
    (mousex, mousey) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            menu = False
            run = False
            menu = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
            menu = False  
            run = False
            menu = False    
            
    win.fill((0, 0, 0)) 
           
           
    
    quit = pygame.draw.rect(win, color2, pygame.Rect(300, 500, 200, 100),  0)     
    mouse =  pygame.draw.circle(win, (0, 0, 0), (mousex, mousey), 1, 0)   
    totalText1 = set_text( 'you lost', 400, 400, 50)
    mouse =  pygame.draw.circle(win, (0, 0, 0), (mousex, mousey), 1, 0)   
    totalText = set_text( 'Quit', 400, 550, 50)
    win.blit(totalText[0], totalText[1])
    win.blit(totalText1[0], totalText1[1])    
    pygame.display.update()
    
    
    
               
    if mouse.colliderect(quit):
        color2 = ((50, 50, 50))
    else:
        color2 = (63, 64, 63)          
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN and mouse.colliderect(quit):
            run = False
            menu = False
         
    
    
    
    
    
        
# here we have all the if statments and logic of the game

# and that was pretty much it

# its a simple and very easy project that can be done in less than 30 minuts .

# i take my word back it isnt simple after adding the UI and other stuff it became a hellhole dont try it if you value your life or well being            
            
                        
                        
                   

            

