import math
import random
import pygame

SCREEN_W = 800
SCREEN_H = 400
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
bg = pygame.image.load('C:/Users/hp/Desktop/Python/space-invaders-game-bg.jpg') #800, 400 -> w, h
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('C:/Users/hp/Desktop/Python/moon-icon.jpg')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('C:/Users/hp/Desktop/Python/rocket-player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
total_enemies = 6

for i in range(total_enemies):
    enemyImg.append(pygame.image.load('C:/Users/hp/Desktop/Python/enemy-sprite.png'))
    enemyX.append(random.randint(0, SCREEN_W - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletImg = pygame.image.load('C:/Users/hp/Desktop/Python/fire-bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bullet_State = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))
def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
def fire_bullet(x, y):
    global bullet_State
    bullet_State = "fire"
    screen.blit(bulletImg, (x+16, y+10))
def isCollision(enemyX, enemyY, )