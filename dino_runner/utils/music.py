import pygame
from dino_runner.utils.constants import *


def music():
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load(MARIO_TRACK)
    pygame.mixer.music.play(-1)


def sound(self):
    sound = pygame.mixer.Sound(self)
    sound.set_volume(0.5)
    sound.play()
