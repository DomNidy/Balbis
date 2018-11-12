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
      width = 10
      height = 10
      vel = 0.3
      area = width * height
      max_area = 1000000
      score = (max_area - area) /1000

class Border:
      x = 800
      y = 500
      width = 30
      height = 60
      area = x * y

class FinishLine:
      x = 1500
      y = 0
      width = 10
      height = 1600

zoom_data = [Character.width, Character.height, Border.width, Border.height]

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
      if keys[pygame.K_TAB]:
            for i in zoom_data:
                  i += 100
            
      
      Character.area = Character.width * Character.height            
      if keys[pygame.K_TAB]:


            print("Characters Area: " + str(Character.area))
            
      Character.score = (Character.max_area - Character.area * 2) / 1000
      if keys[pygame.K_EQUALS]:
            print("Score: " + str(Character.score))

      if round(Character.x) == FinishLine.x:
            pygame.quit()
      
                  
      screen.fill((0, 0, 0))
      pygame.draw.rect(screen, (0, 0, 255), (Character.x, Character.y, Character.width, Character.height))
      pygame.draw.rect(screen, (255, 0 ,0), (Border.x, Border.y, Border.width, Border.height))
      pygame.draw.rect(screen, (25, 100, 93), (FinishLine.x, FinishLine.y, FinishLine.width, FinishLine.height))
      pygame.display.update()

pygame.quit()
#End                 
            
      
            
