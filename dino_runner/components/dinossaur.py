from dino_runner.utils.constants import  RUNNING, ICON, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, DUCKING, DUCKING_HAMMER, DUCKING_SHIELD, DEFAULT_TYPE, SHIELD_TYPE, RUNNING_SHIELD, RUNNING_HAMMER
import os
import pygame



class Dino(pygame.sprite.Sprite):
  X_POS = 80
  Y_POS = 220
  Y_POS_DUCK = 290



  def __init__(self):
    super().__init__()

    self.type = DEFAULT_TYPE
    self.image = RUNNING[0]
    self.rect = self.image.get_rect()
    self.rect.x = self.X_POS
    self.rect.y = self.Y_POS
    self.is_jumping = False
    self.is_running = True
    self.is_duck = False
    self.step_index = 0
    self.jump_velocity = 10
    self.has_power_up = False
    self.power_up_time = 0



    self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 5, self.rect.width - 20, self.rect.height - 10)


  def update_hitbox(self):  
  
    self.hitbox.x = self.rect.x + 10      
    self.hitbox.y = self.rect.y + 5


  def draw(self, screen):
    screen.blit(self.image, self.rect)


  def update(self, user_input):

    if self.is_jumping:
      self.jump()
    elif self.is_duck:
      self.duck()
    else:
      self.run()
  
    

    if user_input[pygame.K_SPACE] or user_input[pygame.K_UP] and not self.is_jumping:
      self.is_jumping = True
      self.is_duck = False
      self.is_running = False
      self.rect.y = self.Y_POS

    if user_input[pygame.K_DOWN] and not self.is_duck:
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

    if self.type == SHIELD_TYPE:
      self.image = RUNNING_SHIELD[self.step_index // 5]
    elif self.type == RUNNING_HAMMER:     
      [self.step_index // 5]  
    else: 
      self.image = RUNNING[self.step_index // 5] 

    self.image = RUNNING[self.step_index // 5]
    self.rect.x = self.X_POS
    self.rect.y = self.Y_POS
    self.step_index += 1

  def jump(self):
    if self.type == SHIELD_TYPE:
        self.image = JUMPING_SHIELD
    elif self.type == "hammer":
        self.image = JUMPING_HAMMER
    else:
        self.image = JUMPING

    self.image = JUMPING
    self.rect.y -= self.jump_velocity * 4.2
    self.jump_velocity -= 0.9

    if self.jump_velocity < -10:
      self.rect.y = self.Y_POS
      self.is_jumping = False
      self.jump_velocity = 10


  def duck(self):

    if self.type == SHIELD_TYPE:
        self.image = DUCKING_SHIELD[self.step_index // 5]
    elif self.type == "hammer":
        self.image = DUCKING_HAMMER[self.step_index // 5]
    else:
        self.image = DUCKING[self.step_index // 5]
    self.image = DUCKING[self.step_index // 5]
    self.rect.x = self.X_POS
    self.rect.y = self.Y_POS_DUCK
    self.step_index += 1
    
  def activate_hammer_power(self):
    self.has_power_up = True
    self.type = "hammer"
    self.power_up_time = pygame.time.get_ticks() + 5000 










  
