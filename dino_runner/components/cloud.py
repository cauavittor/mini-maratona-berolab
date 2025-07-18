import random
from dino_runner.utils.constants import CLOUD


class Cloud():

 def __init__(self):
  self.image = CLOUD
  self.rect = self.image.get_rect()
  self.rect.x = random.randint(1100, 1500)  # Posição inicial aleatória
  self.rect.y = random.randint(50, 200)      # Altura mais variada
  self.speed = random.randint(3, 7)          # Velocidade aleatória

 def update(self):
   self.rect.x -= self.speed
   if self.rect.x < -self.rect.width:
    self.rect.x = random.randint(1100, 1500)  # Nova posição aleatória
    self.rect.y = random.randint(50, 200)      # Nova altura aleatória
    self.speed = random.randint(3, 7)          # Nova velocidade aleatória

 def draw(self, screen): 
   screen.blit(self.image, self.rect) 