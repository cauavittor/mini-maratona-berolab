import pygame
from dino_runner.components import dinossaur
from dino_runner.utils import constants
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird
import random
from dino_runner.components.cloud import Cloud
from dino_runner.components.powerups.hammer import Hammer
import os

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

  # Highscore
  self.highscore_file = 'highscore.txt'
  self.highscore = self.load_highscore()

  # Martelo
  self.hammer_active = False
  self.hammer_end_time = 0

  # Game over state
  self.game_over = False
  self.game_over_font = pygame.font.Font(None, 80)
  self.button_font = pygame.font.Font(None, 50)
  
  # Reset button properties
  self.reset_button_width = 80
  self.reset_button_height = 80
  self.reset_button_x = self.WIDTH // 2 - self.reset_button_width // 2
  self.reset_button_y = self.HEIGHT // 2 + 50

  # Controle de ondas de obstáculos
  self.wave_mode = False
  self.wave_start_time = 0
  self.wave_duration = 4000  # 4 segundos de onda
  self.wave_interval = 6000  # 6 segundos de calmaria
  self.last_wave_switch = pygame.time.get_ticks()

  # Sistema de sons simples
  self.sounds = {}
  self.sounds_enabled = True
  self.game_started = False

 def load_highscore(self):
  if os.path.exists(self.highscore_file):
   with open(self.highscore_file, 'r') as f:
    try:
     return int(f.read())
    except Exception:
     return 0
  return 0

 def setup_sounds(self, sound_paths):
  """Configura os sons do jogo com os caminhos fornecidos"""
  pygame.mixer.init()
  
  # Carrega apenas os três sons disponíveis
  sound_files = {
    'jump': sound_paths.get('jump', ''),
    'death': sound_paths.get('death', ''),
    'score': sound_paths.get('score', '')
  }
  
  # Carrega os sons
  for sound_name, file_path in sound_files.items():
    if file_path and os.path.exists(file_path):
      try:
        self.sounds[sound_name] = pygame.mixer.Sound(file_path)
        self.sounds[sound_name].set_volume(0.7)
        print(f"✅ Som carregado: {sound_name}")
      except pygame.error as e:
        print(f"❌ Erro ao carregar {sound_name}: {e}")
    else:
      print(f"⚠️ Arquivo não encontrado: {file_path}")

 def play_sound(self, sound_name):
  """Reproduz um efeito sonoro"""
  if not self.sounds_enabled or sound_name not in self.sounds:
    return
  try:
    self.sounds[sound_name].play()
  except:
    pass



 def save_highscore(self):
  with open(self.highscore_file, 'w') as f:
   f.write(str(self.highscore))

 def reset_game(self):
  """Reset the game state to start a new game"""
  self.game_over = False
  self.score = 0
  self.game_speed = 10
  self.x_pos_bg = 0
  self.obstacles = []
  self.power_ups = []
  self.dino = dinossaur.Dino()
  # clouds
  self.clouds = []
  for i in range(3):
   cloud = Cloud()
   cloud.rect.x = 1100 + (i * 300)
   self.clouds.append(cloud)
  self.last_score_update = pygame.time.get_ticks()
  self.last_speed_increase_time = pygame.time.get_ticks()
  self.hammer_active = False
  self.hammer_end_time = 0
  
  # Reinicia o jogo
  self.game_started = True

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
   
   if event.type == pygame.KEYDOWN:
    # Controles de som
    if event.key == pygame.K_s:  # S para sons
     self.sounds_enabled = not self.sounds_enabled
   
   if event.type == pygame.USEREVENT:
    # Eventos customizados
    if event.dict.get('action') == 'jump':
     self.play_sound('jump')
   
   if event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
    mouse_pos = pygame.mouse.get_pos()
    reset_button_rect = pygame.Rect(self.reset_button_x, self.reset_button_y, self.reset_button_width, self.reset_button_height)
    
    if reset_button_rect.collidepoint(mouse_pos):
     self.reset_game()

 def get_difficulty_settings(self):
    if self.score < 500:
      return {
        'max_obstacles': 1,
        'min_distance': 1000,
        'game_speed': 10
      }
    elif self.score < 2000:
      return {
        'max_obstacles': 2,
        'min_distance': 700,
        'game_speed': 13
      }
    else:
      return {
        'max_obstacles': 3,
        'min_distance': 500,
        'game_speed': 18
      }

 def update(self):
    if self.game_over:
     return

    # Marca o jogo como iniciado
    if not self.game_started:
     self.game_started = True

    user_input = pygame.key.get_pressed()
    self.dino.update(user_input)

    # Alterna entre onda e calmaria
    now = pygame.time.get_ticks()
    if self.wave_mode:
      if now - self.wave_start_time > self.wave_duration:
        self.wave_mode = False
        self.last_wave_switch = now
    else:
      if now - self.last_wave_switch > self.wave_interval:
        self.wave_mode = True
        self.wave_start_time = now

    # Níveis de dificuldade
    settings = self.get_difficulty_settings()
    self.game_speed = settings['game_speed']
    max_obstacles = settings['max_obstacles']
    min_distance = settings['min_distance']

    def pode_adicionar_obstaculo():
      return all(ob.rect.x < self.WIDTH - min_distance for ob in self.obstacles)

    # Geração de obstáculos baseada no nível
    if len(self.obstacles) < max_obstacles:
      if len(self.obstacles) == 0 or pode_adicionar_obstaculo():
        obstacle_choice = random.randint(0, 9)
        if obstacle_choice < 5:
          self.obstacles.append(SmallCactus())
        elif obstacle_choice < 9:
          self.obstacles.append(LargeCactus())
        else:
          self.obstacles.append(Bird())

    # Martelo aparece com menos frequência
    if len(self.power_ups) == 0 and random.randint(0, 1000) < 1:
        self.power_ups.append(Hammer())    

    current_time = pygame.time.get_ticks()

    if current_time - self.last_score_update < 30000:  # Aumentado para 30000ms (30 segundos)
     pygame.time.delay(20)
     self.score += 1
     self.last_score_update = current_time 
     

     if self.score % 100 == 0:
        if current_time - self.last_speed_increase_time >= 1000:
          self.game_speed += 1
          self.last_speed_increase_time = current_time
          self.play_sound('score')  # Som de pontuação

    # Atualiza highscore
    if self.score > self.highscore:
     self.highscore = self.score
     self.save_highscore()

    # Efeito do martelo: dinossauro pode destruir obstáculos ao colidir
    if self.hammer_active:
     if pygame.time.get_ticks() >= self.hammer_end_time:
      self.hammer_active = False

    for obstacle in self.obstacles[:]:  # Usar cópia da lista para evitar erro ao remover
     obstacle.update(self.game_speed, self.obstacles) 
     if self.dino.rect.colliderect(obstacle.rect):
      if self.hammer_active:
       # Dinossauro com martelo destrói o obstáculo
       self.obstacles.remove(obstacle)
      else:
       # Dinossauro sem martelo morre
       self.play_sound('death')
       self.game_over = True
       return
      
    for power_up in self.power_ups:
      power_up.update(self.game_speed, self.power_ups)
      if self.dino.rect.colliderect(power_up.rect):
        if power_up.type == "hammer":
         self.hammer_active = True
         self.hammer_end_time = pygame.time.get_ticks() + 4000
         self.dino.activate_hammer_power()
         self.power_ups.remove(power_up)
         continue
        self.dino.activate_hammer_power()
        self.power_ups.remove(power_up)

    for cloud in self.clouds: 
      cloud.update()  

 def draw_game_over_screen(self):
   """Draw the game over screen with restart button"""
   # Semi-transparent overlay
   overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
   overlay.set_alpha(128)
   overlay.fill((0, 0, 0))
   self.screen.blit(overlay, (0, 0))
   
   # Game Over image
   game_over_img = constants.GAME_OVER
   img_rect = game_over_img.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 - 100))
   self.screen.blit(game_over_img, img_rect)
   
   # Final score
   final_score_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))
   score_rect = final_score_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 - 30))
   self.screen.blit(final_score_text, score_rect)
   
   # Reset button (using Reset.png image)
   mouse_pos = pygame.mouse.get_pos()
   reset_button_rect = pygame.Rect(self.reset_button_x, self.reset_button_y, self.reset_button_width, self.reset_button_height)
   
   reset_img = constants.RESET
   reset_img_rect = reset_img.get_rect(center=(self.reset_button_x + self.reset_button_width // 2, self.reset_button_y + self.reset_button_height // 2))
   self.screen.blit(reset_img, reset_img_rect)

 def draw_start_screen(self):
        overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((255, 255, 255))
        self.screen.blit(overlay, (0, 0))
        start_img = constants.START_BUTTON
        img_rect = start_img.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(start_img, img_rect)
        # Mensagem opcional
        font = pygame.font.Font(None, 40)
        text = font.render('Clique ou pressione qualquer tecla para começar', True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 100))
        self.screen.blit(text, text_rect)

 def draw(self):
  self.screen.fill(self.bg_color)
  for cloud in self.clouds:
    cloud.draw(self.screen)
  self.x_pos_bg -= self.game_speed

  if self.x_pos_bg <= -self.track.get_width():
   self.x_pos_bg = 0
  
  self.screen.blit(self.track, (self.x_pos_bg, 300))
  self.screen.blit(self.track, (self.x_pos_bg + self.track.get_width(), 300))

  if not self.game_started:
    self.draw_start_screen()
  else:
    self.dino.draw(self.screen)
    for obstacle in self.obstacles:
      obstacle.draw(self.screen)
    for power_up in self.power_ups:
      power_up.draw(self.screen)
    score_text =  self.font.render(f'Score: {self.score}', True, (0, 0, 0))
    self.screen.blit(score_text, (600, 50))
    highscore_text = self.font.render(f'Recorde: {self.highscore}', True, (0, 0, 0))
    self.screen.blit(highscore_text, (600, 90))
    # Informações de controle de som
    sound_info_font = pygame.font.Font(None, 25)
    sound_info = sound_info_font.render('S: Liga/Desliga Sons', True, (100, 100, 100))
    self.screen.blit(sound_info, (10, 10))
    # Draw game over screen if game is over
    if self.game_over:
      self.draw_game_over_screen()
  pygame.display.update() 