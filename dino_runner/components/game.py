import pygame
from dino_runner.components import dinossaur
from dino_runner.utils import constants

class Game():
 
 def __init__(self):
  pygame.init()

  self.x_pos_bg = 0
  self.game_speed = 10
  
  self.TITLE = constants.TITLE
  self.HEIGHT = constants.SCREEN_HEIGHT
  self.WIDTH = constants.SCREEN_WIDTH
  
  self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
  pygame.display.set_caption(self.TITLE)
  
  self.clock = pygame.time.Clock()

  self.dino = dinossaur.Dino()

  self.bg_color = (255, 255, 255)
  
  self.track = constants.BG

 def execute(self):
   self.run = True

   while self.run:
    self.handle_commands()
    self.draw()
    self.update()
    self.clock.tick(60)
    
   pygame.quit()
 
 
 def handle_commands(self):
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    self.run = False

 def update(self):
   user_input = pygame.key.get_pressed()
   self.dino.update(user_input)


 def draw(self):

  self.screen.fill(self.bg_color)
  self.x_pos_bg -= self.game_speed

  if self.x_pos_bg <= -self.track.get_width():
   self.x_pos_bg = 0
  

  self.screen.blit(self.track, (self.x_pos_bg, 300))
  self.screen.blit(self.track, (self.x_pos_bg + self.track.get_width(), 300))

  self.dino.draw(self.screen)
  pygame.display.update()



