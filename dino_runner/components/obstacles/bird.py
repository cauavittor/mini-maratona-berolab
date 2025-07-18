from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle
import random


class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = random.choice([120, 150, 180, 210, 240, 260])  # Alturas seguras, nunca abaixo da estrada
        self.step_index = 0

    def draw(self, screen):
        self.image = self.image_list[self.step_index // 5]
        screen.blit(self.image, self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0

