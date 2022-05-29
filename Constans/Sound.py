import pygame
import os

pygame.mixer.init()

PAUSE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "mixkit-modern-technology-select-3124.mp3"))
GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join("Assets", "mixkit-little-piano-game-over-1944.mp3"))
ENTER_GAME_SOUND = pygame.mixer.Sound(os.path.join("Assets", "mixkit-video-game-mystery-alert-234.mp3"))
COLLIDE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "mixkit-cool-interface-click-tone-2568.mp3"))
BALL_SOUND = pygame.mixer.Sound(os.path.join("Assets", "mixkit-arcade-game-jump-coin-216.mp3"))
FEATURE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Collect Item sound effect.mp3"))
HOVER_SOUND = pygame.mixer.Sound(os.path.join("Assets", "UI Hover - Sound Effect (HD) .mp3"))