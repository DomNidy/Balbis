import pygame
import pygame,sys
import random

pygame.display.init()
pygame.font.init()
screen_width=1600
screen_height=900
screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Turnaments")

class Character:
      x = 50
      y = 50
      width = 40
      height = 60
      vel = 0.3
      area = x * y

class Border:
      x = 50
      y = 50
      width = 30
      height = 60
      area = x * y

class AllObjects(Character, Border):
      pass

run = True
while run:
      pygame.time.delay(1)

      for event in pygame.event.get():
            #Quits Game
            if event.type == pygame.QUIT:
                  run = False
                  
      keys = pygame.key.get_pressed()

      if keys[pygame.K_LEFT]:
                  Character.x -= Character.vel
                  Character.width += 0.1
                  Character.height += 0.1
      if keys[pygame.K_RIGHT]:
                  Character.x += Character.vel
                  Character.width += 0.1
                  Character.height += 0.1
      if keys[pygame.K_UP]:
                  Character.y -= Character.vel
                  Character.width += 0.1
                  Character.height += 0.1
      if keys[pygame.K_DOWN]:
                  Character.y += Character.vel
                  Character.width += 0.1
                  Character.height += 0.1
      
      Character.area = Character.width * Character.height            
      print("Characters Area: " + str(Character.area))
      
                  
      screen.fill((0, 0, 0))
      pygame.draw.rect(screen, (0, 0, 255), (Character.x, Character.y, Character.width, Character.height))
      pygame.draw.rect(screen, (255, 0 ,0), (Border.x, Border.y, Border.width, Border.height))
      pygame.display.update()

pygame.quit()
#End                 
            
      
            
