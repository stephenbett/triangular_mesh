# from turtle import circle
import pygame

pygame.init()

white = (255,255,255)
black =(0,0,0)

red =(255,0,0)
green =(0,255,0)
blue = (0,0,255)


gameDisplay =pygame.display.set_mode((800,600))
gameDisplay.fill(black)


pygame.draw.line(gameDisplay,blue,(200,100),(600,550),7) 
# pygame.draw.line(gameDisplay,green,(150,100),(600,350),7) 
# pygame.draw.line(gameDisplay,blue,(200,100),(600,550),7) 


# pygame.draw.TRIANGLE(gameDisplay,green,0,6)