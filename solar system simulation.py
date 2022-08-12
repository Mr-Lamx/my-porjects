import pygame 
import math
from pygame.locals import * 

#importing the modules I will be using 

def set_text(string, coordx, coordy, fontSize): #Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(255, 255, 255) is white, to make white text
    text = font.render(string, True, (255, 255, 255)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect) 

pygame.init()

x = 350
y = 350
x2 = 200
y2 = 200
x3 = 150
y3 = 150
x4 = 450
y4 = 450
x5 = 550
y5 = 550
x6 = 700
y6 = 700

#math shit

angle = 0
angle2 = 0
angle3 = 0
angle4 = 0
angle5 = 0
angle6 = 0

#alot of math nerd shit

win = pygame.display.set_mode((1500, 1500))

run = True
while run:
    
    win.fill((0, 0, 0))
    
    #removing the old frame to draw a new one 
    
    mars =  pygame.draw.circle(win, (255, 0, 0), (x4*math.cos(angle4)+750, y4*math.sin(angle4)+750), 5, 0)
    venus =  pygame.draw.circle(win, (255, 150, 0), (x2*math.cos(angle2)+750, y2*math.sin(angle2)+750), 10, 0)
    mercury =  pygame.draw.circle(win, (200, 200, 200), (x3*math.cos(angle3)+750, y3*math.sin(angle3)+750), 10, 0)
    earth =  pygame.draw.circle(win, (0, 0, 255), (x*math.cos(angle)+750, y*math.sin(angle)+750), 10, 0)
    jupiter =  pygame.draw.circle(win, (255, 255, 200), (x5*math.cos(angle5)+750, y5*math.sin(angle5)+750), 30, 0)
    saturn =  pygame.draw.circle(win, (255, 255, 200), (x6*math.cos(angle6)+750, y6*math.sin(angle6)+750), 20, 0)
    saturn =  pygame.draw.circle(win, (255, 255, 200), (x6*math.cos(angle6)+750, y6*math.sin(angle6)+750), 33, 5)
    
    sun =  pygame.draw.circle(win, (255, 100, 0),(750, 750), 60, 0)
    
    #drawing the planets 
    #and also lots and lots of math 
    #im losing brain cells and im only 50 lines in 
    
    totalText = set_text( 'x: ' + str(round(x*math.cos(angle)+750)) +' y: ' + str(round(y*math.sin(angle)+750)), x*math.cos(angle)+750+16, y*math.sin(angle)+750-50, 20)
    win.blit(totalText[0], totalText[1])
    
    
    totalText1 = set_text( 'x: ' + str(round(x2*math.cos(angle2)+750)) +' y: ' + str(round(y2*math.sin(angle2)+750)), x2*math.cos(angle2)+750+16, y2*math.sin(angle2)+750-50, 20)
    win.blit(totalText1[0], totalText1[1])
    
    
    
    totalText2 = set_text( 'x: ' + str(round(x3*math.cos(angle3)+750)) +' y: ' + str(round(y3*math.sin(angle3)+750)), x3*math.cos(angle3)+750+16, y3*math.sin(angle3)+750-50, 20)
    win.blit(totalText2[0], totalText2[1])
    
    totalText3 = set_text( 'x: ' + str(round(x4*math.cos(angle4)+750)) +' y: ' + str(round(y4*math.sin(angle4)+750)), x4*math.cos(angle4)+750+16, y4*math.sin(angle4)+750-50, 20)
    win.blit(totalText3[0], totalText3[1])
    
    
    totalText = set_text( 'x: ' + str(round(x5*math.cos(angle5)+750)) +' y: ' + str(round(y5*math.sin(angle5)+750)), x5*math.cos(angle5)+750+16, y5*math.sin(angle5)+750-50, 20)
    win.blit(totalText[0], totalText[1])
    
    totalText = set_text( 'x: ' + str(round(x6*math.cos(angle6)+750)) +' y: ' + str(round(y6*math.sin(angle6)+750)), x6*math.cos(angle6)+750+16, y6*math.sin(angle6)+750-50, 20)
    win.blit(totalText[0], totalText[1])
    #drawing the coardinantes next to their respective planets with you guessed it lots and lots of math
    
    
    
    
    #writting the names of the planets onder them
    totalText = set_text('Earth', x*math.cos(angle)+750, y*math.sin(angle)+750+50, 20)
    win.blit(totalText[0], totalText[1])
    
    totalText = set_text('Venus', x2*math.cos(angle2)+750, y2*math.sin(angle2)+750+50, 20)
    win.blit(totalText[0], totalText[1])
    
    totalText = set_text('Mercury', x3*math.cos(angle3)+750, y3*math.sin(angle3)+750+50, 20)
    win.blit(totalText[0], totalText[1])
    
    totalText = set_text('Mars', x4*math.cos(angle4)+750, y4*math.sin(angle4)+750+50, 20)
    win.blit(totalText[0], totalText[1])
    
    totalText = set_text('Jupiter', x5*math.cos(angle5)+750, y5*math.sin(angle5)+750+50, 20)
    win.blit(totalText[0], totalText[1])
    
    totalText = set_text('Saturn', x6*math.cos(angle6)+750, y6*math.sin(angle6)+750+50, 20)
    win.blit(totalText[0], totalText[1])
    
    
    
    
     #updating the frame
    pygame.display.update()
    a = 4
    angle5 += 0.0005 * a
    angle4 += 0.00075 * a
    angle += 0.001 * a
    angle2 += 0.002 * a
    angle3 += 0.003 * a
    angle6 += 0.0004 * a
    #some math stuff
    
    
    
    for event in pygame.event.get():  
          
        if event.type == pygame.QUIT:
            
            run = False
            
            #this will make sure to close the app when you click to exit but it has so FUCKING PURPOSE NOW BECAUSE THE APP IS SO BIG IT COVERS THE WHOLE SCREEN AND THE EXIT BUTTON IS GONE NOW FOR SOME REASON
            
            
# that is baisically it the math may look like rocket science because ITS LITERAL FUCKING ORBITAL DYNAMICS           
            
