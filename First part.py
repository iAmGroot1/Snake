import pygame
import time
from random import randint

pygame.init()

#def display_setting():
 
dis_width=600
dis_height=600
X = dis_width/2
Y = dis_height/2
width = 10
height= 10
JUSTMOVER=False
JUSTMOVEL=False
MOVEX = 0
MOVEY = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FONT= pygame.font.SysFont(None,25)

clock= pygame.time.Clock()
win=pygame.display.set_mode((dis_width,dis_height))

def display_message(msg,colour):
     FONT= pygame.font.SysFont(None,25)
     text=FONT.render(msg,True,colour)
     win.blit(text,[dis_width/2,dis_height/2])



def Game():
     rect=pygame.image.load("block.jpg").convert()
     apple=pygame.image.load("block.jpg").convert()
     dis_width=600
     dis_height=600
     X = [0]
     Y = [0]
     APPLEX=dis_width-60
     APPLEY=dis_height-60
     LENGTH=3
     width = 10
     height= 10
     MOVEX = 30
     MOVEY = 0
     LIMITX=dis_width-MOVEX+5
     LIMITY=dis_height-MOVEX+5
     BLACK = (0, 0, 0)
     WHITE = (255, 255, 255)
     GREEN = (0, 255, 0)
     RED = (255, 0, 0)
     FONT= pygame.font.SysFont(None,25)

     for i in range(0,2000):
           X.append(-100)
           Y.append(-100)

     X[0]=dis_width/2  
     Y[0]=dis_height/2
     X[1]=dis_width/2-30
     Y[1]=dis_height/2
     Show(X,Y,LENGTH,MOVEX,MOVEY,rect,APPLEX,APPLEY,apple)
     run=True     
     while run :
          Show(X,Y,LENGTH,MOVEX,MOVEY,rect,APPLEX,APPLEY,apple)

          for event in pygame.event.get():
               if(event.type == pygame.QUIT):
                    run=False
          keys = pygame.key.get_pressed()
               
          if keys[pygame.K_RIGHT]:
               if MOVEX == 30 or MOVEX == 0  :
                    MOVEX=30
                    MOVEY=0
               else :
                    MOVEX=-30
                    MOVEY=0

          if keys[pygame.K_LEFT]: 
               if MOVEX == -30 or MOVEX == 0  :
                    MOVEX=-30
                    MOVEY=0
               else :
                    MOVEX=30
                    MOVEY=0

          if keys[pygame.K_DOWN]: 
               if MOVEY == 30 or MOVEY == 0  :
                    MOVEX=0 
                    MOVEY=30
               else :
                    MOVEX=0
                    MOVEY=-30
                    
          if keys[pygame.K_UP]:
               if MOVEY == -30 or MOVEY == 0  :
                    MOVEX=0
                    MOVEY=-30
               else :
                    MOVEX=0
                    MOVEY=30
                    
          if X[0]+MOVEX >LIMITX :
               X[0]=0
          elif X[0]-MOVEX < 0: 
               X[0]=dis_width
          elif Y[0]-MOVEY < 0:
               Y[0]=dis_height 
          elif Y[0]+MOVEY > LIMITY :
               Y[0]=0
          
          for i in range(2,LENGTH):
               if (X[0] >= X[i] and X[0] < X[i]+30) :
                    if (Y[0] >= Y[i] and Y[0] < Y[i]+30):
                         print(X[0],X[i])
                         display_message('YOU LOSE HERE',RED)
                         pygame.display.update()
                         pygame.time.delay(50)
                         quit()

          if(X[0]==APPLEX and Y[0]==APPLEY):
               LENGTH+=1
               APPLEX=randint(2,9)*(dis_width/10)
               APPLEY=randint(2,9)*(dis_height/10)

          clock.tick(90)
     pygame.quit()

def Show(X,Y,LENGTH,MOVEX,MOVEY,rect,APPLEX,APPLEY,apple) :
     win.fill(BLACK)
     for i in range(LENGTH-1,0,-1):
          X[i] = X[i-1]
          Y[i] = Y[i-1]

     X[0]+=MOVEX
     Y[0]+= MOVEY

     for i in range(0,LENGTH):
          win.blit(rect,(X[i],Y[i]))
     win.blit(apple,(APPLEX,APPLEY))

     pygame.time.delay(80)
     pygame.display.update()



Game()
