import pygame
from dino_runner.components import dinossaur
from dino_runner.utils import constants
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird
import random
from dino_runner.components.cloud import Cloud
from dino_runner.components.powerups.hammer import Hammer
class Game():
 
 def __init__(self):
  pygame.init()

  self.x_pos_bg = 0
  self.game_speed = 10
  self.last_score_update = 0
  self.last_speed_increase_time = pygame.time.get_ticks()
  self.clouds = [Cloud() for _ in range(3)]


  self.obstacles = []

  self.power_ups = []  
  self.last_hammer_spawn_time = 0  
  self.hammer_spawn_interval = 15000
  
  self.TITLE = constants.TITLE
  self.HEIGHT = constants.SCREEN_HEIGHT
  self.WIDTH = constants.SCREEN_WIDTH
  
  self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
  pygame.display.set_caption(self.TITLE)
  
  self.clock = pygame.time.Clock()

  self.dino = dinossaur.Dino()

  self.bg_color = (255, 255, 255)
  
  self.track = constants.BG

  self.score = 0
  self.font = pygame.font.Font(None, 40)
  self.last_score_update = pygame.time.get_ticks()


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

    if len(self.obstacles) == 0:
      obstacle_choice = random.randint(0, 2)
      if obstacle_choice == 0:
        self.obstacles.append(SmallCactus())
      if obstacle_choice == 1:
        self.obstacles.append(LargeCactus()) 
      if obstacle_choice == 2:
        self.obstacles.append(Bird())

    if len(self.power_ups) == 0 and random.randint(0, 1000) < 10:
        self.power_ups.append(Hammer())    


    current_time = pygame.time.get_ticks()

    if current_time - self.last_score_update < 1000: 
     pygame.time.delay(20)
     self.score += 1
     self.last_score_update = current_time 
     

     if self.score % 100 == 0:
        if current_time - self.last_speed_increase_time >= 1000:
          self.game_speed += 1
          self.last_speed_increase_time = current_time

    for obstacle in self.obstacles:
     obstacle.update(self.game_speed, self.obstacles) 
     if self.dino.rect.colliderect(obstacle.rect):
      pygame.time.delay(500)
      self.run = False
      
      
    for power_up in self.power_ups:
      power_up.update(self.game_speed, self.power_ups)
      if self.dino.rect.colliderect(power_up.rect):
        self.dino.activate_hammer_power()
        self.power_ups.remove(power_up)

    for cloud in self.clouds: 
      cloud.update()  

   
  


 def draw(self):

  self.screen.fill(self.bg_color)
  for cloud in self.clouds:
    cloud.draw(self.screen)
  self.x_pos_bg -= self.game_speed

  if self.x_pos_bg <= -self.track.get_width():
   self.x_pos_bg = 0
  

  self.screen.blit(self.track, (self.x_pos_bg, 300))
  self.screen.blit(self.track, (self.x_pos_bg + self.track.get_width(), 300))

  self.dino.draw(self.screen)

  for obstacle in self.obstacles:
   obstacle.draw(self.screen)

  score_text =  self.font.render(f'Score: {self.score}', True, (0, 0, 0))
  self.screen.blit(score_text, (600, 50))

  pygame.display.update()

  