import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle


class SmallCactus(Obstacle):
 def __init__(self):
    self.type = random.randint(0, 2)
    super().__init__(SMALL_CACTUS, self.type)
    self.rect.y = 300 - self.rect.height + 10
  


class LargeCactus(Obstacle):
  def __init__(self):
    self.type = random.randint(0, 2)
    super().__init__(LARGE_CACTUS, self.type)
    self.rect.y = 300 - self.rect.height + 10  