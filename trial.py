from turtle import circle
import pygame

pygame.init()

white = (255,255,255)
black =(0,0,0)
pink = (255,0,255)
red =(255,0,0)
green =(0,255,0)
blue = (0,0,255)


gameDisplay =pygame.display.set_mode((800,600))
gameDisplay.fill(black)


pixAr =pygame.PixelArray(gameDisplay)  #displaying pixels
pixAr [10][20] = green

pygame.draw.line(gameDisplay,blue,(300,200),(400,550),7)
pygame.draw.line(gameDisplay,green,(25,200),(400,550),7)
pygame.draw.line(gameDisplay,red,(25,200),(300,200),7)
pygame.draw.line(gameDisplay,white,(600,200),(300,200),7) 
pygame.draw.line(gameDisplay,pink,(310,700),(600,200),7) 




# pygame.draw.rect(gameDisplay,green,(400,400,100,50))       # specify the top left (x,y) then height and width
# pygame.draw.circle(gameDisplay,red,(150, 150),75) # specify the center of the circle and the radius
# pygame.draw.polygon(gameDisplay,white,((50,65),(76,125),(250,375),(400,25)))
  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
