from dino_runner.utils.constants import  RUNNING, ICON, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, DUCKING, DUCKING_HAMMER, DUCKING_SHIELD
import os
import pygame



class Dino(pygame.sprite.Sprite):
 X_POS = 80
 Y_POS = 220
 Y_POS_DUCK = 290

 def __init__(self):
  
  self.image = RUNNING[0]
  self.rect = self.image.get_rect()
  self.rect.x = self.X_POS
  self.rect.y = self.Y_POS
  self.is_jumping = False
  self.is_running = True
  self.is_duck = False
  self.step_index = 0
  self.jump_velocity = 8.5


 def draw(self, screen):
  
  screen.blit(self.image, self.rect)


 def update(self, user_input):

  if self.is_jumping:
   self.jump()
  elif self.is_duck:
   self.duck()
  else:
   self.run()
  
    

  if user_input[pygame.K_SPACE] or user_input[pygame.K_UP]:
   if not self.is_jumping:
    self.is_jumping = True
    self.is_duck = False
    self.is_running = False

  if user_input[pygame.K_DOWN]: 
   if not self.is_duck:
    self.is_duck = True 
    self.is_jumping  = False
    self.is_running = False
  elif not user_input[pygame.K_DOWN] and not self.is_jumping: 
    self.is_running = True
    self.is_duck = False
    self.is_jumping = False

  
  if self.step_index >= 10:
   self.step_index = 0

 def run(self):  

  self.image = RUNNING[self.step_index // 5]
  self.rect.x = self.X_POS
  self.rect.y = self.Y_POS
  self.step_index += 1

 def jump(self):
  self.image = JUMPING
  self.rect.y -= self.jump_velocity * 4
  self.jump_velocity -= 0.8

  if self.jump_velocity < -8.5:
   self.rect.y = self.Y_POS
   self.is_jumping = False
   self.jump_velocity = 8.5


 def duck(self):
  self.image = DUCKING[self.step_index // 5]
  self.rect.x = self.X_POS
  self.rect.y = self.Y_POS_DUCK
  self.step_index += 1












  
