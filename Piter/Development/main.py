import sys
import pygame
from pygame.locals import *

# Necessary setup before you can start using pygame functionalities:
pygame.init()


KEYS_DOWN = []

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

CLOCK   = pygame.time.Clock()
FPS     = 30

BG_COLOUR = [0, 0, 0]
IS_RUNNING = True

class Player:
    _lives = 3
    _points = 0
    _speed = 5
    _playerSprite = ""
    _playerRect = ""

    def __init__(self, surfaceSpriteLink = "../Art/textureNotFound.png"):
        self._playerSprite = pygame.image.load(surfaceSpriteLink)
        self._playerRect = self._playerSprite.get_rect()

    def Update(self):
        KEYS_DOWN = pygame.key.get_pressed()
        if (KEYS_DOWN[K_UP]):
            self._playerRect.y -= self._speed
        elif (KEYS_DOWN[K_DOWN]):
            self._playerRect.y += self._speed
        if (KEYS_DOWN[K_LEFT]):
            self._playerRect.x-= self._speed
        elif (KEYS_DOWN[K_RIGHT]):
            self._playerRect.x += self._speed

    def Draw(self):
        SCREEN.fill(BG_COLOUR)
        SCREEN.blit(self._playerSprite, self._playerRect)
        pygame.display.flip()
        CLOCK.tick(FPS)

Player1 = Player("../Art/spr_Player.png")


while IS_RUNNING:
    # ------------------------------------------------
    # EVENT HANDLING:
    # ------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False
    # ------------------------------------------------
    # UPDATE GAME LOGIC:
    # ------------------------------------------------
    Player1.Update()
    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    Player1.Draw()
