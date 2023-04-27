# Imports
import pickle
import random
import time

import pygame
import sys
from pygame.locals import *

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 7
SCORE = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self._alpha = 0.1
        self._gamma = 0.9
        self._epsilon = 0.6
        self.qTable = [[[0 for _ in range(2)] for _ in range(600)] for _ in range(600)]

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 5:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH - 5:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def ai_step(self, ai_action):
        pressed_keys = ai_action

        if self.rect.left > 20:
            if pressed_keys == 0:
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH - 10:
            if pressed_keys == 1:
                self.rect.move_ip(10, 0)
        return self.rect.centerx

    def get_best_action(self, player_x, enemy_x):
        if self.qTable[player_x][enemy_x][0] == self.qTable[player_x][enemy_x][1]:
            return random.randrange(2)
        if self.qTable[player_x][enemy_x][0] > self.qTable[player_x][enemy_x][1]:
            return 0
        else:
            return 1

    def get_action(self, player, enemy):
        if random.random() <= self._epsilon:
            return random.randrange(2)
        return self.get_best_action(player, enemy)

    def update_ai(self, player, enemy, ai_action, ai_reward, new_pos_player, new_pos_enemy, is_done):
        a = self._alpha
        g = self._gamma
        if is_done:
            self.qTable[player][enemy][ai_action] += a * (ai_reward - self.qTable[player][enemy][ai_action])
        else:
            best_action = self.get_best_action(new_pos_player, new_pos_enemy)
            self.qTable[player][enemy][ai_action] += a * (
                    ai_reward + g * self.qTable[new_pos_player][new_pos_enemy][best_action] -
                    self.qTable[player][enemy][ai_action])

    def save_q_table(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.qTable, f)
            print("LOG: SAVED")

    def load_q_table(self, filename):
        with open(filename, 'rb') as f:
            self.qTable = pickle.load(f)
            print("LOG: LOADED")


# Setting up Sprites
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# P1.load_q_table("qTable.pkl")
# print(P1.qTable)
# time.sleep(2)
# Game Loop
while True:

    # Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.001
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    pos_player = P1.rect.centerx
    pos_enemy = E1.rect.centerx
    if pos_player < 0:
        pos_player = 0
    if pos_enemy < 0:
        pos_enemy = 0

    for _ in range(1):  # IF LEARNING CHANGE FOR HIGHER VALUE (FOR EX. 5000
        object_player = pygame.Rect((P1.rect.left, 0), (P1.rect.right, 0))
        object_enemy = pygame.Rect((E1.rect.left, 0), (E1.rect.right, 0))

        action = P1.get_best_action(int(pos_player), int(pos_enemy))  # IF LEARNING CHANGE FOR P1.get_action() not best
        new_pos = P1.ai_step(action)
        if new_pos < 0:
            new_pos = 0
        reward = 0
        if E1.rect.right >= P1.rect.left >= E1.rect.left or E1.rect.left <= P1.rect.right <= E1.rect.right:
            reward = -1
        else:
            reward = 1
        P1.update_ai(pos_player, pos_enemy, action, reward, new_pos, pos_enemy, False)
    SPEED = random.randint(6, 10)
    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        # for entity in all_sprites:
        #     entity.kill()
        time.sleep(0.1)
        # pygame.quit()
        # sys.exit()

        P1.save_q_table("qTable.pkl")
        DISPLAYSURF = pygame.display.set_mode((400, 600))
        DISPLAYSURF.fill(WHITE)
        pygame.display.set_caption("Game")
        E1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        P1.rect.center = (160, 520)
        SPEED = 7
        SCORE = 0

    pygame.display.update()
    FramePerSec.tick(FPS)
