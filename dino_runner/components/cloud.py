import random
from dino_runner.utils.constants import CLOUD


class Cloud():

 def __init__(self):
  self.image = CLOUD
  self.rect = self.image.get_rect()
  self.rect.x = 1100
  self.rect.y = random.randint(50, 100)
  self.speed = 5

 def update(self):
   self.rect.x -= self.speed
   if self.rect.x < -self.rect.width:
    self.rect.x = 1100
    self.rect.y = random.randint(50, 100)

 def draw(self, screen): 
   screen.blit(self.image, self.rect) 