import pygame
import pygame,sys
import random

pygame.display.init()
screen_width=1600
screen_height=900
screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Turnaments")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
      pygame.time.delay(100)

      for event in pygame.event.get():
            #Quits Game
            if event.type == pygame.QUIT:
                  run = False
                  
      keys = pygame.key.get_pressed()

      if keys[pygame.K_LEFT]:
                  x -= vel
      if keys[pygame.K_RIGHT]:
                  x += vel
      if keys[pygame.K_UP]:
                  y -= vel
      if keys[pygame.K_DOWN]:
                  y += vel

      screen.fill((0, 0, 0))
      pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))
      pygame.display.update()

pygame.quit()
#End                 
            
      
            
