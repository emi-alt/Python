import math
import random
import pygame

SCREEN_WIDTH = 736
SCREEN_HEIGHT = 736
PLAYER_START_X = 368
PLAYER_START_Y = 600
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 1
ENEMY_SPEED_Y = 4
BULLET_SPEED_Y = 4
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('C:\Users\hp\Desktop\Python\Recent files\underwater-bg-image.jpg.jpeg')#736x736

pygame.display.set_caption("Underwater Attack")
icon = pygame.image.load('pearl-icon.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('ACP/submarine-player-sprite.png') #130x130
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ACP/jellyfish-enemy.png')) #100x100
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64)) 
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletImg = pygame.image.load('ACP/bullet-sprite.png') #60x60
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y - 2
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE and bullet_state == "ready":
              bulletX = playerX
              fire_bullet(bulletX, bulletY)

    keys = pygame.key.get_pressed()
    playerX_change = 0
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        playerX_change = -2
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        playerX_change = 2

    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64)) 
    for i in range(num_of_enemies):
        if enemyY[i] > 340: 
            for j in range(num_of_enemies):
                enemyY[j] = 1000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 70:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 70)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()