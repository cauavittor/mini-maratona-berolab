
import pygame
from dino_runner.utils.constants import GUITARRA, GUITARRA_TYPE
from .powerup import PowerUp

class Guitarra(PowerUp):
    def __init__(self):
        guitarra_img = pygame.transform.scale(GUITARRA, (52, 52))
        super().__init__(guitarra_img, GUITARRA_TYPE)
        self.rect.y = 250