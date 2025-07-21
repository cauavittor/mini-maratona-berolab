import pygame

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, image, type):
        super().__init__()
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = 1100  
        self.rect.y = 250
        self.speed = 10     

    def update(self, game_speed, powerups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            powerups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)