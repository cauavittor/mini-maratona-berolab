import pygame

class Obstacle(pygame.sprite.Sprite):
  
 def __init__(self, image_list, type):
   super().__init__()
   self.image_list = image_list
   self.type = type
   self.image = image_list[type]
   self.rect = self.image.get_rect()
   self.rect.x = 1000

   side_margin = 10
   self.hitbox = pygame.Rect(
     self.rect.x + side_margin,
    self.rect.y,
    self.rect.width - 2 * side_margin,
    self.rect.height)

 def update(self, game_speed, obstacles):
  self.rect.x -= game_speed
  self.hitbox.x = self.rect.x + 10 
  if self.rect.x < -self.rect.width:
   obstacles.remove(self)

 def draw(self, screen):
  screen.blit(self.image, self.rect)   
