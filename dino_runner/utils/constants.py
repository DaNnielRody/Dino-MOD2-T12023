import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

FONT_STYLE = "./font/8-BIT WONDER.TTF"
BLACK_COLOR = (0,0,0)
WHITE_COLOR = (255, 255, 255)
GRAY_COLOR = (122, 122, 122)

# Assets Constants
ICON = pygame.image.load(os.path.join(ASSETS_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun2Hammer1.png")),
]

JUMPING = pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoJump.png"))

JUMPING_SHIELD = pygame.image.load(
    os.path.join(ASSETS_DIR, "Dino/DinoJumpShield.png"))

JUMPING_HAMMER = pygame.image.load(
    os.path.join(ASSETS_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck2Hammer.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Bird/Bird2.png")),
]

BUTTONS = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Button/button_audio.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Button/button_back.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Button/button_keys.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Button/button_options.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Button/button_quit.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Button/button_resume.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Button/button_video.png")),
]

CLOUD = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/hammer.png'))
HEART = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/Heart.png'))

BG = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/Track.png'))

GAME_OVER = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/GameOver.png'))
DEAD = pygame.image.load(os.path.join(ASSETS_DIR, 'Dino/DinoDead.png'))

MARIO_TRACK = os.path.join(ASSETS_DIR, "Other/music_mario.wav")
DEATH_SOUND = os.path.join(ASSETS_DIR, "Other/mario_death.wav")
JUMP_SOUND = os.path.join(ASSETS_DIR, "Other/mario_jump.wav")
SCORE_SOUND = os.path.join(ASSETS_DIR, "Other/sons_score_sound.wav")

MAIN_STATE = 'main'
OPT_STATE = 'options'

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
HEART_TYPE = "life"
