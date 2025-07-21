import pygame
import os
import pygame.image

TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
GUITARRA = pygame.image.load(os.path.join(IMG_DIR, 'Other/guitar.png'))
GUITARRA_TYPE = "guitarra"

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))

START_BUTTON = pygame.image.load(os.path.join(IMG_DIR, 'Other/start.png'))

DINO_ROCK = pygame.image.load(os.path.join(IMG_DIR, 'Other/dinoRock.png'))

RUNNING_ROCK = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Dino/dinoRock1.png")), (110, 120)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Dino/dinoRock2.png")), (110, 120)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Dino/dinoRock3.png")), (110, 120)),
]
JUMPING_ROCK = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Dino/dinoRock1.png')), (110, 120))

DINO_ROCK_STATIC = pygame.image.load(os.path.join(IMG_DIR, 'Other/dinoRock.png'))

DUCKING_ROCK = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Dino/dinoRockDuck1.png")), (110, 120)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Dino/dinoRockDuck2.png")), (110, 120)),
]

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
